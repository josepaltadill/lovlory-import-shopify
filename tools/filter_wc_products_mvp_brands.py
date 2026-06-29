import csv
import json
import re
from collections import Counter
from pathlib import Path


BASE = Path(r"E:\Projectes web\Globals\sexshoplorena")
SOURCE = BASE / "wc-product-export-29-6-2026-1782741544086.csv"
OUTPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp.csv"
REPORT = BASE / "wc-product-export-29-6-2026-marcas-mvp_resumen.json"
TARGETS = {"ORGIE", "SVAKOM", "TENGA", "MISTRESS"}


def brand_tokens(row: dict[str, str]) -> list[str]:
    value = row.get("Marcas") or ""
    return [brand.strip().upper() for brand in re.split(r"[,|;]", value) if brand.strip()]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(
            handle,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            skipinitialspace=False,
        )
        return reader.fieldnames or [], list(reader)


def direct_keep(row: dict[str, str]) -> bool:
    return bool(TARGETS.intersection(brand_tokens(row)))


def is_child_of_kept(row: dict[str, str], keep_ids: set[str], keep_skus: set[str]) -> bool:
    parent = (row.get("Superior") or "").strip()
    if not parent:
        return False
    parent_clean = parent.replace("id:", "").strip()
    return parent in keep_ids or parent in keep_skus or parent_clean in keep_ids or parent_clean in keep_skus


def main() -> None:
    fields, rows = read_csv(SOURCE)

    keep_ids = {row.get("ID", "").strip() for row in rows if direct_keep(row) and row.get("ID", "").strip()}
    keep_skus = {row.get("SKU", "").strip() for row in rows if direct_keep(row) and row.get("SKU", "").strip()}
    kept = [row for row in rows if direct_keep(row) or is_child_of_kept(row, keep_ids, keep_skus)]

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            lineterminator="\r\n",
            extrasaction="ignore",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(kept)

    _, check_rows = read_csv(OUTPUT)
    outside_brands = sorted({brand for row in check_rows for brand in brand_tokens(row) if brand not in TARGETS})

    summary = {
        "source": str(SOURCE),
        "output": str(OUTPUT),
        "total_rows": len(rows),
        "kept_rows_written": len(kept),
        "kept_rows_reopened": len(check_rows),
        "removed_rows": len(rows) - len(kept),
        "target_brands": sorted(TARGETS),
        "kept_by_brand": dict(Counter(next((brand for brand in brand_tokens(row) if brand in TARGETS), "[variation/child]") for row in check_rows)),
        "kept_by_type": dict(Counter(row.get("Tipo", "") for row in check_rows)),
        "outside_brands_after_filter": outside_brands,
        "field_count": len(fields),
        "output_size": OUTPUT.stat().st_size,
    }

    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if len(check_rows) != len(kept):
        raise SystemExit("Validation failed: reopened row count does not match written row count")
    if outside_brands:
        raise SystemExit("Validation failed: outside brands remain after filtering")


if __name__ == "__main__":
    main()
