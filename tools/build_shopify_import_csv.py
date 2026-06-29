import csv
import html
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv"
OUTPUT = BASE / "shopify_import_lovlory_mvp_productos.csv"
REPORT = BASE / "shopify_import_lovlory_mvp_productos_resumen.json"

SHOPIFY_COLUMNS = [
    "Handle",
    "Title",
    "Body (HTML)",
    "Vendor",
    "Product Category",
    "Type",
    "Tags",
    "Published",
    "Option1 Name",
    "Option1 Value",
    "Option2 Name",
    "Option2 Value",
    "Option3 Name",
    "Option3 Value",
    "Variant SKU",
    "Variant Grams",
    "Variant Inventory Tracker",
    "Variant Inventory Qty",
    "Variant Inventory Policy",
    "Variant Fulfillment Service",
    "Variant Price",
    "Variant Compare At Price",
    "Variant Requires Shipping",
    "Variant Taxable",
    "Variant Barcode",
    "Image Src",
    "Image Position",
    "Image Alt Text",
    "Gift Card",
    "SEO Title",
    "SEO Description",
    "Google Shopping / Google Product Category",
    "Google Shopping / Gender",
    "Google Shopping / Age Group",
    "Google Shopping / MPN",
    "Google Shopping / Condition",
    "Google Shopping / Custom Product",
    "Variant Image",
    "Variant Weight Unit",
    "Variant Tax Code",
    "Cost per item",
    "Status",
]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug or "producto"


def clean_html(value: str) -> str:
    text = value or ""
    if "<" in text and ">" in text:
        return text
    escaped = html.escape(text).replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [part.strip() for part in escaped.split("\n\n") if part.strip()]
    if paragraphs:
        return "".join(f"<p>{paragraph.replace(chr(10), '<br>')}</p>" for paragraph in paragraphs)
    return f"<p>{escaped}</p>" if escaped else ""


def normalize_price(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(".", "").replace(",", ".") if "," in raw else raw
    try:
        return f"{float(raw):.2f}"
    except ValueError:
        return ""


def normalize_int(value: str, default: int = 0) -> str:
    raw = (value or "").strip()
    if not raw:
        return str(default)
    try:
        return str(int(float(raw.replace(",", "."))))
    except ValueError:
        return str(default)


def grams_from_weight(value: str) -> str:
    return normalize_int(value, 0)


def split_images(value: str) -> list[str]:
    return [url.strip() for url in (value or "").split(",") if url.strip()]


def published_value(row: dict[str, str], status: str) -> str:
    if status == "draft":
        return "FALSE"
    return "TRUE" if (row.get("Publicado") or "").strip() == "1" else "FALSE"


def status_for(row: dict[str, str], price: str, images: list[str]) -> tuple[str, list[str]]:
    reasons = []
    if not price:
        reasons.append("sin precio")
    if not images:
        reasons.append("sin imagen")
    if reasons:
        return "draft", reasons
    return "active", reasons


def unique_handles(rows: list[dict[str, str]]) -> dict[str, str]:
    used = Counter()
    result = {}
    for row in rows:
        base = slugify(row.get("Nombre", ""))
        used[base] += 1
        handle = base if used[base] == 1 else f"{base}-{used[base]}"
        result[row["ID"]] = handle
    return result


def tags_for(row: dict[str, str]) -> str:
    tags = []
    for source in [
        row.get("Tags Shopify", ""),
        f"vendor-{slugify(row.get('Vendor Shopify', ''))}",
    ]:
        for tag in [item.strip() for item in source.split(",") if item.strip()]:
            if tag not in tags:
                tags.append(tag)
    return ", ".join(tags)


def main() -> None:
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True))

    handles = unique_handles(source_rows)
    output_rows = []
    status_reasons = Counter()
    products_by_status = Counter()
    image_rows = 0

    for row in source_rows:
        images = split_images(row.get("Imágenes", ""))
        price = normalize_price(row.get("Precio normal", ""))
        status, reasons = status_for(row, price, images)
        products_by_status[status] += 1
        for reason in reasons:
            status_reasons[reason] += 1

        handle = handles[row["ID"]]
        title = row.get("Nombre", "").strip()
        body_html = clean_html(row.get("Descripción", ""))
        seo_description = html.unescape(row.get("Meta: _yoast_wpseo_metadesc", "")).strip()
        barcode = (row.get("GTIN, UPC, EAN o ISBN") or "").strip()
        if not barcode:
            barcode = (row.get("SKU") or "").strip()

        base = {
            "Handle": handle,
            "Title": title,
            "Body (HTML)": body_html,
            "Vendor": row.get("Vendor Shopify", "").strip(),
            "Product Category": "",
            "Type": row.get("Product type Shopify", "").strip(),
            "Tags": tags_for(row),
            "Published": published_value(row, status),
            "Option1 Name": "Title",
            "Option1 Value": "Default Title",
            "Option2 Name": "",
            "Option2 Value": "",
            "Option3 Name": "",
            "Option3 Value": "",
            "Variant SKU": row.get("SKU", "").strip(),
            "Variant Grams": grams_from_weight(row.get("Peso (g)", "")),
            "Variant Inventory Tracker": "shopify",
            "Variant Inventory Qty": normalize_int(row.get("Inventario", ""), 0),
            "Variant Inventory Policy": "deny",
            "Variant Fulfillment Service": "manual",
            "Variant Price": price or "0.00",
            "Variant Compare At Price": "",
            "Variant Requires Shipping": "TRUE",
            "Variant Taxable": "TRUE" if (row.get("Estado del impuesto") or "").strip() == "taxable" else "FALSE",
            "Variant Barcode": barcode,
            "Image Src": images[0] if images else "",
            "Image Position": "1" if images else "",
            "Image Alt Text": title if images else "",
            "Gift Card": "FALSE",
            "SEO Title": title[:70],
            "SEO Description": seo_description[:320],
            "Google Shopping / Google Product Category": "",
            "Google Shopping / Gender": "",
            "Google Shopping / Age Group": "adult",
            "Google Shopping / MPN": row.get("SKU", "").strip(),
            "Google Shopping / Condition": "new",
            "Google Shopping / Custom Product": "FALSE",
            "Variant Image": images[0] if images else "",
            "Variant Weight Unit": "g",
            "Variant Tax Code": "",
            "Cost per item": "",
            "Status": status,
        }
        output_rows.append(base)

        for position, image in enumerate(images[1:], start=2):
            image_row = {column: "" for column in SHOPIFY_COLUMNS}
            image_row["Handle"] = handle
            image_row["Image Src"] = image
            image_row["Image Position"] = str(position)
            image_row["Image Alt Text"] = title
            output_rows.append(image_row)
            image_rows += 1

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=SHOPIFY_COLUMNS,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            lineterminator="\r\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(output_rows)

    with OUTPUT.open(encoding="utf-8-sig", newline="") as handle:
        reopened = list(csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True))

    report = {
        "input": str(INPUT),
        "output": str(OUTPUT),
        "source_products": len(source_rows),
        "csv_rows": len(reopened),
        "product_rows": len(source_rows),
        "additional_image_rows": image_rows,
        "columns": len(SHOPIFY_COLUMNS),
        "products_by_status": dict(products_by_status),
        "draft_reasons": dict(status_reasons),
        "unique_handles": len(set(handles.values())),
        "duplicate_handles": len(source_rows) - len(set(handles.values())),
        "products_without_price": status_reasons.get("sin precio", 0),
        "products_without_images": status_reasons.get("sin imagen", 0),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if len(reopened) != len(output_rows):
        raise SystemExit("Validation failed: reopened row count mismatch")
    if report["unique_handles"] != len(source_rows):
        raise SystemExit("Validation failed: product handles are not unique")


if __name__ == "__main__":
    main()
