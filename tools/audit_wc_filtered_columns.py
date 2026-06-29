import csv
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp.csv"
OUTPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp_columnas_resumen.json"


def main() -> None:
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True)
        rows = list(reader)
        fields = reader.fieldnames or []

    stats = []
    for field in fields:
        values = [(row.get(field) or "").strip() for row in rows]
        samples = []
        for value in values:
            if value and value not in samples:
                samples.append(value)
            if len(samples) >= 3:
                break
        stats.append(
            {
                "field": field,
                "non_empty": sum(1 for value in values if value),
                "empty": sum(1 for value in values if not value),
                "unique": len({value for value in values if value}),
                "samples": samples,
            }
        )

    summary = {
        "input": str(INPUT),
        "rows": len(rows),
        "columns": len(fields),
        "empty_columns": [item["field"] for item in stats if item["non_empty"] == 0],
        "non_empty_columns": [item["field"] for item in stats if item["non_empty"] > 0],
        "stats": stats,
    }
    OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
