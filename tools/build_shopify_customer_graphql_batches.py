import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "clientes" / "selected-lists-contacts.csv"
OUTPUT = BASE / "clientes" / "shopify_customer_import_batches.json"
SKIP_EMAILS = {"locashop.cat@gmail.com"}
BATCH_SIZE = 20


def parse_created_at(value: str) -> str | None:
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").isoformat() + "+02:00"


def opt_in_level(value: str) -> str:
    normalized = value.strip().lower()
    if normalized == "double opt-in":
        return "CONFIRMED_OPT_IN"
    if normalized == "single opt-in":
        return "SINGLE_OPT_IN"
    return "UNKNOWN"


def main() -> None:
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    seen = set(SKIP_EMAILS)
    inputs = []
    skipped_unsubscribed = 0
    skipped_duplicates = 0

    for row in rows:
        email = (row.get("Correo electrónico") or "").strip().lower()
        status = (row.get("Estado") or "").strip().lower()
        if status != "subscribed":
            skipped_unsubscribed += 1
            continue
        if email in seen:
            skipped_duplicates += 1
            continue
        seen.add(email)

        list_name = (row.get("Lista") or "").strip()
        acceptance_type = (row.get("Tipo de aceptación") or "").strip()
        created_at = (row.get("Creado el") or "").strip()

        inputs.append(
            {
                "email": email,
                "firstName": (row.get("Nombre") or "").strip(),
                "lastName": (row.get("Apellidos") or "").strip(),
                "tags": ["newsletter", "wordpress-import", "clientes-import-2026-08-27"],
                "note": (
                    "Importado desde CSV original LovLory. "
                    f"Lista: {list_name}. "
                    f"Tipo aceptación: {acceptance_type}. "
                    f"Fecha origen: {created_at}."
                ),
                "emailMarketingConsent": {
                    "marketingState": "SUBSCRIBED",
                    "marketingOptInLevel": opt_in_level(acceptance_type),
                    "consentUpdatedAt": parse_created_at(created_at),
                },
            }
        )

    batches = [inputs[index : index + BATCH_SIZE] for index in range(0, len(inputs), BATCH_SIZE)]
    graphql_batches = []
    for batch_index, batch in enumerate(batches):
        definitions = ", ".join(f"$input{index}: CustomerInput!" for index in range(len(batch)))
        fields = "\n".join(
            (
                f"  c{index}: customerCreate(input: $input{index}) "
                "{ userErrors { field message } customer { id email } }"
            )
            for index in range(len(batch))
        )
        graphql_batches.append(
            {
                "query": f"mutation ImportCustomersBatch{batch_index}({definitions}) {{\n{fields}\n}}",
                "variables": {f"input{index}": item for index, item in enumerate(batch)},
            }
        )
    payload = {
        "source_rows": len(rows),
        "prepared_inputs": len(inputs),
        "skipped_unsubscribed": skipped_unsubscribed,
        "skipped_duplicates_or_already_imported": skipped_duplicates,
        "batch_size": BATCH_SIZE,
        "batches": batches,
        "graphql_batches": graphql_batches,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {key: payload[key] for key in payload if key not in ("batches", "graphql_batches")}
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
