"""Add the prepared public image URLs to the supplier Shopify CSV."""

from __future__ import annotations

import csv
import json
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPLIER_DIR = (
    ROOT
    / "datos"
    / "03-archivos-importacion-shopify"
    / "orgie-tenga-svakom-shunga"
)
INPUT_CSV = (
    SUPPLIER_DIR
    / "shopify-import-orgie-tenga-svakom-shunga-nuevos-sin-imagenes.csv"
)
IMAGE_REPORT = (
    ROOT
    / "datos"
    / "05-informes-validacion"
    / "orgie-tenga-svakom-shunga-imagenes.json"
)
OUTPUT_CSV = (
    SUPPLIER_DIR
    / "shopify-import-orgie-tenga-svakom-shunga-nuevos-con-imagenes.csv"
)
VALIDATION_REPORT = (
    ROOT
    / "datos"
    / "05-informes-validacion"
    / "orgie-tenga-svakom-shunga-csv-con-imagenes.json"
)
IMAGE_BASE_URL = (
    "https://ilercavonia.info/lovlory/imagenes-para-subir-125-productos"
)


def check_image_url(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            content_type = response.headers.get_content_type()
            return {
                "url": url,
                "status": response.status,
                "content_type": content_type,
                "valid": response.status == 200 and content_type.startswith("image/"),
            }
    except (urllib.error.URLError, TimeoutError) as error:
        return {"url": url, "valid": False, "error": str(error)}


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def load_images_by_sku() -> dict[str, list[str]]:
    report = json.loads(IMAGE_REPORT.read_text(encoding="utf-8"))
    images: dict[str, list[str]] = defaultdict(list)
    for item in report["files"]:
        if item.get("valid") is not True or not item.get("relative_path"):
            continue
        sku = clean(item.get("sku"))
        relative_path = clean(item["relative_path"]).replace("\\", "/")
        url = f"{IMAGE_BASE_URL}/{relative_path}"
        if url not in images[sku]:
            images[sku].append(url)
    return dict(images)


def main() -> None:
    images_by_sku = load_images_by_sku()
    with INPUT_CSV.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("The input CSV has no header")
        source_rows = list(reader)

    required_columns = {
        "Handle",
        "Title",
        "Variant SKU",
        "Image Src",
        "Image Position",
        "Image Alt Text",
        "Status",
    }
    missing_columns = sorted(required_columns.difference(fieldnames))
    if missing_columns:
        raise ValueError(f"Missing Shopify columns: {missing_columns}")

    output_rows: list[dict[str, str]] = []
    missing_skus: list[str] = []
    source_skus: list[str] = []
    image_counts_by_brand: Counter[str] = Counter()

    for source_row in source_rows:
        sku = clean(source_row.get("Variant SKU"))
        source_skus.append(sku)
        image_urls = images_by_sku.get(sku, [])
        if not image_urls:
            missing_skus.append(sku)
            continue

        title = clean(source_row.get("Title"))
        brand = clean(source_row.get("Vendor"))
        for position, image_url in enumerate(image_urls, start=1):
            if position == 1:
                row = dict(source_row)
            else:
                row = {column: "" for column in fieldnames}
                row["Handle"] = clean(source_row.get("Handle"))
            row["Image Src"] = image_url
            row["Image Position"] = str(position)
            row["Image Alt Text"] = title
            output_rows.append(row)
            image_counts_by_brand[brand] += 1

    duplicate_source_skus = sorted(
        sku for sku, count in Counter(source_skus).items() if sku and count > 1
    )
    if missing_skus:
        raise ValueError(f"Products without a prepared image: {missing_skus}")
    if duplicate_source_skus:
        raise ValueError(f"Duplicate source SKUs: {duplicate_source_skus}")

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    full_rows = [row for row in output_rows if clean(row.get("Variant SKU"))]
    continuation_rows = [row for row in output_rows if not clean(row.get("Variant SKU"))]
    image_urls = [clean(row.get("Image Src")) for row in output_rows]
    with ThreadPoolExecutor(max_workers=16) as executor:
        remote_checks = list(executor.map(check_image_url, image_urls))
    failed_remote_urls = [item for item in remote_checks if item["valid"] is not True]
    validation = {
        "source_csv": str(INPUT_CSV.relative_to(ROOT)),
        "image_report": str(IMAGE_REPORT.relative_to(ROOT)),
        "output_csv": str(OUTPUT_CSV.relative_to(ROOT)),
        "image_base_url": IMAGE_BASE_URL,
        "products": len(full_rows),
        "output_data_rows": len(output_rows),
        "image_rows": len(image_urls),
        "continuation_image_rows": len(continuation_rows),
        "unique_image_urls": len(set(image_urls)),
        "public_image_urls_checked": len(remote_checks),
        "public_image_urls_valid": len(remote_checks) - len(failed_remote_urls),
        "public_image_url_failures": failed_remote_urls,
        "products_without_images": missing_skus,
        "duplicate_source_skus": duplicate_source_skus,
        "all_products_draft": all(
            clean(row.get("Status")).casefold() == "draft" for row in full_rows
        ),
        "images_by_brand": dict(sorted(image_counts_by_brand.items())),
    }
    VALIDATION_REPORT.parent.mkdir(parents=True, exist_ok=True)
    VALIDATION_REPORT.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    if failed_remote_urls:
        raise RuntimeError(
            f"Public validation failed for {len(failed_remote_urls)} image URLs"
        )


if __name__ == "__main__":
    main()
