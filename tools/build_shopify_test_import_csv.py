import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
FULL = BASE / "shopify_import_lovlory_mvp_productos.csv"
OUTPUT = BASE / "shopify_import_lovlory_mvp_test.csv"
REPORT = BASE / "shopify_import_lovlory_mvp_test_resumen.json"


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True)
        return reader.fieldnames or [], list(reader)


def main() -> None:
    fields, rows = read_rows(FULL)
    product_rows = [row for row in rows if row.get("Title")]

    selected_handles = []
    for vendor in ["TENGA", "ORGIE", "SVAKOM", "MISTRESS"]:
        for row in product_rows:
            if row.get("Vendor") == vendor and row.get("Status") == "active":
                selected_handles.append(row["Handle"])
                break

    draft_handle = next((row["Handle"] for row in product_rows if row.get("Status") == "draft"), None)
    if draft_handle:
        selected_handles.append(draft_handle)

    selected_handles = list(dict.fromkeys(selected_handles))
    selected = [row for row in rows if row.get("Handle") in selected_handles]

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            lineterminator="\r\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(selected)

    _, reopened = read_rows(OUTPUT)
    product_selected = [row for row in reopened if row.get("Title")]
    image_counts = defaultdict(int)
    for row in reopened:
        if row.get("Image Src"):
            image_counts[row["Handle"]] += 1

    report = {
        "source": str(FULL),
        "output": str(OUTPUT),
        "selected_handles": selected_handles,
        "csv_rows": len(reopened),
        "product_rows": len(product_selected),
        "image_rows_total": sum(image_counts.values()),
        "products": [
            {
                "handle": row["Handle"],
                "title": row["Title"],
                "vendor": row["Vendor"],
                "type": row["Type"],
                "status": row["Status"],
                "price": row["Variant Price"],
                "images": image_counts[row["Handle"]],
                "tags": row["Tags"],
            }
            for row in product_selected
        ],
        "status_counts": dict(Counter(row["Status"] for row in product_selected)),
        "vendor_counts": dict(Counter(row["Vendor"] for row in product_selected)),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if len(product_selected) != len(selected_handles):
        raise SystemExit("Validation failed: product row count mismatch")


if __name__ == "__main__":
    main()
