import fs from "node:fs/promises";
import { Workbook } from "@oai/artifact-tool";


const csvPath = new URL(
  "../datos/03-archivos-importacion-shopify/orgie-tenga-svakom-shunga/" +
    "shopify-import-orgie-tenga-svakom-shunga-nuevos-con-imagenes.csv",
  import.meta.url,
);
const csvText = await fs.readFile(csvPath, "utf8");
const workbook = await Workbook.fromCSV(csvText, { sheetName: "Shopify import" });
const sheet = workbook.worksheets.getItem("Shopify import");
const usedRange = sheet.getUsedRange(true);
const values = usedRange.values;
const headers = values[0].map((header, position) =>
  position === 0 ? String(header).replace(/^\uFEFF/, "") : header,
);
const rows = values.slice(1);

const index = Object.fromEntries(headers.map((header, position) => [header, position]));
const required = [
  "Handle",
  "Title",
  "Variant SKU",
  "Image Src",
  "Image Position",
  "Image Alt Text",
  "Status",
];
const missingHeaders = required.filter((header) => index[header] === undefined);
const productRows = rows.filter((row) => String(row[index["Variant SKU"]] ?? "").trim());
const imageRows = rows.filter((row) => String(row[index["Image Src"]] ?? "").trim());
const invalidContinuationRows = rows.filter((row) => {
  const sku = String(row[index["Variant SKU"]] ?? "").trim();
  if (sku) return false;
  const populated = headers.filter((header, column) => {
    const value = String(row[column] ?? "").trim();
    return value && !["Handle", "Image Src", "Image Position", "Image Alt Text"].includes(header);
  });
  return populated.length > 0;
});

const summary = {
  rows: rows.length,
  columns: headers.length,
  products: productRows.length,
  imageRows: imageRows.length,
  missingHeaders,
  invalidContinuationRows: invalidContinuationRows.length,
};

if (
  summary.rows !== 348 ||
  summary.products !== 125 ||
  summary.imageRows !== 348 ||
  missingHeaders.length ||
  invalidContinuationRows.length
) {
  throw new Error(`CSV validation failed: ${JSON.stringify(summary)}`);
}

workbook.recalculate();
const inspection = await workbook.inspect({
  kind: "table",
  range: "Shopify import!A1:A6",
  include: "values",
  tableMaxRows: 6,
  tableMaxCols: 1,
  maxChars: 2000,
});
console.log(JSON.stringify(summary, null, 2));
console.log(inspection.ndjson);
