import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "datos" / "05-informes-validacion" / "estructura_proyecto_resumen.json"

EXPECTED_DIRECTORIES = [
    "datos/01-fuentes-originales",
    "datos/02-datos-intermedios",
    "datos/03-archivos-importacion-shopify",
    "datos/04-lotes-importacion",
    "datos/05-informes-validacion",
    "datos/06-registros-shopify",
    "datos/07-colecciones",
    "documentacion",
    "recursos-visuales",
    "tools",
    "output",
]

CRITICAL_FILES = [
    "datos/01-fuentes-originales/wc-product-export-29-6-2026-1782741544086.csv",
    "datos/02-datos-intermedios/wc-product-export-29-6-2026-marcas-mvp_limpio.csv",
    "datos/02-datos-intermedios/wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv",
    "datos/03-archivos-importacion-shopify/shopify_import_lovlory_mvp_productos_con_pesos.csv",
    "datos/07-colecciones/LovLory_estructura_colecciones_shopify_MVP_v1.xlsx",
    "documentacion/ESTADO.md",
    "documentacion/PLAN_IMPLEMENTACION_CONFIGURACION_SHOPIFY.md",
    "documentacion/PLAN_IMPLEMENTACION_CONFIGURACION_SHOPIFY.docx",
]

FORBIDDEN_ROOT_SUFFIXES = {".csv", ".xlsx", ".json", ".docx", ".png"}
LEGACY_PATH_MARKERS = ("E:/Projectes web", 'BASE / "wc-product', 'BASE / "shopify_import')


def main() -> None:
    errors: list[str] = []

    for relative_path in EXPECTED_DIRECTORIES:
        if not (ROOT / relative_path).is_dir():
            errors.append(f"Falta la carpeta: {relative_path}")

    for relative_path in CRITICAL_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Falta el archivo crítico: {relative_path}")

    loose_artifacts = sorted(
        path.name
        for path in ROOT.iterdir()
        if path.is_file() and path.suffix.lower() in FORBIDDEN_ROOT_SUFFIXES
    )
    if loose_artifacts:
        errors.append(f"Hay artefactos sueltos en la raíz: {', '.join(loose_artifacts)}")

    python_files = sorted((ROOT / "tools").glob("*.py"))
    syntax_checked = []
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            syntax_checked.append(path.name)
        except (SyntaxError, UnicodeDecodeError) as exc:
            errors.append(f"Error de sintaxis o codificación en {path.name}: {exc}")

    stale_references = []
    for path in [*python_files, *(ROOT / "tools").glob("*.mjs")]:
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in LEGACY_PATH_MARKERS):
            stale_references.append(path.name)
    if stale_references:
        errors.append(f"Quedan rutas antiguas en: {', '.join(sorted(stale_references))}")

    summary = {
        "status": "ok" if not errors else "error",
        "directories_checked": len(EXPECTED_DIRECTORIES),
        "critical_files_checked": len(CRITICAL_FILES),
        "python_files_syntax_checked": syntax_checked,
        "loose_root_artifacts": loose_artifacts,
        "errors": errors,
    }
    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
