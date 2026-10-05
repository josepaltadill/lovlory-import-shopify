import fs from "node:fs/promises";
import path from "node:path";
import { Workbook } from "@oai/artifact-tool";

const root = process.cwd();
const sourceDir = path.join(
  root,
  "datos",
  "03-archivos-importacion-shopify",
  "orgie-tenga-svakom-shunga",
);
const csvPath = path.join(
  sourceDir,
  "shopify-import-orgie-tenga-svakom-shunga-nuevos-sin-imagenes.csv",
);
const reportPath = path.join(
  sourceDir,
  "shopify-import-orgie-tenga-svakom-shunga-validacion.json",
);
const products = JSON.parse(
  await fs.readFile(path.join(root, ".codex-tmp", "new-products.json"), "utf8"),
);
const duplicateSummary = JSON.parse(
  await fs.readFile(path.join(root, ".codex-tmp", "duplicate-summary.json"), "utf8"),
);
const imageChecks = JSON.parse(
  await fs.readFile(path.join(root, ".codex-tmp", "image-check-results.json"), "utf8"),
);

const headers = [
  "Handle",
  "Title",
  "Body (HTML)",
  "Vendor",
  "Product Category",
  "Type",
  "Tags",
  "Published",
  "Option1 Name",
  "Option1 Value",
  "Option2 Name",
  "Option2 Value",
  "Option3 Name",
  "Option3 Value",
  "Variant SKU",
  "Variant Grams",
  "Variant Inventory Tracker",
  "Variant Inventory Qty",
  "Variant Inventory Policy",
  "Variant Fulfillment Service",
  "Variant Price",
  "Variant Compare At Price",
  "Variant Requires Shipping",
  "Variant Taxable",
  "Variant Barcode",
  "Image Src",
  "Image Position",
  "Image Alt Text",
  "Gift Card",
  "SEO Title",
  "SEO Description",
  "Google Shopping / Google Product Category",
  "Google Shopping / Gender",
  "Google Shopping / Age Group",
  "Google Shopping / MPN",
  "Google Shopping / Condition",
  "Google Shopping / Custom Product",
  "Variant Image",
  "Variant Weight Unit",
  "Variant Tax Code",
  "Cost per item",
  "Status",
];

function clean(value) {
  return String(value ?? "")
    .replaceAll("_x000D_", "\n")
    .replace(/\r\n?/g, "\n")
    .trim();
}

function slugify(value) {
  return clean(value)
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 180);
}

function htmlEscape(value) {
  return clean(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function bodyHtml(product) {
  const paragraphs = clean(product.description)
    .split(/\n{2,}/)
    .map((item) => item.replace(/\n+/g, " ").trim())
    .filter(Boolean)
    .map((item) => `<p>${htmlEscape(item)}</p>`);
  const details = [
    ["Características", product.features],
    ["Batería", product.battery],
    ["Material", product.material],
    ["Color", product.color],
    ["Dimensiones", product.dimensions],
    ["Ingredientes", product.ingredients],
  ].filter(([, value]) => clean(value));
  if (details.length) {
    paragraphs.push(
      `<ul>${details
        .map(
          ([label, value]) =>
            `<li><strong>${label}:</strong> ${htmlEscape(value)}</li>`,
        )
        .join("")}</ul>`,
    );
  }
  return paragraphs.join("");
}

function numberOrBlank(value) {
  const normalized = clean(value).replace(",", ".");
  if (!normalized) return "";
  const parsed = Number(normalized);
  return Number.isFinite(parsed) && parsed >= 0 ? parsed : "";
}

function gramsOrBlank(value) {
  const text = clean(value).toLowerCase();
  if (!text) return "";
  const matches = [...text.matchAll(/(\d+(?:[.,]\d+)?)\s*(kg|mg|gr|g)\b/g)];
  if (!matches.length) return "";
  const grams = matches.reduce((sum, match) => {
    const amount = Number(match[1].replace(",", "."));
    const unit = match[2];
    if (unit === "kg") return sum + amount * 1000;
    if (unit === "mg") return sum + amount / 1000;
    return sum + amount;
  }, 0);
  return Number.isFinite(grams) && grams > 0 ? Math.round(grams) : "";
}

function productType(product) {
  if (product.brand === "ORGIE" || product.brand === "SHUNGA") {
    return "Cosmética íntima";
  }
  if (product.brand === "SVAKOM") return "Juguetes eróticos";
  if (/lotion|lubric/i.test(product.title)) return "Cosmética íntima";
  return "Masturbador masculino";
}

function tags(product) {
  const values = [`vendor-${product.brand.toLowerCase()}`];
  if (product.brand === "ORGIE" || product.brand === "SHUNGA") {
    values.push("cosmetica-intima");
  } else if (product.brand === "SVAKOM") {
    values.push("juguetes-eroticos");
  } else if (/lotion|lubric/i.test(product.title)) {
    values.push("cosmetica-intima", "lubricante");
  } else {
    values.push("juguetes-eroticos", "tipo-masturbador");
  }
  if (clean(product.category).toUpperCase() === "NOVEDADES") values.push("novedad");
  return values.join(", ");
}

function seoDescription(product) {
  return clean(product.description).replace(/\s+/g, " ").slice(0, 320);
}

const rows = products.map((product) => [
  `${slugify(product.title)}-${slugify(product.sku)}`,
  clean(product.title),
  bodyHtml(product),
  product.brand,
  "",
  productType(product),
  tags(product),
  false,
  "Title",
  "Default Title",
  "",
  "",
  "",
  "",
  clean(product.sku),
  gramsOrBlank(product.product_weight),
  "shopify",
  numberOrBlank(product.stock),
  "deny",
  "manual",
  numberOrBlank(product.recommended_price),
  "",
  true,
  true,
  clean(product.ean),
  "",
  "",
  "",
  false,
  clean(product.title),
  seoDescription(product),
  "",
  "",
  "adult",
  clean(product.sku),
  "new",
  false,
  "",
  "g",
  "",
  numberOrBlank(product.cost),
  "draft",
]);

const matrix = [headers, ...rows];
const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Shopify import");
sheet.getRangeByIndexes(0, 0, matrix.length, headers.length).values = matrix;
sheet.freezePanes.freezeRows(1);
sheet.getRangeByIndexes(0, 0, matrix.length, headers.length).format.font = {
  name: "Arial",
  size: 10,
};
sheet.getRangeByIndexes(0, 0, 1, headers.length).format = {
  fill: "#1F4E78",
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
  verticalAlignment: "center",
};
sheet.showGridLines = false;
workbook.recalculate();

function csvCell(value) {
  const text = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

const csvText = `${matrix.map((row) => row.map(csvCell).join(",")).join("\r\n")}\r\n`;
await fs.writeFile(csvPath, csvText, "utf8");

const handles = rows.map((row) => row[0]);
const skus = rows.map((row) => row[14]);
const barcodes = rows.map((row) => row[24]).filter(Boolean);
const brandCounts = Object.fromEntries(
  ["ORGIE", "SHUNGA", "SVAKOM", "TENGA"].map((brand) => [
    brand,
    products.filter((product) => product.brand === brand).length,
  ]),
);
const outputImageUrls = products.flatMap((product) =>
  clean(product.images)
    .split(",")
    .map((url) => url.trim())
    .filter(Boolean),
);
const outputUrlSet = new Set(outputImageUrls);
const outputImageResults = imageChecks.results.filter((result) =>
  outputUrlSet.has(result.url),
);
const failures = outputImageResults.filter((result) => !result.ok);

const report = {
  source_file: path.relative(root, path.join(sourceDir, "productos de Tenga, Shunga, Svakom i Orgie.xlsx")),
  output_file: path.relative(root, csvPath),
  generated_at: new Date().toISOString(),
  source_products: Object.values(duplicateSummary).reduce(
    (sum, brand) => sum + brand.source,
    0,
  ),
  duplicate_analysis: duplicateSummary,
  new_candidates_before_exclusions: Object.values(duplicateSummary).reduce(
    (sum, brand) => sum + brand.new,
    0,
  ),
  exclusions: {
    material_pos: 10,
    testers_and_displays_outside_material_pos: 26,
    total_non_sale_items: 36,
  },
  output_products: products.length,
  output_products_by_brand: brandCounts,
  field_mapping: {
    "Variant Price": "PVP Recomendado",
    "Cost per item": "Precio",
    "Variant SKU": "SKU",
    "Variant Barcode": "EAN",
    "Variant Inventory Qty": "Cantidad",
    "Variant Grams": "Peso del Producto, convertido a gramos cuando es interpretable",
  },
  publication: {
    status: "draft",
    published: false,
    reason: "Las URL del proveedor no son HTTPS y las imágenes se han omitido.",
  },
  images: {
    urls_declared_for_output_products: outputImageUrls.length,
    urls_checked: outputImageResults.length,
    accessible_over_http: outputImageResults.filter((result) => result.ok).length,
    failed: failures.length,
    https_compatible: 0,
    omitted_from_csv: true,
    failed_urls: failures.map((result) => result.url),
  },
  completeness: {
    missing_source_image_urls: products.filter((product) => !clean(product.images)).length,
    missing_variant_price: rows.filter((row) => row[20] === "").length,
    missing_variant_weight: rows.filter((row) => row[15] === "").length,
    zero_or_missing_stock: rows.filter((row) => row[17] === "" || row[17] <= 0).length,
    missing_description: products.filter((product) => !clean(product.description)).length,
  },
  validation: {
    duplicate_handles: handles.length - new Set(handles).size,
    duplicate_skus: skus.length - new Set(skus).size,
    duplicate_barcodes: barcodes.length - new Set(barcodes).size,
    blank_skus: skus.filter((sku) => !sku).length,
    invalid_prices: rows.filter(
      (row) => row[20] !== "" && (!Number.isFinite(row[20]) || row[20] < 0),
    ).length,
    all_rows_draft: rows.every((row) => row[41] === "draft"),
    image_columns_blank: rows.every((row) => row[25] === "" && row[37] === ""),
  },
  tenga_deduplication_note:
    "Se excluyeron 14 coincidencias claras por modelo. 3DX ZEN y 3D Pile se conservaron porque no son equivalencias inequívocas con los productos 3D Zen y 3D Module actuales.",
};
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");

const finalWorkbook = await Workbook.fromCSV(csvText, { sheetName: "Shopify import" });
const inspected = await finalWorkbook.inspect({
  kind: "table",
  range: "Shopify import!A1:AP8",
  include: "values,formulas",
  tableMaxRows: 8,
  tableMaxCols: 42,
  maxChars: 12000,
});
console.log(inspected.ndjson);
const errors = await finalWorkbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 50 },
  summary: "final formula error scan",
});
console.log(errors.ndjson);
const preview = await finalWorkbook.render({
  sheetName: "Shopify import",
  range: "A1:H12",
  scale: 1,
  format: "png",
});
await fs.writeFile(
  path.join(root, ".codex-tmp", "shopify-import-preview.png"),
  new Uint8Array(await preview.arrayBuffer()),
);
console.log(JSON.stringify({ csvPath, reportPath, products: products.length, brandCounts }));
