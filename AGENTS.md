# Repository Guidelines

## Estructura del Proyecto y Organización
Este repositorio es un workspace de migración de catálogo de WooCommerce a Shopify para LovLory, no una aplicación web. Los artefactos de trabajo están organizados por fase dentro de `datos/`:

- `datos/01-fuentes-originales/`: exportaciones sin modificar y referencias de origen.
- `datos/02-datos-intermedios/`: CSV filtrados, limpios y enriquecidos.
- `datos/03-archivos-importacion-shopify/`: CSV preparados para Shopify.
- `datos/04-lotes-importacion/`: lotes operativos preparados o importados.
- `datos/05-informes-validacion/`: resúmenes JSON y comprobaciones reproducibles.
- `datos/06-registros-shopify/`: planes y registros de recursos creados en Shopify.
- `datos/07-colecciones/`: workbooks de arquitectura y colecciones.

Los scripts reutilizables están en `tools/`. Cubren filtrado de marcas, limpieza de columnas, enriquecimiento de taxonomía Shopify, generación de CSV final, extracción de payloads de prueba y verificación. La documentación de trabajo está en `documentacion/`, los recursos visuales en `recursos-visuales/` y los entregables generados en `output/`.

Los scripts calculan la raíz del repositorio desde su propia ubicación, por lo que deben funcionar igual al clonar el proyecto en otro PC.

## Flujo de Migración Planificado
El flujo canónico es: exportación WooCommerce completa, filtrado por marcas MVP (`ORGIE`, `SVAKOM`, `TENGA`, `MISTRESS`), limpieza de columnas, asignación de taxonomía Shopify, generación de CSV final con pesos y creación/importación por lotes.

No sobrescribas la categoría WooCommerce original sin dejar trazabilidad. Usa campos Shopify separados para colecciones, tipo de producto, tags, SEO, vendor, stock, peso e imágenes.

## Comandos de Trabajo
No hay pipeline de build. Ejecuta los scripts desde la raíz del repo clonado:

- `python tools\filter_wc_products_mvp_brands.py` - filtra las marcas MVP.
- `python tools\clean_wc_products_for_shopify_staging.py` - limpia columnas para staging.
- `python tools\enrich_wc_products_shopify_taxonomy.py` - añade taxonomía y tags Shopify.
- `python tools\build_shopify_import_csv.py` - genera el CSV final de importación.
- `python tools\fill_shopify_weights_from_description.py` - completa pesos desde descripciones cuando falten.
- `python tools\verify_wc_cleaned_mvp.py` - valida el CSV limpiado.

## Reglas de Importación Shopify
Usa los datos reales del CSV final. La descripción del producto debe salir de `Body (HTML)`/body, nunca inventarse. Mantén SEO title y SEO description cuando existan.

Las imágenes deben quedar alojadas en Shopify CDN. Tras cada creación o actualización, verifica que el media esté en `READY`; si una URL falla, documenta el producto y evita usar imágenes inventadas.

Importa en `DRAFT` productos sin precio, sin imagen o sin stock disponible. Para productos válidos, confirma stock, peso, SKU, vendor, tipo, tags y colecciones antes de considerarlos terminados.

## Estilo de Código y Datos
Los scripts Python deben ser pequeños, explícitos y basados en librería estándar cuando sea razonable. Usa `snake_case` para funciones, variables y archivos.

Respeta nombres de columnas esperados por los scripts, especialmente `SKU`, `Marcas`, `Imágenes`, `Precio normal`, `Inventario`, `Peso (g)`, `Vendor Shopify`, `Product type Shopify` y `Tags Shopify`.

## Verificación
Cada transformación debe dejar un JSON de resumen o una comprobación reproducible. Trata como bloqueantes: recuentos inesperados, marcas fuera del MVP, handles duplicados, SKUs vacíos, precios inválidos, pesos faltantes en productos físicos e imágenes no accesibles.

Para importaciones directas en Shopify, verifica después de cada lote: estado, inventario, peso, número de imágenes y estado de media.

## Seguridad de Datos
No reemplaces exportaciones fuente sin una razón clara. Prefiere generar un nuevo archivo, validarlo y conservar el resumen. Los archivos de lotes (`datos/04-lotes-importacion/shopify_import_lovlory_mvp_batch*.json`) sirven como registro operativo de qué se ha preparado/importado.

## Commits y PRs
El historial aún es mínimo, así que usa commits cortos e imperativos, por ejemplo `update shopify import guide` o `fix weight extraction`. En PRs, incluye archivos afectados, recuentos antes/después y cualquier incidencia de importación relevante.
