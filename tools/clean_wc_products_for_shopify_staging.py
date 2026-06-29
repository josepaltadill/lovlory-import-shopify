import csv
import json
from pathlib import Path


BASE = Path(r"E:\Projectes web\Globals\sexshoplorena")
INPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp.csv"
OUTPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp_limpio.csv"
REPORT = BASE / "wc-product-export-29-6-2026-marcas-mvp_limpieza_resumen.json"

KEEP_COLUMNS = [
    "ID",
    "Tipo",
    "SKU",
    "GTIN, UPC, EAN o ISBN",
    "Nombre",
    "Publicado",
    "¿Está destacado?",
    "Descripción corta",
    "Descripción",
    "Estado del impuesto",
    "¿Existencias?",
    "Inventario",
    "¿Permitir reservas de productos agotados?",
    "¿Vendido individualmente?",
    "Peso (g)",
    "Longitud (cm)",
    "Anchura (cm)",
    "Altura (cm)",
    "Precio normal",
    "Categorías",
    "Etiquetas",
    "Imágenes",
    "Marcas",
    "Meta: _yoast_wpseo_metadesc",
]


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True)
        return reader.fieldnames or [], list(reader)


def non_empty_count(rows: list[dict[str, str]], column: str) -> int:
    return sum(1 for row in rows if (row.get(column) or "").strip())


def main() -> None:
    fields, rows = read_rows(INPUT)
    missing = [column for column in KEEP_COLUMNS if column not in fields]
    if missing:
        raise SystemExit(f"Missing expected columns: {missing}")

    cleaned_rows = [{column: row.get(column, "") for column in KEEP_COLUMNS} for row in rows]
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=KEEP_COLUMNS,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            lineterminator="\r\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(cleaned_rows)

    _, reopened = read_rows(OUTPUT)
    dropped_columns = [column for column in fields if column not in KEEP_COLUMNS]
    empty_dropped = [column for column in dropped_columns if non_empty_count(rows, column) == 0]
    non_empty_dropped = [column for column in dropped_columns if non_empty_count(rows, column) > 0]

    summary = {
        "input": str(INPUT),
        "output": str(OUTPUT),
        "rows_input": len(rows),
        "rows_output": len(reopened),
        "columns_input": len(fields),
        "columns_output": len(KEEP_COLUMNS),
        "kept_columns": KEEP_COLUMNS,
        "dropped_columns_count": len(dropped_columns),
        "dropped_empty_columns": empty_dropped,
        "dropped_non_empty_columns": non_empty_dropped,
        "non_empty_counts_kept": {column: non_empty_count(reopened, column) for column in KEEP_COLUMNS},
        "output_size": OUTPUT.stat().st_size,
    }

    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if len(reopened) != len(rows):
        raise SystemExit("Validation failed: output row count changed")
    if len(reopened[0].keys()) != len(KEEP_COLUMNS):
        raise SystemExit("Validation failed: output column count mismatch")


if __name__ == "__main__":
    main()
