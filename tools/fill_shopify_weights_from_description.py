import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_TAXONOMY = ROOT / "datos" / "02-datos-intermedios" / "wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv"
SOURCE_IMPORT = ROOT / "datos" / "03-archivos-importacion-shopify" / "shopify_import_lovlory_mvp_productos.csv"
OUTPUT_IMPORT = ROOT / "datos" / "03-archivos-importacion-shopify" / "shopify_import_lovlory_mvp_productos_con_pesos.csv"
SUMMARY = ROOT / "datos" / "05-informes-validacion" / "shopify_import_lovlory_mvp_productos_con_pesos_resumen.json"


WEIGHT_PATTERNS = [
    re.compile(r"(?i)weight\s*:\s*([0-9]+(?:[.,][0-9]+)?)\s*kg\b"),
    re.compile(r"(?i)peso\s*:\s*([0-9]+(?:[.,][0-9]+)?)\s*kg\b"),
    re.compile(r"(?i)el\s+peso\s+del\s+producto\s+es\s+de\s+([0-9]+(?:[.,][0-9]+)?)\s*kg\b"),
    re.compile(r"(?i)peso\s+del\s+producto\s*:?\s*([0-9]+(?:[.,][0-9]+)?)\s*g\b"),
    re.compile(r"(?i)peso\s*\(g\)\s*:?\s*([0-9]+(?:[.,][0-9]+)?)\b"),
    re.compile(r"(?i)aprox\.?\s*:?\s*([0-9]+(?:[.,][0-9]+)?)\s*g\b"),
    re.compile(r"(?i)peso\s*;?\s*([0-9]+(?:[.,][0-9]+)?)\s*gramos\b"),
    re.compile(r"(?i)peso\s*;?\s*([0-9]+(?:[.,][0-9]+)?)\s*g\b"),
]


def parse_decimal(value: str) -> float:
    return float(value.replace(",", "."))


def extract_grams(text: str) -> int | None:
    if not text:
        return None

    normalized = text.replace("&nbsp;", " ")
    for pattern in WEIGHT_PATTERNS:
        match = pattern.search(normalized)
        if not match:
            continue

        amount = parse_decimal(match.group(1))
        matched_text = match.group(0).lower()
        if "kg" in matched_text:
            return int(round(amount * 1000))
        return int(round(amount))

    return None


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    taxonomy_rows = read_csv(SOURCE_TAXONOMY)
    import_rows = read_csv(SOURCE_IMPORT)

    grams_by_sku: dict[str, int] = {}
    extraction_examples: list[dict[str, str | int]] = []

    for row in taxonomy_rows:
        sku = row.get("SKU", "").strip()
        grams = extract_grams(row.get("Descripción", ""))
        if not sku or not grams:
            continue
        grams_by_sku[sku] = grams
        if len(extraction_examples) < 25:
            extraction_examples.append(
                {
                    "sku": sku,
                    "nombre": row.get("Nombre", ""),
                    "grams": grams,
                }
            )

    updated = []
    already_had_weight = 0
    still_zero = 0

    for row in import_rows:
        sku = row.get("Variant SKU", "").strip()
        current = row.get("Variant Grams", "").strip()
        if not sku:
            continue

        try:
            current_grams = int(float(current or "0"))
        except ValueError:
            current_grams = 0

        if current_grams > 0:
            already_had_weight += 1
            continue

        extracted = grams_by_sku.get(sku)
        if extracted:
            row["Variant Grams"] = str(extracted)
            row["Variant Weight Unit"] = "g"
            updated.append(
                {
                    "handle": row.get("Handle", ""),
                    "title": row.get("Title", ""),
                    "sku": sku,
                    "grams": extracted,
                }
            )
        else:
            still_zero += 1

    fieldnames = list(import_rows[0].keys())
    write_csv(OUTPUT_IMPORT, fieldnames, import_rows)

    SUMMARY.write_text(
        json.dumps(
            {
                "source_import": SOURCE_IMPORT.name,
                "output_import": OUTPUT_IMPORT.name,
                "products_already_had_weight": already_had_weight,
                "products_updated_from_description": len(updated),
                "products_still_zero_weight": still_zero,
                "updated": updated,
                "extraction_examples": extraction_examples,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(json.dumps(json.loads(SUMMARY.read_text(encoding="utf-8")), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
