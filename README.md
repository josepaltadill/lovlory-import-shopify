# LovLory — migración de WooCommerce a Shopify

Workspace de preparación, validación e importación del catálogo MVP de LovLory. No es una aplicación web: contiene exportaciones, transformaciones, lotes operativos, documentación y scripts reproducibles.

## Estructura del repositorio

```text
datos/
├── 01-fuentes-originales/              Exportaciones sin modificar y referencias de origen
├── 02-datos-intermedios/               CSV filtrados, limpios y enriquecidos
├── 03-archivos-importacion-shopify/    CSV preparados para importar en Shopify
├── 04-lotes-importacion/               Lotes preparados o ya utilizados
├── 05-informes-validacion/             Resúmenes JSON y comprobaciones reproducibles
├── 06-registros-shopify/               Planes y registros de recursos creados en Shopify
└── 07-colecciones/                      Workbooks de arquitectura de colecciones

documentacion/                           Estado, instrucciones, guías y planes operativos
recursos-visuales/                       Previsualizaciones y referencias visuales
tools/                                   Scripts reutilizables del flujo de migración
output/                                  Entregables generados
```

## Flujo principal

Ejecutar desde la raíz del repositorio:

```powershell
python tools\filter_wc_products_mvp_brands.py
python tools\clean_wc_products_for_shopify_staging.py
python tools\enrich_wc_products_shopify_taxonomy.py
python tools\build_shopify_import_csv.py
python tools\fill_shopify_weights_from_description.py
python tools\verify_wc_cleaned_mvp.py
```

Los scripts resuelven las rutas desde su propia ubicación, de modo que el proyecto puede clonarse en cualquier carpeta sin modificar rutas absolutas.

## Documentos principales

- `documentacion/ESTADO.md`: estado operativo y registro histórico de la migración.
- `documentacion/INSTRUCCIONES.md`: instrucciones funcionales y de colecciones.
- `documentacion/PLAN_IMPLEMENTACION_CONFIGURACION_SHOPIFY.md`: lista viva para configurar y lanzar la tienda.
- `documentacion/PLAN_IMPLEMENTACION_CONFIGURACION_SHOPIFY.docx`: versión Word compartible del plan.

## Regla de seguridad de datos

No sobrescribir los archivos de `datos/01-fuentes-originales/`. Cada transformación debe producir un archivo nuevo y, cuando corresponda, un resumen en `datos/05-informes-validacion/`.
