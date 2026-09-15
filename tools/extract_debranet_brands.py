#!/usr/bin/env python3
"""Extract selected Debranet brands from downloaded product XML batches."""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path


def text(element: ET.Element, tag: str) -> str:
    return (element.findtext(tag) or "").strip()


def has_child_content(element: ET.Element, tag: str) -> bool:
    child = element.find(tag)
    return child is not None and any((value.text or "").strip() for value in child.iter())


def is_positive_decimal(value: str) -> bool:
    try:
        return Decimal(value.replace(",", ".")) > 0
    except (InvalidOperation, AttributeError):
        return False


def parse_weight_kg(value: str) -> Decimal | None:
    match = re.fullmatch(r"\s*([0-9]+(?:[.,][0-9]+)?)\s*(kg|g)\.?\s*", value, re.IGNORECASE)
    if not match:
        return None
    amount = Decimal(match.group(1).replace(",", "."))
    if amount <= 0:
        return None
    return amount if match.group(2).casefold() == "kg" else amount / Decimal("1000")


def language_counts(products: list[ET.Element], container: str, item: str) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for product in products:
        for value in product.findall(f"./{container}/{item}"):
            code = text(value, "language_code")
            if code:
                counts[code] += 1
    return dict(sorted(counts.items()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("brands", nargs="+", help="Brand names to extract")
    args = parser.parse_args()

    folder = args.folder.resolve()
    requested = {brand.casefold(): brand for brand in args.brands}

    brands_root = ET.parse(folder / "debranet-brands.xml").getroot()
    brand_by_id = {
        text(brand, "brand_id"): text(brand, "brand_name") for brand in brands_root
    }
    selected_ids = {
        brand_id: name
        for brand_id, name in brand_by_id.items()
        if name.casefold() in requested
    }
    missing_brands = sorted(set(requested) - {name.casefold() for name in selected_ids.values()})
    if missing_brands:
        raise SystemExit(f"Brands not found: {', '.join(missing_brands)}")

    source_files = sorted(folder.glob("debranet-products-[0-9]*.xml"))
    if not source_files:
        raise SystemExit("No Debranet product batches found")

    output_root = ET.Element("products")
    source_counts: dict[str, int] = {}
    all_ids: list[str] = []
    selected_products: list[ET.Element] = []

    for source_file in source_files:
        products = list(ET.parse(source_file).getroot())
        source_counts[source_file.name] = len(products)
        for product in products:
            all_ids.append(text(product, "product_id"))
            if text(product, "product_brandid") in selected_ids:
                selected_products.append(product)
                output_root.append(product)

    product_ids = [text(product, "product_id") for product in selected_products]
    product_codes = [text(product, "product_code") for product in selected_products]
    duplicate_ids = sorted(key for key, count in Counter(product_ids).items() if key and count > 1)
    duplicate_codes = sorted(key for key, count in Counter(product_codes).items() if key and count > 1)

    counts_by_brand = Counter(
        selected_ids[text(product, "product_brandid")] for product in selected_products
    )
    parsed_weights = [parse_weight_kg(text(product, "product_weight")) for product in selected_products]
    valid_weights = [weight for weight in parsed_weights if weight is not None]
    missing = {
        "product_id": sum(not text(product, "product_id") for product in selected_products),
        "product_code": sum(not text(product, "product_code") for product in selected_products),
        "ean": sum(not text(product, "product_ean") for product in selected_products),
        "weight": sum(weight is None for weight in parsed_weights),
        "stock": sum(not text(product, "product_stock") for product in selected_products),
        "price_eur": sum(not is_positive_decimal(text(product, "product_ownprice_EUR")) for product in selected_products),
        "names": sum(not has_child_content(product, "product_names") for product in selected_products),
        "descriptions": sum(not has_child_content(product, "product_descriptions") for product in selected_products),
        "pictures": sum(not has_child_content(product, "product_pics") for product in selected_products),
    }

    output_name = "debranet-products-mistress-lelo.xml"
    output_path = folder / output_name
    ET.indent(output_root, space="  ")
    ET.ElementTree(output_root).write(output_path, encoding="utf-8", xml_declaration=True)

    summary = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_files": source_counts,
        "source_rows": len(all_ids),
        "source_unique_product_ids": len(set(all_ids)),
        "source_duplicate_product_ids": len(all_ids) - len(set(all_ids)),
        "selected_brands": [
            {"brand_id": brand_id, "brand_name": name, "products": counts_by_brand[name]}
            for brand_id, name in sorted(selected_ids.items(), key=lambda item: item[1].casefold())
        ],
        "selected_products": len(selected_products),
        "duplicate_selected_product_ids": duplicate_ids,
        "duplicate_selected_product_codes": duplicate_codes,
        "missing_or_invalid_fields": missing,
        "weight_kg": {
            "valid_products": len(valid_weights),
            "minimum": str(min(valid_weights)) if valid_weights else None,
            "maximum": str(max(valid_weights)) if valid_weights else None,
        },
        "language_coverage": {
            "names": language_counts(selected_products, "product_names", "product_name"),
            "descriptions": language_counts(
                selected_products, "product_descriptions", "product_description"
            ),
        },
        "output_file": output_name,
    }
    summary_path = folder / "debranet-extraction-summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
