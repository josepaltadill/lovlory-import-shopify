# Estado de la Migración LovLory a Shopify

## Resumen de la sesión
Se está migrando el catálogo de WooCommerce a Shopify para LovLory. La estrategia acordada es no arrastrar directamente las categorías antiguas de WooCommerce, sino usarlas como referencia para generar una taxonomía limpia en Shopify: colecciones, vendor/marca, product type, tags y campos SEO.

Las marcas MVP de trabajo son:

- `ORGIE`
- `SVAKOM`
- `TENGA`
- `MISTRESS`

Se decidió crear colecciones principales y colecciones de marca, pero no ponerlas aún en menú. Las colecciones pueden quedar vacías temporalmente sin problema. Las colecciones de marca se gestionan como colecciones Shopify, mientras que la marca del producto se guarda en `Vendor`.

También se acordó:

- Mantener la categoría WooCommerce como referencia, no como destino final.
- Usar `Body (HTML)`/body del CSV como descripción real del producto.
- No inventar descripciones ni imágenes.
- Importar en `DRAFT` productos sin precio, sin imagen o sin stock.
- Cargar imágenes en Shopify CDN, no dejarlas referenciadas desde WordPress.
- Verificar tras cada importación: stock, peso, SKU, estado, SEO e imágenes en `READY`.

## Archivos clave
El archivo principal de trabajo para productos preparados es:

- `shopify_import_lovlory_mvp_productos_con_pesos.csv`

Este CSV es el que contiene los productos limpios, filtrados por marcas MVP, con taxonomía Shopify y pesos completados cuando ha sido posible.

Otros archivos útiles:

- `wc-product-export-29-6-2026-1782741544086.csv`: exportación completa original de WooCommerce.
- `wc-product-export-29-6-2026-marcas-mvp_shopify_taxonomia.csv`: CSV intermedio con taxonomía Shopify.
- `shopify_import_lovlory_mvp_batch3.json`: lote usado para TENGA UNI/3D y Scarlett.
- `shopify_import_lovlory_mvp_batch4.json`: lote usado para Kevin, Daniel, Sebastian, Aurora y productos ORGIE.
- `shopify_import_lovlory_mvp_pilot10.json`, `shopify_import_lovlory_mvp_pilot10_selected.json`, `shopify_import_lovlory_mvp_pilot_next8.json`: lotes piloto usados durante la importación inicial.
- `AGENTS.md`: guía actualizada del repositorio y flujo de trabajo.

Los scripts de `tools/` se actualizaron para ser portables entre PCs. Ahora calculan la raíz del repo con:

```python
BASE = Path(__file__).resolve().parents[1]
```

## Correcciones realizadas
Se detectó un problema inicial en Shopify con el producto `Barbara Love Doll`: descripción inventada, solo 5 imágenes, sin stock/peso correctos y sin usar correctamente el body del CSV.

Se corrigió la estrategia de importación:

- Usar el body real del CSV.
- Cargar todas las imágenes disponibles.
- Añadir peso en envío.
- Activar seguimiento de inventario.
- Cargar SEO title y SEO description.
- Confirmar que las imágenes quedan alojadas en Shopify CDN.

`Barbara Love Doll` quedó corregida como producto de referencia.

## Productos ya importados o actualizados
Productos de muestra/existentes actualizados:

- `Barbara Love Doll` (`MSTRS00053`) - corregido, stock 3, peso 33 kg, 14 imágenes.
- `TENGA CRYSTA MASTURBADOR MASCULINO BALL` (`D-226949`)
- `Acqua Crocante Monoi` (`1451546`)
- `ALEX NEO 2` (`25338743`)
- `ACRYLIC DISPLAY` (`25300001`)

Productos importados después:

- `TENGA - FLEX MASTUBADOR MASCULINO BLANCO` (`D-216577`)
- `TENGA - CRYSTA MASTURBADOR MASCULINO BLOCK` (`D-227353`)
- `TENGA - CLICK BALL MASTURBADOR POCKET` (`D-230821`)
- `TENGA - CRYSTAL MIST MASTURBADOR POCKET` (`D-230824`)
- `TENGA - SPARK BEARDS MASTURBADOR POCKET` (`D-230825`)
- `TENGA - LOCION LUBRICANTE LIGHT BASE AGUA` (`D-241187`)
- `Nora Love Doll` (`MSTRS00009`)
- `Busty Lady Half Body Sex Doll` (`MSTRS00013`)
- `Zoey Love Doll` (`MSTRS00003`)
- `Isabella Love Doll` (`MSTRS00041`)
- `TENGA - MASTURBADOR GEO AQUA` (`D-226945`)
- `TENGA - MASTURBATOR GEO GLACIER` (`D-226947`)
- `TENGA - FLIP 0 ZERO ELECTRONIC VIBRATION` (`D-226986`)
- `TENGA - FLIP 0 ZERO ROJO CON CALENTADOR` (`D-228897`) - una URL de imagen falló; se dejaron solo imágenes válidas.
- `TENGA - AERO SILVER RING ANILLA PLATEADA` (`D-228898`)
- `TENGA - AERO COBALT RING ANILLA AZUL COBALTO` (`D-228899`)
- `TENGA - FLEX FIZZY GREEN MASTURBADOR` (`D-232974`)
- `TENGA - UNI EMERALD MASTURBADOR DEDAL` (`D-238092`)
- `TENGA - UNI DIAMOND MASTURBADOR DEDAL` (`D-238093`)
- `TENGA - UNI TOPAZ MASTURBADOR DEDAL` (`D-238094`)
- `TENGA - UNI AMETHYST MASTURBADOR DEDAL` (`D-238095`)
- `TENGA - UNI VARIETY MASTURBADOR DEDAL PACK 4 UDS` (`D-238096`)
- `TENGA - 3D MODULE SCULPTED ECSTASY` (`TNH-002`)
- `TENGA - 3D ZEN SCULPTED ECSTASY` (`TNH-003`)
- `TENGA - 3D POLYGON SCULPTED ECSTASY` (`TNH-004`)
- `Scarlett Love Doll` (`MSTRS00001`)
- `Acqua Crocante Sakura` (`1451553`)
- `ACQUA CROCCANTE PASSION FRUIT` (`1417007`)
- `Kevin Love Doll` (`MSTRS00007`)
- `Daniel Love Doll` (`MSTRS00002`)
- `Sebastian Love Doll` (`MSTRS00056`)
- `Aurora Love Doll` (`MSTRS00005`)
- `Muñeca sexual para el autocontrol masculino` (`MSTRS00012`)
- `Emma Half Body Sex Doll` (`MSTRS00011`)
- `Love Doll Roxanne` (`MSTRS00052`)
- `Natalie Love Doll` (`MSTRS00054`)
- `Suzanne Love Doll` (`MSTRS00080`)
- `Carmen Love Doll` (`MSTRS00084`)
- `Acqua Crocante Strawberry` (`1421371`) - en `DRAFT` por peso no confirmado en el CSV final.
- `ALL-NATURAL ACQUA Water-based Intimate Gel` (`1417274`) - en `DRAFT` por peso no confirmado en el CSV final.
- `ALL-NATURAL STRAWBERRY Kissable Water-based Intimate Gel` (`1417304`)
- `ALL-NATURAL ULTRA SLIDEWater-based Intimate Gel` (`1417298`)
- `DUAL VIBE! LEMON GIN & TONIC KISSABLE LIQUID VIBRATOR` (`1417557`)
- `DUAL VIBE! PIN? COLADA KISSABLE LIQUID VIBRATOR` (`1417311`) - en `DRAFT` por peso no confirmado en el CSV final.
- `DUAL VIBE! SEX ON THE BEACH KISSABLE LIQUID VIBRATOR` (`1417328`) - en `DRAFT` por peso no confirmado en el CSV final.
- `DUAL VIBE! STRAWBERRY GIN & TONIC KISSABLE LIQUID VIBRATOR` (`1417540`)
- `GLOW Shimmer Body Cream` (`1417243`)
- `GLOW Shimmering Body Oil` (`1417236`)
- `Greek Kiss - 50 Ml` (`1421409`) - en `DRAFT` por stock 0 y peso no confirmado en el CSV final.
- `Hemp! - Intense Orgasm - 15 Ml` (`1421393`) - en `DRAFT` por stock 0 y peso no confirmado en el CSV final.
- `HUMAN LUBE Water-based Intimate Gel` (`1417250`) - en `DRAFT` por stock 0.
- `Intimus White Intimate Whitening And Stimulating` (`1421166`) - en `DRAFT` por peso no confirmado en el CSV final.
- `SEMEN LUBE Water-based Intimate Gel` (`1417267`) - importado, stock 50, peso 180 g.
- `SENSFEEL FOR MAN 10 ML` (`1451959`) - importado, stock 14, peso 25 g.
- `SENSFEEL FOR MAN PHEROMOME PERFUME` (`1451744`) - importado, stock 9, en `DRAFT` por peso no confirmado.
- `SENSFEEL FOR WOMAN 10 ML` (`1451942`) - importado, stock 23, peso 25 g.
- `SENSFEEL FOR WOMAN PHEROMOME PERFUME` (`1451751`) - importado, stock 17, en `DRAFT` por peso no confirmado.
- `SENSFEEL SEDUCTION ELIXIR 10 in 1 MAN 100 ML` (`1451829`) - importado, stock 19, peso 130 g.
- `SENSFEEL SEDUCTION ELIXIR 10 in 1 WOMAN 100 ML` (`1451812`) - importado, stock 10, peso 130 g.
- `Sexy Therapy Afrodisiac` (`1421036`) - importado, stock 4, en `DRAFT` por peso no confirmado.
- `Sexy Therapy Amor` (`1421043`) - importado, stock 14, en `DRAFT` por peso no confirmado.
- `SEXY THERAPY SENSUAL MASSAGE OILS 3 x 30ml Set Mini Size Collection` (`1417137`) - importado, stock 21, en `DRAFT` por peso no confirmado.
- `TANTRIC SENSUAL MASSAGE OILS 3 x 30ml Set Mini Size Collection` (`1417090`) - importado, stock 9, en `DRAFT` por peso no confirmado.
- `THE PLAY SET` (`1451904`) - importado, stock 0, en `DRAFT` por stock 0 y peso no confirmado.
- `Time Lag - 25 ml` (`1421478`) - importado, stock 0, en `DRAFT` por stock 0 y peso no confirmado.
- `TIME LAG 2 DELAY SPRAY Next Generation` (`1417052`) - importado, stock 10, peso 21 g.
- `Touro XXXL` (`1421638`) - importado, stock 22, peso 30 g.
- `VOL+ UP 50 ML` (`1451928`) - importado, stock 10, peso 95 g.
- `Wow! Blowjob Spray` (`1421364`) - importado, stock 0, en `DRAFT` por stock 0 y peso no confirmado.
- `WOW! STRAWBERRY ICE 10 ML` (`1451935`) - importado, stock 13, peso 20 g.
- `Xtra Hardpower Gel For Him` (`1421180`) - importado, stock 10, en `DRAFT` por peso no confirmado.
- `Xtra Time - Delay Gel` (`1421234`) - importado, stock 17, en `DRAFT` por peso no confirmado.
- `ALEX NEO2 SLEEVE` (`25338755`) - siguiente SKU pendiente en el CSV final.
- `ALEX NEO2 SLEEVE` (`25338755`) - importado, stock 48, peso 225 g.
- `AMY 2 LIGHT PURPLE` (`25338753`) - importado, stock 22, peso 120 g.
- `AMY 2 VIOLET` (`25338748`) - importado, stock 18, peso 120 g.
- `AMY PALE PINK SVAKOM` (`25325050`) - importado, stock 18, peso 90 g.
- `Angel Plum Red` (`25337941`) - importado, stock 2, peso 146 g.
- `Anya Plum Red` (`25337841`) - importado, stock 0, en `DRAFT` por stock 0.
- `AVA NEO` (`25338752`) - importado, stock 0, en `DRAFT` por stock 0.
- `AVERY LILAC` (`25338747`) - importado, stock 18, peso 185 g.
- `Avery Strawberry Pink` (`25338768`) - importado, stock 14, peso 183 g.
- `AYLIN DARK BLUE` (`25338746`) - importado, stock 4, peso 180 g.
- `BENEDICT BLACK` (`25338734`) - importado, stock 23, peso 70 g.
- `BETTY TESTER` (`25335600`) - importado, stock 3, en `DRAFT` por precio 0 e imagen ausente.
- `CHIKA TURQUOISE GREY` (`25338756`) - importado, stock 14, en `DRAFT` por peso no confirmado.
- `CICI 2 PASTEL LILIAC` (`25338760`) - importado, stock 0, en `DRAFT` por stock 0.
- `Cici 2+` (`25338769`) - importado, stock 17, peso 72 g.
- `CICI VIOLET` (`25337020`) - importado, stock 0, en `DRAFT` por stock 0.
- `EDENY` (`25338721`) - importado, stock 18, peso 43 g.
- `Ella Neo` (`25338716`) - importado, stock 33, en `DRAFT` por peso no confirmado.
- `ELVA PLUM RED` (`25336441`) - importado, stock 0, en `DRAFT` por stock 0.
- `ELVA VIOLET` (`25336420`) - importado, stock 0, en `DRAFT` por stock 0.

## Último punto exacto de la importación
En el último intento se completó un lote de 10 productos:

- `DUAL VIBE! LEMON GIN & TONIC KISSABLE LIQUID VIBRATOR` (`1417557`)
- `DUAL VIBE! PIN? COLADA KISSABLE LIQUID VIBRATOR` (`1417311`)
- `DUAL VIBE! SEX ON THE BEACH KISSABLE LIQUID VIBRATOR` (`1417328`)
- `DUAL VIBE! STRAWBERRY GIN & TONIC KISSABLE LIQUID VIBRATOR` (`1417540`)
- `GLOW Shimmer Body Cream` (`1417243`)
- `GLOW Shimmering Body Oil` (`1417236`)
- `Greek Kiss - 50 Ml` (`1421409`)
- `Hemp! - Intense Orgasm - 15 Ml` (`1421393`)
- `HUMAN LUBE Water-based Intimate Gel` (`1417250`)
- `Intimus White Intimate Whitening And Stimulating` (`1421166`)

Ambos se sacaron del archivo:

- `shopify_import_lovlory_mvp_productos_con_pesos.csv`
- `shopify_import_lovlory_mvp_batch8.json`

Detalles:

- `DUAL VIBE! LEMON GIN & TONIC KISSABLE LIQUID VIBRATOR`
  - SKU: `1417557`
  - Shopify ID: `gid://shopify/Product/10950276219223`
  - Estado: `ACTIVE`
  - Stock: `10`
  - Peso: `32 g` tomado del CSV final.
  - Imágenes: 1, verificada en `READY`.

- `DUAL VIBE! PIN? COLADA KISSABLE LIQUID VIBRATOR`
  - SKU: `1417311`
  - Shopify ID: `gid://shopify/Product/10950276612439`
  - Estado: `DRAFT`
  - Stock: `20`
  - Peso: `0 g` porque el CSV final no trae peso verificable.
  - Imágenes: 1, verificada en `READY`.

- `DUAL VIBE! SEX ON THE BEACH KISSABLE LIQUID VIBRATOR`
  - SKU: `1417328`
  - Shopify ID: `gid://shopify/Product/10950277169495`
  - Estado: `DRAFT`
  - Stock: `46`
  - Peso: `0 g` porque el CSV final no trae peso verificable.
  - Imágenes: 1, verificada en `READY`.

- `DUAL VIBE! STRAWBERRY GIN & TONIC KISSABLE LIQUID VIBRATOR`
  - SKU: `1417540`
  - Shopify ID: `gid://shopify/Product/10950278447447`
  - Estado: `ACTIVE`
  - Stock: `1`
  - Peso: `32 g` tomado del CSV final.
  - Imágenes: 1, verificada en `READY`.

- `GLOW Shimmer Body Cream`
  - SKU: `1417243`
  - Shopify ID: `gid://shopify/Product/10950279168343`
  - Estado: `ACTIVE`
  - Stock: `8`
  - Peso: `315 g` tomado del CSV final.
  - Imágenes: 1, verificada en `READY`.

- `GLOW Shimmering Body Oil`
  - SKU: `1417236`
  - Shopify ID: `gid://shopify/Product/10950279790935`
  - Estado: `ACTIVE`
  - Stock: `31`
  - Peso: `125 g` tomado del CSV final.
  - Imágenes: 1, verificada en `READY`.

- `Greek Kiss - 50 Ml`
  - SKU: `1421409`
  - Shopify ID: `gid://shopify/Product/10950280937815`
  - Estado: `DRAFT`
  - Stock: `0`
  - Peso: `0 g` porque el CSV final no trae peso verificable.
  - Imágenes: 1, verificada en `READY`.

- `Hemp! - Intense Orgasm - 15 Ml`
  - SKU: `1421393`
  - Shopify ID: `gid://shopify/Product/10950281265495`
  - Estado: `DRAFT`
  - Stock: `0`
  - Peso: `0 g` porque el CSV final no trae peso verificable.
  - Imágenes: 1, verificada en `READY`.

- `HUMAN LUBE Water-based Intimate Gel`
  - SKU: `1417250`
  - Shopify ID: `gid://shopify/Product/10950281953623`
  - Estado: `DRAFT`
  - Stock: `0`
  - Peso: `190 g` tomado del CSV final.
  - Imágenes: 1, verificada en `READY`.

- `Intimus White Intimate Whitening And Stimulating`
  - SKU: `1421166`
  - Shopify ID: `gid://shopify/Product/10950282477911`
  - Estado: `DRAFT`
  - Stock: `16`
  - Peso: `0 g` porque el CSV final no trae peso verificable.
  - Imágenes: 1, verificada en `READY`.

Quedamos justo después de importar y verificar este lote de 10 productos. Para continuar en una nueva sesión, buscar el siguiente producto pendiente en `shopify_import_lovlory_mvp_productos_con_pesos.csv`, comprobando antes en Shopify por SKU para evitar duplicados.

El siguiente SKU pendiente en el orden del CSV final es:

- `25338755` - `ALEX NEO2 SLEEVE`
- `25338734` - `BENEDICT BLACK`
- `25338765` - `Emma Neo 2`

## Reglas para continuar
Antes de importar un producto nuevo:

1. Buscarlo por `sku:<SKU>` en Shopify.
2. Si ya existe, no duplicarlo.
3. Si no existe, crear usando los datos reales del CSV.
4. Usar `DRAFT` cuando falte precio, imagen o stock.
5. Verificar después de crear:
   - `status`
   - `totalInventory`
   - `tracksInventory`
   - peso del inventory item
   - número de imágenes
   - media `READY`
   - SEO title/description

Para seguir, conviene construir el siguiente lote desde el CSV final y saltar todos los SKUs listados arriba.

## Ultima tanda importada

Lote de 10 productos importado y verificado:

- `Jordan` - SKU `25338767` - `gid://shopify/Product/10950547997015` - `ACTIVE` - stock `8` - peso `83 g`
- `JUDY TESTER` - SKU `25337100` - `gid://shopify/Product/10950548554071` - `DRAFT` - stock `3` - peso `0 g`
- `Mini Emma Neo` - SKU `25338766` - `gid://shopify/Product/10950548652375` - `ACTIVE` - stock `21` - peso `130 g`
- `MORA NEO PEACH PINK` - SKU `25338758` - `gid://shopify/Product/10950548685143` - `DRAFT` - stock `25` - peso `0 g`
- `NOVA PLUM RED` - SKU `25335941` - `gid://shopify/Product/10950548816215` - `DRAFT` - stock `0` - peso `0 g`
- `NOVA VIOLET` - SKU `25335920` - `gid://shopify/Product/10950548881751` - `DRAFT` - stock `26` - peso `0 g`
- `Nymph Pink` - SKU `25338250` - `gid://shopify/Product/10950552322391` - `ACTIVE` - stock `31` - peso `124 g`
- `PHOENIX NEO 2` - SKU `25338745` - `gid://shopify/Product/10950552650071` - `ACTIVE` - stock `27` - peso `90 g`
- `PHOENIX NEO 2 PASTEL LILIAC` - SKU `25338762` - `gid://shopify/Product/10950552715607` - `ACTIVE` - stock `25` - peso `90 g`
- `PULSE GALAXIE BLACK` - SKU `25338750` - `gid://shopify/Product/10950552748375` - `ACTIVE` - stock `15` - peso `160 g`

Siguiente SKU pendiente en el CSV final:

- `25338751` - `PULSE GALAXIE LILIAC`

## Nueva tanda importada

Se ha continuado la importación con un lote de 10 productos sacados de `shopify_import_lovlory_mvp_productos_con_pesos.csv`.

Los dos primeros ya existían en Shopify y se han corregido a `DRAFT` porque tienen stock 0:

- `Audrey Love Doll` (`MSTRS00006`) - `DRAFT`
- `Emily Love Doll` (`MSTRS00110`) - `DRAFT`

Después se han creado estos 8 productos nuevos, todos con sus imágenes alojadas en Shopify CDN:

- `Lips Massage Kit  Cotton Candy` (`1421333`) - `ACTIVE`
- `Lips Massage Kit  Strawberry` (`1421326`) - `ACTIVE`
- `Lips Massage Kit Apple` (`1421319`) - `ACTIVE`
- `Lube Tube Anal Confort` (`1421142`) - `ACTIVE`
- `Lube Tube Anal Sensitive` (`1421159`) - `ACTIVE`
- `Lube Tube Cannabis - 100ml` (`1421485`) - `ACTIVE`
- `Lube Tube Chocolate` (`1421128`) - `ACTIVE`
- `LUBE TUBE COCKTAIL CAIPIRINHA 100ml` (`1417144`) - `ACTIVE`

Con este lote, quedan **82 productos pendientes** en el CSV final.

Siguiente SKU pendiente en el orden del CSV:

- `1417182` - `LUBE TUBE COCKTAIL CAIPIRINHA 50ml`

## Nueva tanda importada

Se ha continuado la importación con otro lote de 10 productos de `ORGIE`, todos creados a partir de `shopify_import_lovlory_mvp_productos_con_pesos.csv` y con imágenes subidas a Shopify CDN.

Productos importados:

- `LUBE TUBE COCKTAIL CAIPIRINHA 50ml` (`1417182`) - `ACTIVE`
- `LUBE TUBE COCKTAIL PI?A COLADA 100ml` (`1417168`) - `ACTIVE`
- `LUBE TUBE COCKTAIL PI?A COLADA 50ml` (`1417199`) - `ACTIVE`
- `LUBE TUBE COCKTAIL SEX ON THE BEACH 100ml` (`1417175`) - `ACTIVE`
- `LUBE TUBE COCKTAIL SEX ON THE BEACH 50ml` (`1417205`) - `ACTIVE`
- `LUBE TUBE COCKTAIL STRAWBERRY MOJITO 100ml` (`1417151`) - `ACTIVE`
- `LUBE TUBE COCKTAIL STRAWBERRY MOJITO 50ml` (`1417212`) - `ACTIVE`
- `Lube Tube Cool` (`1421074`) - `ACTIVE`
- `Lube Tube Cotton Candy` (`1421135`) - `ACTIVE`
- `Lube Tube Hot` (`1421067`) - `ACTIVE`

Con este lote quedan **72 productos pendientes** en el CSV final.

Siguiente SKU pendiente en el orden del CSV:

- `1421081` - `Lube Tube Nature`

## Nueva tanda importada

Se ha continuado la importación con otro lote de 10 productos de `ORGIE` a partir de `shopify_import_lovlory_mvp_productos_con_pesos.csv`.

En este lote había 2 SKUs que ya existían en Shopify:

- `Noriplay - Nuru Massage Gel` (`1421289`) - ya existía en Shopify con stock 35
- `Noriplay - Energizing Nuru Massage Gel` (`1421296`) - se ha dejado en `DRAFT` porque el CSV final lo marca sin stock

Los otros 8 productos se han creado o confirmado con imágenes en Shopify CDN:

- `Lube Tube Nature` (`1421081`) - `ACTIVE`
- `Lube Tube Strawberry` (`1421104`) - `ACTIVE`
- `LUBE TUBE VIBE PI?A COLADA  100ml` (`1417533`) - `ACTIVE`
- `LUBE TUBE VIBE SEX ON THE BEACH  100ml` (`1417526`) - `ACTIVE`
- `Lube Tube Xtra Lubrication` (`1421098`) - `ACTIVE`
- `Orgasm Drops Clitoral Arousal` (`1421357`) - `ACTIVE`
- `ORGASM DROPS INTENSE` (`1451966`) - `DRAFT`
- `Orgasm Drops Kissable - 30 ml` (`1421416`) - `ACTIVE`

Con este lote quedan **62 productos pendientes** en el CSV final.

Siguiente SKU pendiente en el orden del CSV:

- `1451652` - `ORGASM DROPS VIBE!`

## Nueva tanda importada

Se ha continuado la importación con otro lote de 10 productos de `ORGIE` desde `shopify_import_lovlory_mvp_productos_con_pesos.csv`.

En este bloque ya existían en Shopify y no ha hecho falta recrearlos:

- `Pearls Lust Massage` (`1421241`)
- `Sexy Therapy The Secret` (`1421050`)
- `Sexy Vibe!  Intense Orgasm - Liquid Vibrator` (`1421227`)
- `Sexy Vibe! - Eletric Fellatio Vibrating Gloss` (`1421340`)
- `Sexy Vibe! - Liquid Vibrator` (`1421197`)

Los 5 productos nuevos que sí se han creado son:

- `ORGASM DROPS VIBE!` (`1451652`) - `ACTIVE`
- `Orgie Bio Aloe Vera Intimate Gel 100ml Pump` (`1421539`) - `ACTIVE`
- `Orgie Bio Chamomile Intimate Gel 100ml Pump` (`1421522`) - `ACTIVE`
- `Orgie Bio Grapefruit Organic Oil 100ml Disk Top` (`1421508`) - `ACTIVE`
- `Orgie Bio Rosemary Organic Oil 100ml Disk Top` (`1421515`) - `ACTIVE`

Con este lote quedan **57 productos pendientes** en el CSV final.

Siguiente SKU pendiente en el orden del CSV:

- `1421241` - `Pearls Lust Massage`

## Nueva tanda importada

Se ha continuado la importación con un lote nuevo de 10 productos de `SVAKOM` desde `shopify_import_lovlory_mvp_productos_con_pesos.csv`.

Productos creados:

- `PULSE LITE NEO MINT` (`25338742`) - `ACTIVE`
- `PULSE LITE NEO PINK` (`25338741`) - `ACTIVE`
- `PULSE LITE NEO PURPLE` (`25338740`) - `ACTIVE`
- `PULSE PURE PALE PINK` (`25338738`) - `ACTIVE`
- `PULSE UNION VIOLET` (`25338737`) - `ACTIVE`
- `ROBIN SLEEVE` (`25338733`) - `ACTIVE`
- `ROBIN WHITE` (`25338732`) - `ACTIVE`
- `Sam Neo` (`25338722`) - `ACTIVE`
- `SAM NEO 2` (`25338764`) - `DRAFT`
- `SAM NEO 2 PRO` (`25338763`) - `DRAFT`

Con este lote quedan **42 productos pendientes** en el CSV final.

Siguiente SKU pendiente en el orden del CSV:

- `1421203` - `Sexy Vibe! High Voltage - Liquid Vibrator`

## Nueva tanda importada

Se ha continuado la importaciÃ³n con los dos productos que quedaban realmente pendientes en este tramo del CSV final.

Productos creados y ya ajustados con stock en Shopify:

- `Vick Neo` (`25338715`) - `ACTIVE`, stock `22`, imagen en CDN de Shopify
- `WINNI 2` (`25338736`) - `ACTIVE`, stock `27`, imagen en CDN de Shopify

En ambos casos se ha usado la descripciÃ³n real de `Body (HTML)` del CSV y se ha dejado el inventario rastreado en la ubicaciÃ³n `C/ Sant cristofol 117 puerta 10`.

Con este cierre quedan **40 productos pendientes** en el CSV final, tomando como referencia el conteo anterior de `42` y descontando estos 2 nuevos.

## Nueva tanda importada

Se ha continuado la importaciÃ³n con otro lote de 10 productos nuevos de `SVAKOM` detectados m�s adelante en el CSV final.

Productos creados:

- `PULSE GALAXIE LILIAC` (`25338751`) - `ACTIVE`
- `SAM NEO SLEEVE` (`25338735`) - `ACTIVE`
- `Sleeve` (`25338713`) - `DRAFT`
- `Tammy Violet` (`25338420`) - `ACTIVE`
- `TRYSTA NEO ROMANTIC ROSE` (`25338761`) - `ACTIVE`
- `Trysta Plum` (`25336241`) - `DRAFT`
- `TULIP BLACK` (`25338730`) - `ACTIVE`
- `TULIP VIOLET` (`25338731`) - `ACTIVE`
- `TYLER BLACK` (`25336130`) - `ACTIVE`
- `Vick Black` (`25338130`) - `ACTIVE`

Las cantidades de stock se han fijado en Shopify para los 8 productos activos con inventario real. Los 2 sin stock se han dejado en `DRAFT`.

Con este lote quedan **30 productos pendientes** en el CSV final.

El siguiente tramo del CSV ya contiene varios productos que estaban repetidos o ya importados, asÃ­ que el pr�ximo hueco nuevo hay que localizarlo avanzando un poco m�s en el archivo.
## VerificaciÃ³n final del CSV de importaciÃ³n

Se ha revisado `shopify_import_lovlory_mvp_productos_con_pesos.csv` completo. El fichero contiene **189 productos** reales y termina en `WINNI 2` (`25338736`).

La comprobaciÃ³n con Shopify muestra que ese Ãºltimo tramo ya estÃ¡ importado y no queda un lote nuevo de 10 productos dentro del CSV MVP final.

Estado operativo actual:

- CSV MVP final agotado.
- Sin siguiente lote pendiente dentro del fichero de importaciÃ³n actual.
- Para continuar habrÃ­a que revisar otro origen o regenerar el CSV con nuevos productos.

## Colecciones, subcategorias ficticias y filtros

Se ha actualizado la estructura comercial de colecciones en Shopify para simular jerarquia sin categorias hijas nativas. Las colecciones principales funcionan como padres y las subcolecciones se representan con colecciones automaticas, reglas por tags/product type/vendor y filtros de producto.

Principales trabajadas:

- `Cosmetica Intima`
- `Juguetes Eroticos`
- `Lenceria y Moda Intima`
- `Fetiche y BDSM`
- `Juegos y Experiencias`

Ejemplo de jerarquia simulada:

- `Cosmetica Intima` contiene `Para Ella`, `Para El`, `Para Parejas / Todes` y `Masaje y Aromas`.
- `Para El` contiene productos propios y subgrupos como `Retardantes` y `Vigorizantes`.
- `Juguetes Eroticos` contiene subgrupos como `Vibradores y Succionadores`, `Anal y Prostata`, `Realisticos`, `Munecas tamano real`, `Munecos tamano real` y `Masturbadores`.

Se han normalizado tags puente en productos ya importados para que las colecciones automaticas se rellenen correctamente, sin borrar tags existentes. Algunos ejemplos:

- `cosmetica-el`, `subtipo-retardante`, `retardante`
- `subtipo-vigorizante`, `vigorizante`
- `cosmetica-parejas`, `lubricante`, `geles-efecto`
- `masaje-aromas`, `aceite-esencial`, `aceite-masaje`, `feromonas`, `perfume-feromonas`
- `tipo-succionador`, `succionador`, `anal`, `prostata`
- `muneca-tamano-real`, `muneco-tamano-real`, `masturbador`

Tambien se creo una capa inicial de tags `filtro-*`, pero Shopify Search & Discovery no los mostraba de forma fiable en la pantalla de seleccion de filtros. Para evitar depender de la indexacion de etiquetas, se creo un metafield de producto especifico para filtros:

- Nombre visible: `Subcategoria`
- Namespace/key: `custom.subcategoria`
- Tipo: `list.single_line_text_field`
- Owner: `PRODUCT`

Valores usados en el metafield `custom.subcategoria`:

- `Aceites esenciales`
- `Anal y prostata`
- `Cuidado del suelo pelvico`
- `Geles con efectos`
- `Lubricantes`
- `Masaje y aromas`
- `Masturbadores`
- `Munecas tamano real`
- `Munecos tamano real`
- `Para el`
- `Para ella`
- `Perfumes con feromonas`
- `Realisticos`
- `Retardantes`
- `Vibradores y succionadores`
- `Vigorizantes`

Verificaciones realizadas:

- `ALL-NATURAL ACQUA Water-based Intimate Gel` tiene `custom.subcategoria = ["Lubricantes"]`.
- `Barbara Love Doll` tiene `custom.subcategoria = ["Realisticos", "Munecas tamano real"]`.
- `PULSE GALAXIE BLACK` tiene `custom.subcategoria = ["Vibradores y succionadores"]`.

Configuracion recomendada en Shopify Search & Discovery:

- Fuente del filtro: metafield `Subcategoria` / `custom.subcategoria`.
- Etiqueta visible del filtro: `Subcategoria`.
- Valores: marcar todos los valores disponibles del metafield.
- Logica: `OR`, para que al seleccionar varias subcategorias se muestren productos que coincidan con cualquiera de ellas.

Nota: la tienda puede seguir usando las colecciones automaticas como paginas navegables y el metafield `Subcategoria` como filtro visual dentro de cada coleccion padre.
