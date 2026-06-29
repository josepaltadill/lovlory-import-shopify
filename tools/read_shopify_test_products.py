import csv
import json
from pathlib import Path


BASE = Path(r"E:\Projectes web\Globals\sexshoplorena")
INPUT = BASE / "shopify_import_lovlory_mvp_test.csv"


def main() -> None:
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    images_by_handle = {}
    for row in rows:
        handle = row.get("Handle", "")
        image = row.get("Image Src", "")
        if image:
            images_by_handle.setdefault(handle, []).append(image)

    products = []
    for row in rows:
        if row.get("Title"):
            products.append(
                {
                    "handle": row.get("Handle", ""),
                    "title": row.get("Title", ""),
                    "descriptionHtml": row.get("Body (HTML)", ""),
                    "vendor": row.get("Vendor", ""),
                    "productType": row.get("Type", ""),
                    "tags": [tag.strip() for tag in row.get("Tags", "").split(",") if tag.strip()],
                    "sku": row.get("Variant SKU", ""),
                    "price": row.get("Variant Price", ""),
                    "inventoryQty": row.get("Variant Inventory Qty", ""),
                    "status": row.get("Status", ""),
                    "images": images_by_handle.get(row.get("Handle", ""), []),
                }
            )
    print(json.dumps(products, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
