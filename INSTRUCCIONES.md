# Instrucciones para Añadir Colecciones y Productos en Shopify

Este documento explica cómo añadir productos y colecciones en Shopify siguiendo la estructura preparada para LovLory. La idea principal es sencilla: las colecciones se llenan automáticamente cuando cada producto tiene bien configurada su marca, su tipo y sus etiquetas.

## 1. Cómo funcionan las colecciones

En Shopify un producto puede aparecer en varias colecciones al mismo tiempo. Por ejemplo, un lubricante de ORGIE puede estar en:

- Cosmética Íntima
- Lubricantes
- Para Parejas / Todes
- ORGIE
- Novedades, si es un producto nuevo
- Ofertas, si está rebajado

Para que esto funcione bien, cada producto debe tener los tags correctos. Un tag es una etiqueta interna que Shopify usa para clasificar productos.

Ejemplo de tag:

```text
subtipo-lubricante
```

Es importante escribir los tags siempre igual: en minúsculas, sin acentos, y usando guiones en lugar de espacios.

## 2. Colecciones actuales y tags necesarios

Estas son todas las colecciones previstas en la estructura de LovLory, incluidas las que todavía pueden estar vacías. Para que un producto entre en una colección automática, debe tener el tag indicado o el campo indicado en la tabla.

Importante: cuando una colección depende de un tag, hay que escribirlo exactamente igual. Cuando depende de la marca, se rellena desde el campo Marca o Proveedor del producto.

| Colección | Qué debe tener el producto |
| --- | --- |
| Cosmética Íntima | Tag `cosmetica-intima` |
| Cosmética Íntima - Para Ella | Tag `cosmetica-ella` o público `Ella` |
| Hidratantes vulvares | Tag `hidratante-vulvar` |
| Elixires de placer | Tag `elixir-placer` |
| Cuidado del suelo pélvico | Tag `suelo-pelvico` |
| Cosmética Íntima - Para Él | Tag `cosmetica-el` o público `Él` |
| Geles de higiene | Tag `gel-higiene-hombre` |
| Retardantes | Tag `retardante` |
| Vigorizantes | Tag `vigorizante` |
| Cosmética Íntima - Para Parejas / Todes | Tag `cosmetica-parejas` o público `Parejas/Todes` |
| Lubricantes | Tag `subtipo-lubricante` |
| Geles con efectos | Tag `subtipo-gel-efecto` |
| Espumas crocanti para masaje | Tag `espuma-crocanti` |
| Masaje y Aromas | Tag `masaje-aromas` |
| Aceites esenciales | Tag `aceite-esencial` |
| Perfumes con feromonas | Tag `feromonas` |
| Velas de masaje | Tag `vela-masaje` |
| Juguetes Eróticos | Tag `juguetes-eroticos` |
| Para Él | Tag `publico-el` |
| Para Ella | Tag `publico-ella` |
| Para Parejas / Todes | Tag `publico-parejas-todes` |
| Vibradores y Succionadores | Tag `tipo-vibrador` o `tipo-succionador` |
| Estimuladores de Pareja | Tag `estimulador-pareja` |
| Anal y Próstata | Tag `anal` o `prostata` |
| Kits de Iniciación | Tag `kit-iniciacion` |
| Realísticos | Tag `realistico` |
| Muñecas tamaño real | Tag `muneca-tamano-real` o tag `tamano-real` |
| Muñecos tamaño real | Tag `muneco-tamano-real` o tag `tamano-real` |
| Lencería y Moda Íntima | Tag `lenceria` |
| Sexy & Chic | Tag `sexy-chic` |
| Dark & Fetish | Tag `dark-fetish` |
| Conjuntos | Tag `conjunto` |
| Bodys | Tag `body` |
| Picardías y Babydolls | Tag `picardia` o `babydoll` |
| Accesorios de Moda Íntima | Tag `accesorio-moda-intima` |
| Fetiche y BDSM | Tag `fetiche-bdsm` |
| Ataduras y Sujeción | Tag `atadura` o `sujecion` |
| Sensaciones | Tag `sensaciones-bdsm` |
| Mordazas y Máscaras | Tag `mordaza` o `mascara` |
| Juegos y Experiencias | Tag `juegos-experiencias` |
| Juegos de Mesa | Tag `juego-mesa-erotico` |
| Packs LovLory | Tag `pack-lovlory` o marca / proveedor `LovLory` |
| Novedades | Tag `novedad` |
| Ofertas | Tag `oferta` |
| ORGIE | Marca / proveedor `ORGIE` |
| SVAKOM | Marca / proveedor `SVAKOM` |
| TENGA | Marca / proveedor `TENGA` |
| MISTRESS | Marca / proveedor `MISTRESS` |

Las colecciones de marca no dependen de un tag. Dependen del campo Marca o Proveedor del producto. Por eso hay que escribir la marca siempre igual y en mayúsculas: `ORGIE`, `SVAKOM`, `TENGA` o `MISTRESS`.

## 3. Cómo crear una colección nueva

Cuando se cree una colección nueva, lo recomendable es que sea automática.

Pasos:

1. En Shopify, entra en Productos > Colecciones.
2. Pulsa Crear colección.
3. Escribe el nombre de la colección.
4. Elige Colección automática.
5. Añade la condición que corresponda.
6. Guarda la colección.

Ejemplo: si se crea una colección llamada “Productos Premium”, se puede configurar para que entren todos los productos con el tag:

```text
premium
```

Así, cada vez que un producto tenga ese tag, Shopify lo añadirá automáticamente a la colección.

## 4. Cómo rellenar un producto nuevo

Al crear o editar un producto, revisa estos campos.

## Título

Debe ser el nombre comercial del producto, claro y sin añadir información inventada.

Ejemplo:

```text
TENGA - MASTURBADOR GEO AQUA
```

## Descripción

Debe salir de la información real del producto. No debe inventarse. Si viene de una ficha anterior, proveedor o importación, se puede revisar y mejorar, pero sin añadir datos falsos.

## Imágenes

Sube las imágenes directamente a Shopify. No conviene depender de imágenes alojadas en WordPress u otra web antigua.

Antes de publicar, comprueba que las imágenes se ven correctamente en la ficha del producto.

## Estado

Usa Borrador si falta algún dato importante:

- Precio
- Imagen
- Stock
- Peso
- Descripción

Usa Activo solo cuando el producto esté revisado y listo para vender.

## Marca o proveedor

Este campo es muy importante porque alimenta las colecciones de marca.

Usa siempre uno de estos valores:

```text
ORGIE
SVAKOM
TENGA
MISTRESS
```

No mezcles variantes como “Tenga”, “tenga” o “TENGA España”. Si se escribe diferente, Shopify puede no colocar el producto en la colección correcta.

## Tipo de producto

El tipo ayuda a organizar el catálogo. Debe ser una descripción general del producto.

Tipos usados actualmente:

```text
Masturbador masculino
Muñeca realista
Cosmética íntima
Juguete erótico
Vibrador
Ejercitador suelo pélvico
```

El tipo no sustituye a los tags. Un producto puede tener un solo tipo principal, pero varios tags.

## Tags

Los tags son lo más importante para que el producto entre en las colecciones automáticas.

Reglas para escribir tags:

- Usar minúsculas.
- No usar acentos.
- No usar espacios.
- Separar palabras con guiones.
- Escribirlos siempre exactamente igual.

Ejemplos correctos:

```text
juguetes-eroticos
publico-el
tipo-masturbador
cosmetica-intima
subtipo-lubricante
novedad
oferta
```

Ejemplos incorrectos:

```text
Juguetes Eróticos
publico el
lubricante
Oferta
```

## 5. Ejemplos prácticos

## Producto TENGA para hombre

Marca / proveedor:

```text
TENGA
```

Tipo de producto:

```text
Masturbador masculino
```

Tags recomendados:

```text
juguetes-eroticos
publico-el
tipo-masturbador
```

Si es nuevo, añadir también:

```text
novedad
```

## Lubricante ORGIE

Marca / proveedor:

```text
ORGIE
```

Tipo de producto:

```text
Cosmética íntima
```

Tags recomendados:

```text
cosmetica-intima
publico-parejas-todes
subtipo-lubricante
```

Si está rebajado, añadir también:

```text
oferta
```

## Vibrador SVAKOM

Marca / proveedor:

```text
SVAKOM
```

Tipo de producto:

```text
Vibrador
```

Tags recomendados:

```text
juguetes-eroticos
publico-ella
tipo-vibrador
```

Si es un producto de gama alta, se puede añadir:

```text
premium
```

## Muñeca MISTRESS

Marca / proveedor:

```text
MISTRESS
```

Tipo de producto:

```text
Muñeca realista
```

Tags recomendados:

```text
juguetes-eroticos
publico-el
tipo-muneca-realista
tamano-real
```

## 6. Precio, stock y envío

Antes de publicar un producto, revisa:

- Precio de venta.
- Precio de comparación, si está en oferta.
- SKU.
- Stock disponible.
- Peso del producto.
- Si requiere envío físico.

El peso es importante para calcular correctamente los envíos. Si no se conoce el peso, deja el producto en borrador hasta revisarlo.

## 7. SEO

En la zona de publicación en motores de búsqueda, revisa:

- Título SEO.
- Descripción SEO.
- URL del producto.

El título SEO debe ser claro y parecido al nombre del producto. La descripción SEO debe resumir el producto sin inventar características.

## 8. Añadir un producto manualmente a una colección

Sí, se puede añadir un producto manualmente a una colección aunque no tenga el tag.

Aun así, para este catálogo recomendamos usar siempre los tags. Así el sistema queda ordenado y, si más adelante se importan o actualizan productos en lote, las colecciones seguirán funcionando correctamente.

La regla práctica es:

- Para casos puntuales, se puede añadir manualmente.
- Para categorías principales, marcas, novedades y ofertas, usar tags o proveedor.

## 9. Qué revisar si un producto no aparece en una colección

Si un producto no aparece donde debería, revisa:

1. Que el tag esté escrito exactamente igual.
2. Que no haya espacios, acentos o mayúsculas diferentes.
3. Que la marca / proveedor esté bien escrita.
4. Que el producto esté activo si debe verse en la tienda.
5. Que la colección automática tenga la regla correcta.

## 10. Checklist antes de publicar

Antes de activar un producto, confirma:

- El título es correcto.
- La descripción es real y está revisada.
- Las imágenes están subidas a Shopify.
- El precio está informado.
- El SKU está informado.
- El stock está informado.
- El peso está informado.
- La marca / proveedor está bien escrita.
- El tipo de producto está indicado.
- Los tags necesarios están añadidos.
- El SEO está revisado.
- El producto aparece en las colecciones correctas.
