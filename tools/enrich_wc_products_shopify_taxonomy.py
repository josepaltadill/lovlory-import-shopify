import csv
import html
import json
import re
from collections import Counter
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp_limpio.csv"
OUTPUT = BASE / "wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv"
REPORT = BASE / "wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia_resumen.json"

NEW_COLUMNS = [
    "Vendor Shopify",
    "Colecciones comerciales Shopify",
    "Colección marca Shopify",
    "Product type Shopify",
    "Tags Shopify",
    "custom.publico",
    "custom.subtipo_cosmetica",
    "custom.uso",
    "custom.efecto",
    "custom.estilo_lovlory",
    "custom.nivel_iniciacion",
    "custom.ocasion",
    "Revisar manualmente",
    "Motivo revisión",
]


def split_categories(value: str) -> list[str]:
    return [category.strip() for category in (value or "").split(",") if category.strip()]


def clean_text(value: str) -> str:
    return html.unescape(value or "").lower()


def add_unique(items: list[str], *values: str) -> None:
    for value in values:
        if value and value not in items:
            items.append(value)


def has_any(text: str, words: list[str]) -> bool:
    return any(word in text for word in words)


def classify(row: dict[str, str]) -> dict[str, str]:
    brand = (row.get("Marcas") or "").strip().upper()
    categories = split_categories(row.get("Categorías", ""))
    cat_text = " | ".join(categories).lower()
    name = clean_text(row.get("Nombre", ""))
    desc = clean_text(row.get("Descripción", ""))
    combined = f"{name} {desc} {cat_text}"

    collections: list[str] = []
    tags: list[str] = []
    review_reasons: list[str] = []
    product_type = ""
    publico = ""
    subtipo_cosmetica = ""
    uso = ""
    efecto = ""
    estilo = ""
    nivel = ""
    ocasion = ""

    add_unique(tags, f"vendor-{brand.lower()}")
    add_unique(tags, "novedad" if "novedades" in cat_text else "")
    add_unique(tags, "showroom" if "showroom" in cat_text else "")

    if brand == "TENGA":
        add_unique(collections, "Juguetes Eróticos", "Para Él")
        product_type = "Masturbador masculino"
        publico = "Él"
        uso = "Masturbación masculina"
        estilo = "Bienestar"
        add_unique(tags, "publico-el", "tipo-masturbador", "juguetes-eroticos")
        if "masturbador sin vibración" in cat_text:
            add_unique(tags, "sin-vibracion")

    elif brand == "MISTRESS":
        add_unique(collections, "Juguetes Eróticos")
        product_type = "Muñeca realista"
        publico = "Él"
        uso = "Masturbación masculina"
        estilo = "Bienestar"
        nivel = "Avanzado"
        add_unique(tags, "publico-el", "tipo-muneca-realista", "juguetes-eroticos")
        if "muñec@s tamaño real" in cat_text:
            add_unique(tags, "tamano-real")
        review_reasons.append("Confirmar si las muñecas realistas deben tener colección propia o quedar solo dentro de Juguetes Eróticos/Para Él.")

    elif brand == "SVAKOM":
        add_unique(collections, "Juguetes Eróticos")
        product_type = "Juguete erótico"
        publico = "Unisex"
        estilo = "Premium"
        add_unique(tags, "juguetes-eroticos", "premium")
        if has_any(combined, ["punto g", "vibrador", "vibrating", "vibrator"]):
            add_unique(collections, "Vibradores y Succionadores")
            product_type = "Vibrador"
            publico = "Ella"
            uso = "Estimulación punto G"
            add_unique(tags, "publico-ella", "tipo-vibrador", "punto-g")
        elif has_any(combined, ["kegel", "suelo pélvico", "suelo pelvico"]):
            add_unique(collections, "Cosmética Íntima", "Para Ella", "Cuidado del suelo pélvico")
            product_type = "Ejercitador suelo pélvico"
            publico = "Ella"
            uso = "Suelo pélvico"
            subtipo_cosmetica = "Suelo pélvico"
            add_unique(tags, "publico-ella", "suelo-pelvico")
        else:
            review_reasons.append("SVAKOM sin subtipo claro por categoría/título; revisar si es vibrador, pareja, kegel u otro juguete.")

    elif brand == "ORGIE":
        add_unique(collections, "Cosmética Íntima")
        product_type = "Cosmética íntima"
        publico = "Parejas/Todes"
        estilo = "Bienestar"
        add_unique(tags, "cosmetica-intima", "publico-parejas-todes")
        if has_any(combined, ["lubricante", "lubricantes", "lubricación", "lubricacion"]):
            add_unique(collections, "Para Parejas / Todes", "Lubricantes")
            subtipo_cosmetica = "Lubricante"
            uso = "Lubricación"
            add_unique(tags, "subtipo-lubricante")
        elif has_any(combined, ["vibrador liquido", "vibrador líquido", "estimulante", "efecto calor", "efecto frío", "efecto frio"]):
            add_unique(collections, "Para Parejas / Todes")
            subtipo_cosmetica = "Gel con efecto"
            uso = "Estimulación sensorial"
            add_unique(tags, "subtipo-gel-efecto")
        elif has_any(combined, ["sexo oral", "oral", "sabor"]):
            add_unique(collections, "Para Parejas / Todes")
            subtipo_cosmetica = "Gel oral"
            uso = "Sexo oral"
            add_unique(tags, "subtipo-gel-oral")
        else:
            add_unique(collections, "Para Parejas / Todes")
            review_reasons.append("ORGIE sin subtipo cosmético claro; revisar si es lubricante, gel con efecto, oral, masaje u otro.")

        if has_any(combined, ["calor", "hot", "warming"]):
            efecto = "Calor"
            add_unique(tags, "efecto-calor")
        elif has_any(combined, ["frío", "frio", "ice", "cool"]):
            efecto = "Frío"
            add_unique(tags, "efecto-frio")

    else:
        review_reasons.append("Marca fuera de reglas MVP.")

    if not collections:
        review_reasons.append("Sin colección comercial asignada.")
    if "sin categorizar" in cat_text:
        review_reasons.append("Categoría original Sin categorizar.")
    if not row.get("Precio normal", "").strip():
        review_reasons.append("Sin precio normal.")
    if not row.get("Imágenes", "").strip():
        review_reasons.append("Sin imágenes.")

    return {
        "Vendor Shopify": brand,
        "Colecciones comerciales Shopify": ", ".join(collections),
        "Colección marca Shopify": brand,
        "Product type Shopify": product_type,
        "Tags Shopify": ", ".join(tags),
        "custom.publico": publico,
        "custom.subtipo_cosmetica": subtipo_cosmetica,
        "custom.uso": uso,
        "custom.efecto": efecto,
        "custom.estilo_lovlory": estilo,
        "custom.nivel_iniciacion": nivel,
        "custom.ocasion": ocasion,
        "Revisar manualmente": "Sí" if review_reasons else "No",
        "Motivo revisión": " | ".join(review_reasons),
    }


def main() -> None:
    with INPUT.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=",", quotechar='"', doublequote=True)
        rows = list(reader)
        fields = reader.fieldnames or []

    output_fields = fields + NEW_COLUMNS
    enriched = []
    for row in rows:
        new_row = dict(row)
        new_row.update(classify(row))
        enriched.append(new_row)

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=output_fields,
            delimiter=",",
            quotechar='"',
            doublequote=True,
            lineterminator="\r\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(enriched)

    collection_counter = Counter()
    tag_counter = Counter()
    review_counter = Counter()
    for row in enriched:
        for collection in [item.strip() for item in row["Colecciones comerciales Shopify"].split(",") if item.strip()]:
            collection_counter[collection] += 1
        for tag in [item.strip() for item in row["Tags Shopify"].split(",") if item.strip()]:
            tag_counter[tag] += 1
        if row["Revisar manualmente"] == "Sí":
            review_counter[row["Motivo revisión"]] += 1

    report = {
        "input": str(INPUT),
        "output": str(OUTPUT),
        "rows": len(enriched),
        "columns": len(output_fields),
        "new_columns": NEW_COLUMNS,
        "by_vendor": dict(Counter(row["Vendor Shopify"] for row in enriched)),
        "by_collection": dict(collection_counter),
        "by_product_type": dict(Counter(row["Product type Shopify"] for row in enriched)),
        "manual_review_rows": sum(1 for row in enriched if row["Revisar manualmente"] == "Sí"),
        "manual_review_reasons": dict(review_counter),
        "top_tags": dict(tag_counter.most_common(50)),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
