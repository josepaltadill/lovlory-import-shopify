import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const inputPath = path.join(
  repoRoot,
  "datos",
  "07-colecciones",
  "LovLory_estructura_colecciones_shopify_MVP_v1.xlsx",
);
const outputPath = path.join(
  repoRoot,
  "recursos-visuales",
  "lovlory_mvp_decisiones_preview.png",
);

const input = await FileBlob.load(inputPath);
const workbook = await SpreadsheetFile.importXlsx(input);

const overview = await workbook.inspect({
  kind: "sheet,table",
  tableMaxRows: 5,
  tableMaxCols: 4,
  maxChars: 4000,
});
console.log(overview.ndjson);

const preview = await workbook.render({
  sheetName: "Decisiones MVP",
  range: "A1:D11",
  scale: 1,
  format: "png",
});

await fs.writeFile(outputPath, new Uint8Array(await preview.arrayBuffer()));
console.log(outputPath);
