"""Prepare only the supplier images needed by the filtered Shopify import."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

import openpyxl
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SUPPLIER_DIR = (
    ROOT
    / "datos"
    / "03-archivos-importacion-shopify"
    / "orgie-tenga-svakom-shunga"
)
SOURCE_XLSX = SUPPLIER_DIR / "productos de Tenga, Shunga, Svakom i Orgie.xlsx"
IMPORT_CSV = (
    SUPPLIER_DIR
    / "shopify-import-orgie-tenga-svakom-shunga-nuevos-sin-imagenes.csv"
)
OUTPUT_DIR = SUPPLIER_DIR / "imagenes-para-subir-125-productos"
REPORT_PATH = (
    ROOT
    / "datos"
    / "05-informes-validacion"
    / "orgie-tenga-svakom-shunga-imagenes.json"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--download-missing",
        action="store_true",
        help="Download images absent from the extracted ZIP folders.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze without copying, downloading, or writing the report.",
    )
    return parser.parse_args()


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def load_selected_skus() -> set[str]:
    with IMPORT_CSV.open("r", encoding="utf-8", newline="") as stream:
        return {
            clean(row["Variant SKU"])
            for row in csv.DictReader(stream)
            if clean(row.get("Variant SKU"))
        }


def load_required_images(selected_skus: set[str]) -> list[dict[str, str]]:
    workbook = openpyxl.load_workbook(SOURCE_XLSX, read_only=True, data_only=True)
    sheet = workbook.active
    required: list[dict[str, str]] = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        sku = clean(row[0])
        if sku not in selected_skus:
            continue
        brand = clean(row[4]).lower()
        for url in clean(row[7]).split(","):
            url = url.strip()
            if not url:
                continue
            filename = urllib.parse.unquote(Path(urllib.parse.urlparse(url).path).name)
            required.append(
                {"sku": sku, "brand": brand, "filename": filename, "source_url": url}
            )
    workbook.close()
    return required


def extracted_index(brand: str) -> dict[str, Path]:
    folder = SUPPLIER_DIR / brand
    return {
        item.name.casefold(): item
        for item in folder.rglob("*")
        if item.is_file()
    }


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    partial = destination.with_suffix(destination.suffix + ".part")
    with urllib.request.urlopen(request, timeout=60) as response, partial.open("wb") as stream:
        shutil.copyfileobj(response, stream)
    partial.replace(destination)


def validate_image(path: Path) -> dict[str, object]:
    try:
        with Image.open(path) as image:
            width, height = image.size
            image_format = image.format
            image.verify()
        return {
            "valid": True,
            "format": image_format,
            "width": width,
            "height": height,
            "bytes": path.stat().st_size,
        }
    except Exception as error:  # Pillow provides the useful validation detail.
        return {"valid": False, "error": str(error), "bytes": path.stat().st_size}


def main() -> None:
    args = parse_args()
    selected_skus = load_selected_skus()
    required = load_required_images(selected_skus)
    indexes = {brand: extracted_index(brand) for brand in {item["brand"] for item in required}}
    records: list[dict[str, object]] = []

    for item in required:
        destination = OUTPUT_DIR / item["brand"] / item["filename"]
        source = indexes[item["brand"]].get(item["filename"].casefold())
        if source is None:
            compact_sku = re.sub(r"[^a-z0-9]", "", item["sku"].casefold())
            filename_path = Path(item["filename"])
            compact_stem = filename_path.stem.casefold()
            if compact_stem.startswith(compact_sku):
                suffix = compact_stem[len(compact_sku) :]
                alternative = f"{item['sku']}{suffix}{filename_path.suffix}".casefold()
                source = indexes[item["brand"]].get(alternative)
        status = "missing"
        if source:
            status = "available_in_zip"
            if not args.dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination = destination.with_name(source.name)
                shutil.copy2(source, destination)
                status = "copied_from_zip"
        elif destination.exists() and not args.dry_run:
            status = "already_prepared"
        elif args.download_missing and not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            try:
                download(item["source_url"], destination)
                status = "downloaded"
            except Exception as error:
                records.append({**item, "status": "download_failed", "error": str(error)})
                continue

        record: dict[str, object] = {**item, "status": status}
        if not args.dry_run and destination.exists():
            record["relative_path"] = destination.relative_to(OUTPUT_DIR).as_posix()
            record.update(validate_image(destination))
        records.append(record)

    counts = Counter(record["status"] for record in records)
    report = {
        "source_products_selected": len(selected_skus),
        "required_images": len(required),
        "unique_required_images": len(
            {(item["brand"], item["filename"].casefold()) for item in required}
        ),
        "output_directory": str(OUTPUT_DIR.relative_to(ROOT)),
        "status_counts": dict(sorted(counts.items())),
        "valid_images": sum(record.get("valid") is True for record in records),
        "invalid_images": sum(record.get("valid") is False for record in records),
        "missing_or_failed": sum(
            record["status"] in {"missing", "download_failed"} for record in records
        ),
        "by_brand": {
            brand: {
                "images": sum(record["brand"] == brand for record in records),
                "missing_or_failed": sum(
                    record["brand"] == brand
                    and record["status"] in {"missing", "download_failed"}
                    for record in records
                ),
            }
            for brand in sorted({record["brand"] for record in records})
        },
        "files": records,
    }

    if not args.dry_run:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(json.dumps({key: value for key, value in report.items() if key != "files"}, indent=2))


if __name__ == "__main__":
    main()
