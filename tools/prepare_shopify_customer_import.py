import csv
import re
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "clientes" / "selected-lists-contacts.csv"
OUTPUT = BASE / "clientes" / "shopify_customers_import_subscribed.csv"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "lista-desconocida"


def main() -> None:
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    fieldnames = [
        "First Name",
        "Last Name",
        "Email",
        "Accepts Email Marketing",
        "Accepts SMS Marketing",
        "Tags",
        "Note",
    ]
    output_rows = []
    seen_emails = set()
    skipped_unsubscribed = 0
    skipped_duplicates = 0

    for row in rows:
        email = (row.get("Correo electrónico") or "").strip().lower()
        status = (row.get("Estado") or "").strip().lower()

        if status != "subscribed":
            skipped_unsubscribed += 1
            continue
        if email in seen_emails:
            skipped_duplicates += 1
            continue

        seen_emails.add(email)
        list_name = (row.get("Lista") or "").strip()
        acceptance_type = (row.get("Tipo de aceptación") or "").strip()
        created_at = (row.get("Creado el") or "").strip()

        output_rows.append(
            {
                "First Name": (row.get("Nombre") or "").strip(),
                "Last Name": (row.get("Apellidos") or "").strip(),
                "Email": email,
                "Accepts Email Marketing": "yes",
                "Accepts SMS Marketing": "no",
                "Tags": f"newsletter, wordpress-import, {slug(list_name)}",
                "Note": (
                    "Importado desde CSV original LovLory. "
                    f"Lista: {list_name}. "
                    f"Tipo aceptación: {acceptance_type}. "
                    f"Fecha origen: {created_at}."
                ),
            }
        )

    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"created={OUTPUT}")
    print(f"source_rows={len(rows)}")
    print(f"import_rows={len(output_rows)}")
    print(f"skipped_unsubscribed={skipped_unsubscribed}")
    print(f"skipped_duplicates={skipped_duplicates}")


if __name__ == "__main__":
    main()
