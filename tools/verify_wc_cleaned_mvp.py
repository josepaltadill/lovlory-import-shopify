import csv
import json
import re
from collections import Counter
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "datos" / "02-datos-intermedios" / "wc-product-export-29-6-2026-marcas-mvp_limpio.csv"
TARGETS = {"ORGIE", "SVAKOM", "TENGA", "MISTRESS"}


def brand_tokens(value: str) -> list[str]:
    return [brand.strip().upper() for brand in re.split(r"[,|;]", value or "") if brand.strip()]


def main() -> None:
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True)
        rows = list(reader)
        fields = reader.fieldnames or []

    outside = sorted({brand for row in rows for brand in brand_tokens(row.get("Marcas", "")) if brand not in TARGETS})
    empty_required = {
        column: sum(1 for row in rows if not (row.get(column) or "").strip())
        for column in ["ID", "SKU", "Nombre", "Precio normal", "Marcas", "Imágenes"]
    }
    summary = {
        "rows": len(rows),
        "columns": len(fields),
        "brands": dict(Counter(brand for row in rows for brand in brand_tokens(row.get("Marcas", "")))),
        "outside_brands": outside,
        "empty_required_counts": empty_required,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if len(rows) != 189 or len(fields) != 24:
        raise SystemExit("Unexpected row or column count")
    if outside:
        raise SystemExit("Unexpected brand outside MVP list")


if __name__ == "__main__":
    main()
