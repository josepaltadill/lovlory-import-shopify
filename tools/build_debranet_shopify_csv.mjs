import fs from "node:fs/promises";
import path from "node:path";
import { Workbook } from "@oai/artifact-tool";

const [inputJson, outputCsv, summaryJson, previewPng] = process.argv.slice(2);
if (!inputJson || !outputCsv || !summaryJson || !previewPng) {
  throw new Error("Expected input JSON, output CSV, summary JSON, and preview PNG paths");
}

const data = JSON.parse(await fs.readFile(inputJson, "utf8"));
const matrix = [data.headers, ...data.rows];
const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Shopify import");
sheet.getRange("A1").write(matrix);
sheet.freezePanes.freezeRows(1);
sheet.showGridLines = false;

const used = sheet.getUsedRange();
used.format.font = { name: "Arial", size: 10 };
sheet.getRangeByIndexes(0, 0, 1, data.headers.length).format = {
  fill: "#1F4E78",
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
  verticalAlignment: "center",
  horizontalAlignment: "center",
  wrapText: true,
};
used.format.autofitColumns();
sheet.getRange("A:A").format.columnWidth = 30;
sheet.getRange("B:B").format.columnWidth = 32;
sheet.getRange("C:C").format.columnWidth = 60;
sheet.getRange("W:W").format.columnWidth = 55;
sheet.getRange("Y:Y").format.columnWidth = 35;

workbook.recalculate();
const inspection = await workbook.inspect({
  kind: "table",
  range: "Shopify import!A1:Z8",
  include: "values,formulas",
  tableMaxRows: 8,
  tableMaxCols: 26,
  maxChars: 12000,
});
const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});

const preview = await workbook.render({
  sheetName: "Shopify import",
  range: "A1:Z8",
  scale: 1,
  format: "png",
});
await fs.mkdir(path.dirname(previewPng), { recursive: true });
await fs.writeFile(previewPng, new Uint8Array(await preview.arrayBuffer()));

const quoteCsv = (value) => {
  const stringValue = value == null ? "" : String(value);
  return /[",\r\n]/.test(stringValue) ? `"${stringValue.replaceAll('"', '""')}"` : stringValue;
};
const csv = `\uFEFF${matrix.map((row) => row.map(quoteCsv).join(",")).join("\r\n")}\r\n`;
await fs.mkdir(path.dirname(outputCsv), { recursive: true });
await fs.writeFile(outputCsv, csv, "utf8");

const headerIndex = Object.fromEntries(data.headers.map((header, index) => [header, index]));
const productRows = data.rows.filter((row) => row[headerIndex.SKU]);
const duplicateValues = (values) => {
  const counts = new Map();
  for (const value of values) counts.set(value, (counts.get(value) ?? 0) + 1);
  return [...counts.entries()].filter(([, count]) => count > 1).map(([value]) => value);
};
const missing = (header) => productRows.filter((row) => !String(row[headerIndex[header]] ?? "").trim()).length;
const brands = Object.fromEntries(
  [...new Set(productRows.map((row) => row[headerIndex.Vendor]))]
    .sort()
    .map((brand) => [brand, productRows.filter((row) => row[headerIndex.Vendor] === brand).length]),
);

const summary = {
  source: data.source,
  output: path.basename(outputCsv),
  language: data.language,
  price_mapping: data.price_mapping,
  cost_mapping: data.cost_mapping,
  products: productRows.length,
  rows: data.rows.length,
  image_rows: data.rows.filter((row) => row[headerIndex["Product image URL"]]).length,
  brands,
  out_of_stock_products: productRows.filter((row) => Number(row[headerIndex["Inventory quantity"]]) === 0).length,
  duplicate_handles: duplicateValues(productRows.map((row) => row[headerIndex["URL handle"]])),
  duplicate_skus: duplicateValues(productRows.map((row) => row[headerIndex.SKU])),
  missing_required_product_fields: Object.fromEntries(
    ["Title", "URL handle", "SKU", "Price", "Weight value (grams)", "Product image URL"].map((header) => [header, missing(header)]),
  ),
  invalid_image_urls: data.rows.filter((row) => {
    const url = row[headerIndex["Product image URL"]];
    return url && !String(url).startsWith("https://");
  }).length,
  validation: {
    inspected_range: "Shopify import!A1:Z8",
    inspection: inspection.ndjson,
    formula_error_scan: formulaErrors.ndjson,
  },
};
await fs.writeFile(summaryJson, `${JSON.stringify(summary, null, 2)}\n`, "utf8");
console.log(JSON.stringify({ ...summary, validation: undefined }, null, 2));
