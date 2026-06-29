import csv
import json
from collections import Counter
from pathlib import Path

import openpyxl


BASE = Path(r"E:\Projectes web\Globals\sexshoplorena")
WORKBOOK = BASE / "LovLory_estructura_colecciones_shopify_MVP_v1.xlsx"
TAXONOMY = BASE / "wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv"
OUTPUT = BASE / "shopify_collections_creation_plan.json"


def sheet_rows(wb, sheet_name: str) -> list[dict[str, object]]:
    ws = wb[sheet_name]
    headers = [ws.cell(3, col).value for col in range(1, ws.max_column + 1)]
    rows = []
    for row_idx in range(4, ws.max_row + 1):
        values = [ws.cell(row_idx, col).value for col in range(1, ws.max_column + 1)]
        if any(value not in (None, "") for value in values):
            rows.append(dict(zip(headers, values)))
    return rows


def main() -> None:
    wb = openpyxl.load_workbook(WORKBOOK, data_only=True)
    principal = sheet_rows(wb, "Colecciones principales")
    secondary = sheet_rows(wb, "Colecciones secundarias")
    brands = sheet_rows(wb, "Colecciones marcas")

    with TAXONOMY.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    commercial_collections = Counter()
    tags = Counter()
    product_types = Counter()
    vendors = Counter()
    for row in rows:
        vendors[row["Vendor Shopify"]] += 1
        product_types[row["Product type Shopify"]] += 1
        for collection in [item.strip() for item in row["Colecciones comerciales Shopify"].split(",") if item.strip()]:
            commercial_collections[collection] += 1
        for tag in [item.strip() for item in row["Tags Shopify"].split(",") if item.strip()]:
            tags[tag] += 1

    plan = {
        "principal_from_excel": [
            {
                "title": row.get("Colección principal"),
                "level": row.get("Nivel menú"),
                "block": row.get("Bloque menú"),
                "handle": row.get("Handle sugerido"),
                "rule": row.get("Regla de inclusión"),
            }
            for row in principal
        ],
        "secondary_from_excel": [
            {
                "title": row.get("Colección secundaria"),
                "handle": row.get("Handle sugerido"),
                "rule": row.get("Regla / alimentación"),
            }
            for row in secondary
        ],
        "brands_from_excel": [
            {
                "title": row.get("Marca / Vendor"),
                "handle": row.get("Handle colección marca"),
                "rule": row.get("Regla automática"),
            }
            for row in brands
        ],
        "product_taxonomy_counts": {
            "commercial_collections": dict(commercial_collections),
            "tags": dict(tags),
            "product_types": dict(product_types),
            "vendors": dict(vendors),
        },
    }
    OUTPUT.write_text(json.dumps(plan, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(json.dumps(plan, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
