#!/usr/bin/env python3
"""Prepare normalized Shopify rows from a filtered Debranet XML catalog."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from decimal import Decimal
from pathlib import Path


HEADERS = [
    "Title",
    "URL handle",
    "Description",
    "Vendor",
    "Type",
    "Tags",
    "Published on online store",
    "Status",
    "SKU",
    "Barcode",
    "Option1 name",
    "Option1 value",
    "Price",
    "Cost per item",
    "Charge tax",
    "Inventory tracker",
    "Inventory quantity",
    "Continue selling when out of stock",
    "Weight value (grams)",
    "Weight unit for display",
    "Requires shipping",
    "Fulfillment service",
    "Product image URL",
    "Image position",
    "Image alt text",
    "Gift card",
]


def value(element: ET.Element, tag: str) -> str:
    return (element.findtext(tag) or "").strip()


def localized_value(product: ET.Element, container: str, item: str, field: str) -> str:
    for node in product.findall(f"./{container}/{item}"):
        if value(node, "language_code").casefold() == "en":
            return value(node, field)
    return ""


def eur_retail_price(product: ET.Element) -> str:
    for node in product.findall("./product_retail_prices/product_retail_price"):
        if value(node, "retail_price_currency").casefold() == "eur":
            return value(node, "retail_price_value")
    return ""


def grams(weight: str) -> str:
    match = re.fullmatch(r"\s*([0-9]+(?:[.,][0-9]+)?)\s*(kg|g)\.?\s*", weight, re.IGNORECASE)
    if not match:
        return ""
    amount = Decimal(match.group(1).replace(",", "."))
    result = amount * Decimal("1000") if match.group(2).casefold() == "kg" else amount
    return format(result.normalize(), "f")


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.casefold()).strip("-")


def normalized_integer(number: str) -> str:
    return str(int(Decimal(number)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_xml", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()

    products = list(ET.parse(args.input_xml).getroot())
    base_handles = [slugify(localized_value(p, "product_names", "product_name", "name")) for p in products]
    handle_counts = Counter(base_handles)
    rows: list[list[str]] = []
    product_records: list[dict[str, object]] = []

    for product, base_handle in zip(products, base_handles):
        title = localized_value(product, "product_names", "product_name", "name")
        description = localized_value(
            product, "product_descriptions", "product_description", "description"
        )
        sku = value(product, "product_code")
        brand_name = "MISTRESS" if value(product, "product_brandid") == "8949" else "LELO"
        handle = base_handle if handle_counts[base_handle] == 1 else f"{base_handle}-{slugify(sku)}"
        images = [
            value(image, "product_pic_path")
            for image in product.findall("./product_pics/product_pic")
            if value(image, "product_pic_path")
        ]
        product_records.append(
            {
                "handle": handle,
                "sku": sku,
                "brand": brand_name,
                "images": len(images),
                "stock": normalized_integer(value(product, "product_stock")),
            }
        )

        main = {header: "" for header in HEADERS}
        main.update(
            {
                "Title": title,
                "URL handle": handle,
                "Description": description,
                "Vendor": brand_name,
                "Tags": f"vendor-{brand_name.casefold()}",
                "Published on online store": "FALSE",
                "Status": "draft",
                "SKU": sku,
                "Barcode": value(product, "product_ean"),
                "Option1 name": "Title",
                "Option1 value": "Default Title",
                "Price": eur_retail_price(product),
                "Cost per item": value(product, "product_ownprice_EUR"),
                "Charge tax": "TRUE",
                "Inventory tracker": "shopify",
                "Inventory quantity": normalized_integer(value(product, "product_stock")),
                "Continue selling when out of stock": "DENY",
                "Weight value (grams)": grams(value(product, "product_weight")),
                "Weight unit for display": "kg",
                "Requires shipping": "TRUE",
                "Fulfillment service": "manual",
                "Product image URL": images[0] if images else "",
                "Image position": "1" if images else "",
                "Image alt text": title if images else "",
                "Gift card": "FALSE",
            }
        )
        rows.append([main[header] for header in HEADERS])

        for position, image_url in enumerate(images[1:], start=2):
            extra = {header: "" for header in HEADERS}
            extra.update(
                {
                    "URL handle": handle,
                    "Product image URL": image_url,
                    "Image position": str(position),
                    "Image alt text": title,
                }
            )
            rows.append([extra[header] for header in HEADERS])

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(
            {
                "headers": HEADERS,
                "rows": rows,
                "products": product_records,
                "source": args.input_xml.name,
                "language": "EN",
                "price_mapping": "EUR retail price",
                "cost_mapping": "EUR own price",
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
