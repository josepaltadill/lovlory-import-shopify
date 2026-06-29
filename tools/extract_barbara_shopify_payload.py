import csv
import json
from pathlib import Path


BASE = Path(r"E:\Projectes web\Globals\sexshoplorena")
CSV = BASE / "shopify_import_lovlory_mvp_productos.csv"
OUTPUT = BASE / "barbara_love_doll_expected_from_csv.json"


def main() -> None:
    with CSV.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    product = next(row for row in rows if row.get("Handle") == "barbara-love-doll" and row.get("Title"))
    images = [row["Image Src"] for row in rows if row.get("Handle") == "barbara-love-doll" and row.get("Image Src")]
    payload = {
        "product_id": "gid://shopify/Product/10949423235415",
        "title": product["Title"],
        "descriptionHtml": product["Body (HTML)"],
        "seo": {
            "title": product["SEO Title"],
            "description": product["SEO Description"],
        },
        "images": [{"url": url, "altText": product["Title"]} for url in images],
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
