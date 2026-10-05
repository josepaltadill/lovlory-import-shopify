# Datos pendientes de solicitar al cliente

Este documento registra únicamente la información que falta por solicitar o confirmar para configurar la tienda Shopify. No deben guardarse aquí datos personales completos, documentos de identidad, contraseñas ni información bancaria.

## Información comercial y del titular

- [x] Confirmado que la titular desarrolla la actividad como autónoma individual y no mediante una sociedad (por ejemplo, SL o SLU).
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Tipo de empresa`.
- [x] Segundo apellido recibido y cumplimentado según la información facilitada por la clienta.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Nombre y apellidos`.
- [x] Fecha de nacimiento recibida y cumplimentada. No se registra el valor en el repositorio.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Fecha de nacimiento`.
- [x] Confirmado el domicilio profesional: **Sant Cristòfol, 117, Despacho/puerta n.º 10, 43870 Amposta (Tarragona)**.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Dirección residencial`.
- [ ] Solicitar la dirección residencial particular de la titular, coincidente con su documentación o comprobante de domicilio. Lorena ha confirmado que Sant Cristòfol es únicamente el domicilio profesional, por lo que no debe darse por válida en este campo.
  - **Seguridad:** recibirla y cumplimentarla por un canal seguro; no guardar la dirección residencial en el repositorio.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Dirección residencial`.

## Información fiscal

- [~] Confirmar el NIF de la autónoma y pedir a la gestoría el **número de IVA exacto que debe introducirse en Shopify**, incluido si debe usarse el formato `ES` + NIF. No guardar el número completo en el repositorio.
  - **Respuesta de Lorena (27/07/2026):** confirma que el NIF de la actividad corresponde a su DNI y que está dada de alta en el ROI y consta en VIES. No se registra el valor del documento.
  - **Pendiente:** la gestoría debe confirmar el formato exacto del número de IVA y si debe incluir el prefijo `ES`.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Recauda el IVA en un país de la UE > España > Recaudar IVA > Número de IVA`.
  - **Estado revisado (27/07/2026):** en la pantalla general de `Unión Europea`, España muestra el aviso `Umbral excedido` y el botón `Recaudar IVA`; todavía no consta un registro español de IVA configurado. No se realizó ningún cambio.
  - **Formulario revisado (27/07/2026):** el cuadro `Recaudar el IVA` tiene seleccionado `España` como país de registro y solicita un único campo `Número de IVA`, actualmente vacío. Shopify muestra un ejemplo con prefijo `ES`, pero no debe interpretarse como confirmación del formato aplicable a la titular. El formulario se dejó sin completar y no se pulsó `Recaudar el IVA`.
  - **Pantallas revisadas:** `Configuración > Impuestos y aranceles > Unión Europea` y `Unión Europea > Recauda el IVA en un país de la UE > España > Recaudar IVA`.
- [~] Confirmar con la gestoría si los precios de venta deben mostrarse con IVA incluido y el tipo de IVA aplicable al catálogo.
  - **Respuesta de Lorena (27/07/2026):** confirma que los precios se muestran con IVA incluido y que la mayoría de los productos tributan al 21 %. Indica que puede haber productos de los tres tipos y que confirmará la clasificación definitiva tras revisar el catálogo.
  - **Pendiente:** recibir la confirmación final del tipo aplicable a cada producto o grupo de productos. No aplicar anulaciones ni asumir tipos distintos del 21 % sin esa revisión.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Configuración adicional > Incluir impuesto sobre las ventas en el precio del producto y la tarifa de envío` y `Mercados > España > Impuestos y aranceles > Visualización de impuestos`.
  - **Estado revisado (27/07/2026):** `Incluir impuesto sobre las ventas en el precio del producto y la tarifa de envío` ya está activado, coherente con la confirmación de precios con IVA incluido. Shopify muestra que aplica provisionalmente una tasa del 0 % porque todavía no hay identificación fiscal configurada en la región. No se realizó ningún cambio.
  - **Otras opciones observadas:** `Cobrar impuesto sobre las ventas en el envío` está desactivado y Shopify indica que lo calcula automáticamente para la Unión Europea; `Cobrar IVA sobre contenidos digitales` también está desactivado. Mantener ambas sin cambios hasta validar la tributación del envío y confirmar que el catálogo del lanzamiento es exclusivamente físico.
  - **Mercado España revisado (27/07/2026):** el mercado está activo, el impuesto sobre las ventas figura `Sin recaudación` y la visualización seleccionada es `Visualización dinámica de impuestos`. No se cambió el desplegable ni se guardó el cuadro. Mantener esta selección y validar el resultado en escaparate y checkout después de completar el registro fiscal.
  - **Pantallas revisadas:** `Configuración > Impuestos y aranceles > Configuración adicional` y `Mercados > España > Impuestos y aranceles`.
- [~] Confirmar si la autónoma está inscrita en el régimen OSS.
  - **Respuesta de Lorena (27/07/2026):** prevé vender en España peninsular y Baleares, excluyendo Canarias, Ceuta y Melilla, y también en el resto de Europa excepto Reino Unido.
  - **Pendiente:** Lorena desconoce el estado de OSS y lo ha consultado con la gestoría; si no está inscrita, ha solicitado que se tramite. La inscripción en ROI/VIES no se utilizará como confirmación de OSS.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Recauda el IVA en ventas transfronterizas > Recaudar IVA`.
  - **Formulario revisado (27/07/2026):** `Recauda en toda la UE` permite escoger entre recaudar mediante un registro en Ventanilla Única (OSS) o utilizar el registro del país de origen para microempresas que cumplan las condiciones mostradas por Shopify. Ambas opciones solicitan país de registro y número de IVA; no había ninguna seleccionada y los campos estaban vacíos.
  - **Decisión:** no seleccionar ninguna modalidad ni pulsar `Recaudar IVA` hasta que la gestoría confirme expresamente si corresponde OSS o el régimen del país de origen y facilite el formato fiscal exacto.
  - **Pantalla revisada:** `Configuración > Impuestos y aranceles > Unión Europea > Recauda el IVA en ventas transfronterizas > Recaudar IVA`.
- [~] Confirmar si se utilizarán las facturas con IVA automáticas de Shopify y cómo se integrarán con Odoo.
  - **Respuesta de Lorena (27/07/2026):** prefiere generar las facturas directamente en Shopify si después puede volcarlas a Odoo.
  - **Pendiente:** acordar el flujo y comprobar la exportación o integración con Odoo antes de activar la generación automática.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Facturas con IVA > Generar y mostrar facturas cuando se realicen pedidos`.
  - **Estado revisado (27/07/2026):** `Generar y mostrar facturas cuando se realicen pedidos` está desactivado. Shopify indica que la función no está disponible para pedidos con envío a Portugal.
  - **Decisión:** mantenerla desactivada hasta definir cómo se trasladarán las facturas a Odoo, probar el flujo y decidir el tratamiento de Portugal dentro del alcance europeo.
  - **Pantalla revisada:** `Configuración > Impuestos y aranceles > Unión Europea > Facturas con IVA`.
- [~] Confirmar el alcance B2C/B2B y si deben gestionarse números de IVA de clientes.
  - **Respuesta de Lorena (27/07/2026):** la actividad será mayoritariamente B2C, aunque también prevé vender a asociaciones con NIF.
  - **Pendiente:** concretar si esas asociaciones deberán introducir nombre de empresa y número fiscal durante el checkout y qué tratamiento de factura e IVA corresponderá.
  - **Estado revisado (27/07/2026):** la tarjeta `Número de IVA de la empresa` aparece activada en la configuración de la UE, pero su botón `Gestionar` dirige a `Configuración > Pago > Información del cliente`. En esa pantalla, tanto `Nombre de la empresa` como `Número de IVA de la empresa` están configurados como `No incluir`, por lo que actualmente no se muestran en el checkout.
  - **Decisión:** mantener ambos campos en `No incluir` hasta cerrar con Lorena y la gestoría el flujo de venta y facturación para asociaciones. No se realizó ningún cambio.
  - **Pantallas revisadas:** `Configuración > Impuestos y aranceles > Unión Europea > Número de IVA de la empresa > Gestionar` y `Configuración > Pago > Información del cliente`.

## Preparación del correo

- [x] Solicitudes incorporadas al correo conjunto y enviadas a Lorena el 21 de julio de 2026.
- [x] Respuestas de Lorena sobre envío y preparación recibidas y registradas el 27 de julio de 2026. Cada valor queda pendiente de comprobar en su pantalla de Shopify antes de considerarlo configurado.

## Decisiones operativas por confirmar

- [x] Aprobado y configurado el formato de pedidos: **LV-1001, LV-1002, LV-1003…** (prefijo `LV-` y sufijo vacío).
  - **Pantalla:** `Configuración > General > Formato del ID del pedido`.

## Envío y preparación

> Lorena confirmó el 27 de julio de 2026 que configuró personalmente las opciones existentes. Sus respuestas se utilizaron como base comercial y cada pantalla del bloque se revisó posteriormente en Shopify.

> **Decisión de revisión:** se revisará y documentará una pantalla cada vez. No se activará la UE hasta cerrar países, tarifas y fiscalidad/OSS, ni se aplicarán opciones fiscales sin confirmación de Lorena o de su gestoría.

> **Estado del bloque (28/07/2026): revisión funcional completada.** Se han revisado las pantallas de origen, sucursal, perfiles, zonas, tarifas, plazos, paquetes, transportistas, entrega, recogida y documentos. El bloque queda pendiente de una única validación comercial final de Lorena. Las comprobaciones de IVA/OSS, aduanas, pesos del catálogo y textos legales continúan en sus bloques técnicos correspondientes y no se consideran parte de esta aprobación funcional.

- [x] Lorena confirma que configuró personalmente las zonas, tarifas, plazos y modalidades actuales y ha facilitado correcciones y condiciones comerciales.
  - **Respuesta de Lorena (27/07/2026):** solicita revisar las opciones actuales, corregir el solapamiento de la tarifa estándar, completar plazos y preparar la futura activación de la UE.
  - **Criterio de trabajo:** comprobar cada valor en su pantalla antes de cambiarlo. La autorización general no permite activar la UE mientras sigan pendientes OSS, países exactos y tarifas finales con IVA.
  - **Pantalla:** `Configuración > Envío y entrega` y `Configuración > Envío y entrega > Perfiles de envío > Perfil general`.
  - **Estado revisado (27/07/2026):** `Configuración > Envío y entrega` muestra un único `Perfil general` que contiene todos los productos, una sucursal y tres zonas. También muestra `Fechas manuales`, una caja y ninguna cuenta de empresa de transporte conectada. `Entrega local`, `Retiro en tienda` y `Puntos de retiro` están desactivados. No se abrió ningún elemento ni se realizó ningún cambio.
  - **Siguiente comprobación:** `Configuración > Envío y entrega > Perfiles de envío > Perfil general`.

### Origen, sucursal y preparación

- [x] Ubicación profesional de Amposta desde la que Lorena prepara los pedidos propios confirmada y validada.
  - **Valor actual:** `C/ Sant Cristofol 117 puerta 10, 43870 Amposta, Tarragona, España`.
  - **Diferencia detectada:** en la información facilitada anteriormente figura `Sant Cristòfol, 117, Despacho n.º 10`.
  - **Respuesta de Lorena (27/07/2026):** confirma que se trata de un entresuelo con varios despachos y autoriza usar la forma que Shopify acepte mejor. También confirma que otros pedidos salen directamente de almacenes de proveedores mediante dropshipping.
  - **Decisión:** se acepta como correcta la forma almacenada por Shopify, con `puerta 10`, para identificar el despacho profesional de Amposta.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Ubicación de procesamiento` y `Configuración > Sucursales`.
  - **Estado validado (27/07/2026):** el `Perfil general` muestra una única ubicación de procesamiento con la dirección profesional de Sant Cristòfol 117, puerta 10, Amposta. La dirección se confirma como correcta y no requiere cambios.
  - **Seguimiento independiente:** decidir si los almacenes de proveedores deben representarse como ubicaciones, una aplicación de dropshipping o únicamente como operativa externa. No registrar sus direcciones hasta determinar que sean necesarias.
- [x] Nombre interno de la sucursal de Amposta confirmado y configurado como `LovLory — Amposta`.
  - **Estado final (27/07/2026):** la sucursal es la predeterminada y tiene activado el uso de su inventario para preparar pedidos online. El envío está activado; entrega local, retiro en tienda y envío a puntos de retiro están desactivados.
  - **Cambio aplicado:** el nombre anterior, basado en la dirección completa, se sustituyó por `LovLory — Amposta`. La dirección no se modificó.
  - **Pantalla:** `Configuración > Sucursales > LovLory — Amposta > Información de la sucursal > Nombre`.
- [~] Definir el modelo de ubicaciones para los almacenes de proveedores.
  - **Respuesta de Lorena (27/07/2026):** existen varios almacenes de proveedores desde los que se envía directamente al cliente.
  - **Decisión (27/07/2026):** no solicitar ni crear por ahora una sucursal física para cada proveedor. En Shopify, una aplicación de dropshipping puede crear su propia ubicación; si el proveedor trabaja sin aplicación pero acepta pedidos por correo, puede configurarse posteriormente como servicio de logística personalizado.
  - **Datos mínimos que deben recopilarse primero por proveedor:** nombre comercial o identificador interno; productos/SKU que prepara; método de transmisión del pedido (aplicación, API, correo o gestión manual); sincronización de stock; países atendidos; costes y plazos; transportistas; seguimiento; seguro; devoluciones y tratamiento de pedidos con productos de varios orígenes.
  - **Dirección completa:** pedirla únicamente si resulta necesaria para comprar etiquetas desde Shopify, calcular tarifas desde el origen, gestionar una devolución o cumplir una obligación operativa/legal confirmada. No guardarla en el repositorio si corresponde a una dirección personal.
  - **Pendiente:** inventariar proveedores y flujo de stock/preparación antes de crear aplicaciones, servicios de logística o ubicaciones. Mantener mientras tanto `LovLory — Amposta` como única sucursal física configurada.
  - **Pantalla relacionada:** `Configuración > Sucursales` y `Configuración > Envío y entrega > Perfil general > Ubicación de procesamiento`.
  - **Fiscalidad:** Shopify muestra un aviso para revisar si existe obligación de recaudar impuestos en Tarragona. No se abrió `Gestionar obligación tributaria` ni se realizó ningún cambio; cualquier actuación queda bloqueada hasta confirmación de Lorena o de su gestoría.
- [x] Trasladar a Shopify los plazos operativos facilitados como plazos totales por tarifa.
  - **Respuesta de Lorena (27/07/2026):** 24/48 horas laborables para pedidos nacionales realizados antes de las 16:00 y 2–5 días laborables para pedidos europeos realizados antes de las 14:00.
  - **Estado revisado (27/07/2026):** `Fechas de entrega estimadas` está configurado en modo `Manual` con un tiempo global de preparación de `Siguiente día hábil`. Shopify indica expresamente que calcula el rango mostrado sumando este tiempo de preparación al tiempo de tránsito definido en cada tarifa. No se realizó ningún cambio.
  - **Incidencia:** la respuesta de Lorena se dio al preguntar por preparación, pero 24/48 horas también coincide con el plazo solicitado para la tarifa urgente y 2–5 días con el plazo de la tarifa estándar nacional. Si fueran plazos totales y se introdujeran como tránsito, Shopify añadiría además el día de preparación.
  - **Decisión resuelta (27/07/2026):** interpretar estándar nacional `2–5 días hábiles`, urgente `1–2 días hábiles` y UE `3–7 días hábiles` como plazos totales visibles al cliente.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas`.
  - **Decisión aplicada (27/07/2026):** los intervalos se tratarán como plazos totales visibles y se configurarán en cada tarifa. Se desactivó la suma global de preparación para evitar incrementarlos automáticamente.
- [x] Días de expedición, festivos y tratamiento de pedidos posteriores a la hora límite definidos.
  - **Respuesta de Lorena (27/07/2026):** no se realizan envíos en domingos ni festivos nacionales; indica corte a las 16:00 para nacional y a las 14:00 para Europa.
  - **Criterio operativo (27/07/2026):** interpretar la respuesta literalmente como expediciones de lunes a sábado, excepto festivos nacionales. Los pedidos nacionales recibidos después de las 16:00 y los europeos recibidos después de las 14:00 pasan al siguiente día de expedición disponible.
  - **Aplicación en Shopify:** `Fechas de entrega estimadas` permanece `Desactivado` porque el tiempo de preparación mostrado por Shopify es global y no permite representar en esta pantalla dos cortes diferentes por destino. Los márgenes derivados del corte, domingos, festivos y disponibilidad de las agencias se absorben en el plazo total de cada tarifa.
  - **Comunicación al cliente:** indicar en la política de envíos que las expediciones se realizan en horario laboral, sujetas a disponibilidad de las agencias y posibles incidencias técnicas, y que no se realizan en domingos ni festivos nacionales.
  - **Revisión:** este criterio se incluirá en la única validación final conjunta de Lorena; no queda como solicitud independiente.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas`.
- [x] Mostrar al cliente el plazo configurado en cada tarifa, sin sumar automáticamente un tiempo global de preparación.
  - **Funcionamiento comprobado (27/07/2026):** el modo `Manual` actual muestra la suma del tiempo global de preparación y el tiempo de tránsito de cada tarifa. La alternativa `Desactivado` mostraría únicamente el tránsito o la descripción personalizada de la tarifa.
  - **Configuración aprobada:** estándar nacional y gratuito `2–5 días hábiles`; urgente `1–2 días hábiles`; UE `3–7 días hábiles`. Para la recogida en el despacho, usar una descripción como `Disponible para recoger en 2–5 días hábiles`, ya que no existe tránsito de transportista.
  - **Estado final (27/07/2026):** `Fechas de entrega estimadas` se cambió de `Manual` a `Desactivado`. Shopify confirmó la actualización y el resumen muestra `Desactivado`. Los plazos individuales todavía deben configurarse y verificarse tarifa por tarifa.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas` y `Perfil general > Editar opción de envío > Tiempo de tránsito`.

### Destinos y zonas

- [x] Destinos nacionales del lanzamiento confirmados: España peninsular y Baleares.
  - **Valor inicial:** existía una única zona llamada `España` con las 52 provincias.
  - **Respuesta de Lorena (27/07/2026):** no incluye Canarias, Ceuta ni Melilla.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zona España > Editar zona`.
  - **Estado revisado (27/07/2026):** `Editar zona de envío` confirma que `España` tiene seleccionadas las 52 provincias. Por tanto, la zona actual incluye Península, Baleares, Canarias, Ceuta y Melilla, y no cumple todavía el alcance confirmado. Se cerró con `Cancelar` y no se realizó ningún cambio.
  - **Configuración guardada (27/07/2026):** la zona se renombró `España peninsular` y quedó limitada a `España (47 de 52 provincias)`. Se excluyeron Islas Baleares, Las Palmas, Santa Cruz de Tenerife, Ceuta y Melilla. Shopify guardó el perfil y ya no muestra cambios pendientes.
  - **Estructura pendiente:** crear la zona no solapada `Baleares`; mantener Canarias, Ceuta y Melilla sin zona de envío. Shopify solo permite que una provincia pertenezca a una zona del mismo grupo de sucursales.
- [x] Baleares dispone de una zona diferenciada de Península.
  - **Respuesta de Lorena (27/07/2026):** facilita costes orientativos de Baleares sin IVA distintos de Península. Las capturas muestran SEUR a domicilio desde 7,74 € y Correos Express en oficina o domicilio desde 8,62 €, con plazo de 48–72 horas.
  - **Configuración guardada (27/07/2026):** se creó la zona `Baleares` seleccionando exclusivamente `España (Islas Baleares)`. Shopify confirmó `Perfil actualizado`.
  - **Tarifa estándar guardada (27/07/2026):** `Estándar Baleares`, tipo `Importe del pedido`, mínimo 0,00 €, máximo 49,99 €, precio 8,62 € y plazo personalizado de 2–3 días hábiles. Shopify confirmó `Perfil actualizado`.
  - **Tarifa gratuita guardada (27/07/2026):** `Estándar Baleares`, tipo `Importe del pedido`, mínimo 50,00 €, sin máximo, precio 0,00 € y plazo personalizado de 2–3 días hábiles. El resumen confirma ambos tramos sin huecos ni solapamiento.
  - **Estado:** configuración operativa completada; queda incluida en la validación final conjunta de Lorena.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas de envío`.
- [x] Mantener bloqueadas inicialmente Canarias, Ceuta y Melilla.
  - **Respuesta de Lorena (27/07/2026):** el lanzamiento nacional se limita a Península y Baleares.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas de envío` y `Mercados > España`.
- [~] Lorena solicita vender en la Unión Europea y activar la zona cuando esté preparada.
  - **Valor actual:** todos los países de la antigua zona `UE (Unión Europea)` se han distribuido en mercados y zonas tarifarias específicas. La zona general se eliminó al configurar los dos últimos destinos, Chequia y Polonia.
  - **Respuesta de Lorena (27/07/2026):** solicita un plazo de 3–7 días laborables y envío gratuito desde 150 €, y ha facilitado costes orientativos por grupos de países sin IVA.
  - **Pendiente:** concretar países, convertir los costes en precios finales con IVA y cerrar OSS con la gestoría. No activar todavía.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > UE (Unión Europea)` y `Mercados`.
  - **Estado revisado (28/07/2026):** la zona general se sustituyó por grupos específicos según las tablas recibidas y ya no existe en el perfil. Todos sus países tienen una zona de envío y un mercado activo. La configuración logística no resuelve IVA/OSS, que continúa pendiente de confirmación de la gestoría; no se modificó fiscalidad.
- [~] Separar Portugal de la zona general UE y configurarlo como destino propio.
  - **Valor actual (28/07/2026):** Portugal ya no pertenece a la zona general UE. Existe un mercado independiente `Portugal` en estado `Activo`, con moneda EUR, y una zona de envío propia.
  - **Tarifas facilitadas:** NACEX desde 4,06 € en oficina y 5,20 € a domicilio, con 24–48 horas; Correos Express desde 4,93 € a domicilio, con 24–48 horas; NACEX urgente desde 15,01 € antes de las 12:00; SEUR urgente desde 7,79 € antes de las 13:30. Son importes `Desde` y sin IVA.
  - **Propuesta de configuración:** zona independiente `Portugal`; `Estándar Portugal` a domicilio por 5,20 € entre 0,00 € y 149,99 €, con 1–2 días laborables; `Envío gratuito` desde 150 € con el mismo plazo; y `Urgente Portugal` por 15,01 €, con 1 día laborable. Mantener nombres genéricos y asignar la agencia internamente.
  - **Diferencia pendiente de confirmar:** la captura específica de Portugal indica 24–48 horas, mientras que Lorena indicó 3–7 días laborables para la UE en general. La propuesta trata Portugal como excepción específica.
  - **Configuración aplicada:** `Estándar Portugal`, 5,20 € entre 0,00 € y 149,99 €, con 1–2 días laborables; `Envío gratuito` desde 150 €, con 1–2 días laborables; y `Urgente Portugal`, 15,01 €, con 1 día laborable.
  - **Mercados y fiscalidad:** el mercado `Portugal` se activó por autorización expresa el 28/07/2026. La configuración fiscal continúa heredada como `Sin recaudación`; no se abrió ni se modificó IVA/OSS.
  - **Pantallas revisadas:** `Configuración > Envío y entrega > Perfil general > UE (Unión Europea)` y `Mercados > Portugal`.
  - **Estado revisado (28/07/2026):** Portugal se retiró de `UE (Unión Europea)`, se creó la zona independiente y se guardaron las tres tarifas sin huecos en el tramo estándar/gratuito. Tras activar el mercado, Shopify muestra `Portugal — Activo` y `3 tarifas • Envío a Portugal`.
  - **Pendiente:** ejecutar QA de checkout para un pedido inferior a 150 €, otro igual o superior y la opción urgente. La activación comercial no resuelve el tratamiento fiscal; IVA/OSS continúa bloqueado hasta indicación de la gestoría.
- [x] Separar Francia de la zona general UE y configurarla como destino propio.
  - **Tarifas facilitadas:** DPD a domicilio desde 7,88 € y UPS a domicilio desde 8,08 €, ambas con plazo de 48–72 horas. Los importes son `Desde` y sin IVA.
  - **Decisión aprobada (28/07/2026):** mantener una opción genérica a domicilio y utilizar 8,08 €, la referencia más alta disponible, sin mostrar DPD ni UPS al cliente. Aplicar también la regla europea de envío gratuito desde 150 €.
  - **Configuración aplicada:** mercado independiente `Francia` activo y en EUR; zona de envío `Francia`; `Estándar Francia` por 8,08 € entre 0,00 € y 149,99 €; y `Envío gratuito` desde 150,00 €. Ambas opciones muestran `Entrega en 2–3 días hábiles`.
  - **Comprobación:** Francia se eliminó de `UE (Unión Europea)` y la revisión posterior del perfil confirmó los dos tramos sin hueco ni solapamiento: 0,00–149,99 € y desde 150,00 €.
  - **Fiscalidad:** el mercado mantiene la configuración heredada `Sin recaudación`. No se abrió ni se modificó IVA, OSS ni ninguna opción fiscal.
  - **Pantallas revisadas:** `Mercados > Francia` y `Configuración > Envío y entrega > Perfil general > Francia`.
  - **Pendiente:** ejecutar QA de checkout con un pedido inferior a 150 € y otro igual o superior. La validación fiscal continúa bloqueada hasta indicación de la gestoría.
- [x] Separar Italia y Alemania de la zona general UE y configurarlas como un grupo propio.
  - **Tarifas facilitadas:** DPD a domicilio desde 8,33 € y UPS a domicilio desde 11,83 €, ambas con plazo de 48–72 horas; DHL a domicilio desde 15,88 €, con plazo de 24 horas. Los importes son `Desde` y sin IVA.
  - **Decisión aplicada (28/07/2026):** agrupar Italia y Alemania porque comparten exactamente la misma tabla. Mostrar servicios genéricos: estándar por 11,83 €, tomando la referencia ordinaria más alta; urgente por 15,88 €; y envío gratuito desde 150 €. No mostrar DPD, UPS ni DHL al cliente.
  - **Configuración aplicada:** mercado `Italia y Alemania` activo y en EUR; zona de envío con Alemania e Italia; `Estándar Italia y Alemania` por 11,83 € entre 0,00 € y 149,99 €, con `Entrega en 2–3 días hábiles`; `Envío gratuito` desde 150,00 €, con el mismo plazo; y `Urgente Italia y Alemania` por 15,88 €, con `Entrega en 1 día hábil`.
  - **Comprobación:** Italia y Alemania se eliminaron de `UE (Unión Europea)`. La revisión posterior confirmó ambos países dentro de la nueva zona, los tres servicios activos y los dos tramos estándar/gratuito sin hueco ni solapamiento.
  - **Fiscalidad:** el mercado mantiene la configuración heredada. No se abrió ni se modificó IVA, OSS ni ninguna opción fiscal.
  - **Pantallas revisadas:** `Mercados > Italia y Alemania` y `Configuración > Envío y entrega > Perfil general > Italia y Alemania`.
  - **Pendiente:** QA de checkout para estándar, gratuito y urgente; validar costes reales y margen porque las referencias recibidas son importes `Desde` sin IVA.
- [x] Configurar el grupo europeo de Países Bajos, Bélgica, Luxemburgo, Austria, Bulgaria, Croacia, Dinamarca, Eslovaquia, Eslovenia, Estonia, Finlandia, Grecia, Hungría, Irlanda, Letonia, Lituania, Rumanía y Suecia.
  - **Tarifas facilitadas:** DPD a domicilio desde 11,31 € y UPS a domicilio desde 10,38 €, ambas con plazo de 48–72 horas; DHL a domicilio desde 16,25 €, con plazo de 24 horas. Los importes son `Desde` y sin IVA.
  - **Decisión aplicada (28/07/2026):** agrupar los 18 países porque comparten exactamente la misma tabla. Mostrar servicios genéricos: estándar por 11,31 €, tomando la referencia ordinaria más alta; urgente por 16,25 €; y envío gratuito desde 150 €. No mostrar DPD, UPS ni DHL al cliente.
  - **Configuración aplicada:** mercado y zona `UE — Grupo 11,31 €`, activos y en EUR; `Estándar Europa grupo 11,31 €` por 11,31 € entre 0,00 € y 149,99 €, con `Entrega en 2–3 días hábiles`; `Envío gratuito` desde 150,00 €, con el mismo plazo; y `Urgente Europa grupo 11,31 €` por 16,25 €, con `Entrega en 1 día hábil`.
  - **Comprobación:** la revisión posterior confirmó los 18 países, los tres servicios activos y los tramos estándar/gratuito sin huecos ni solapamientos. Estos países se retiraron de la zona UE general.
  - **Fiscalidad:** el mercado mantiene la configuración heredada. No se abrió ni se modificó IVA, OSS ni ninguna opción fiscal.
  - **Pantallas revisadas:** `Mercados > UE — Grupo 11,31 €` y `Configuración > Envío y entrega > Perfil general > UE — Grupo 11,31 €`.
  - **Pendiente:** QA de checkout para estándar, gratuito y urgente; validar costes reales y margen porque las referencias recibidas son importes `Desde` sin IVA.
- [x] Configurar el grupo de Chipre, Malta, Liechtenstein, Islandia, Moldavia, Noruega, San Marino, Suiza y Ucrania.
  - **Tarifa facilitada:** DHL a domicilio desde 21,75 €, con plazo indicado de 48 horas. El importe es `Desde` y sin IVA.
  - **Decisión aplicada (28/07/2026):** agrupar los nueve países porque comparten la misma tarifa. Mostrar una opción genérica de 21,75 € y aplicar también el envío gratuito desde 150 €, sin mostrar DHL al cliente.
  - **Configuración aplicada:** mercado y zona `Europa — Grupo 21,75 €`, activos y en EUR; `Estándar Europa grupo 21,75 €` por 21,75 € entre 0,00 € y 149,99 €, con `Entrega en 2 días hábiles`; y `Envío gratuito` desde 150,00 €, con el mismo plazo.
  - **Comprobación:** la revisión posterior confirmó los nueve países, las dos opciones activas y los tramos sin huecos ni solapamientos. Chipre y Malta se retiraron de la zona UE general; Noruega y Suiza se retiraron de `Internacional`.
  - **Fiscalidad:** el grupo mezcla países comunitarios y no comunitarios. No se abrió ni se modificó IVA, OSS, aranceles ni ninguna opción fiscal; su tratamiento sigue pendiente de Lorena o de la gestoría.
  - **Pantallas revisadas:** `Mercados > Europa — Grupo 21,75 €` y `Configuración > Envío y entrega > Perfil general > Europa — Grupo 21,75 €`.
  - **Pendiente:** QA de checkout para ambos tramos, validación de costes reales y margen, y confirmación fiscal/aduanera para los destinos no comunitarios.
- [x] Configurar Polonia y Chequia como último grupo de la antigua zona UE general.
  - **Tarifas facilitadas:** DPD a domicilio desde 11,28 €, con plazo de 4–6 días; UPS a domicilio desde 11,83 €, con plazo de 3–5 días. Los importes son `Desde` y sin IVA.
  - **Decisión aplicada (28/07/2026):** utilizar 11,83 €, la referencia ordinaria más alta, y una promesa genérica conservadora de 4–6 días hábiles mientras no se confirme qué agencia se asignará. Aplicar envío gratuito desde 150 € y no mostrar DPD ni UPS.
  - **Configuración aplicada:** mercado y zona `Polonia y Chequia`, activos y en EUR; `Estándar Polonia y Chequia` por 11,83 € entre 0,00 € y 149,99 €, con `Entrega en 4–6 días hábiles`; y `Envío gratuito` desde 150,00 €, con el mismo plazo.
  - **Comprobación:** la revisión posterior confirmó Chequia y Polonia, las dos opciones activas y los tramos sin huecos ni solapamientos. La antigua zona `UE (Unión Europea)` se eliminó porque ya no contenía otros países.
  - **Fiscalidad:** no se abrió ni se modificó IVA, OSS ni ninguna opción fiscal.
  - **Pantallas revisadas:** `Mercados > Polonia y Chequia` y `Configuración > Envío y entrega > Perfil general > Polonia y Chequia`.
  - **Pendiente:** QA de checkout para ambos tramos y validación conjunta de costes reales y margen.
- [x] Configurar Andorra como destino internacional no perteneciente a la UE.
  - **Tarifa facilitada:** Correos Express a domicilio desde 17,27 €, con plazo indicado de 24–48 horas. Correos no muestra una tarifa disponible.
  - **Aprobación (28/07/2026):** se autoriza crear y activar un mercado independiente para Andorra y utilizar 17,27 € como tarifa mostrada en Shopify.
  - **Configuración aplicada:** mercado `Andorra` activo, moneda EUR; zona de envío independiente `Andorra`; opción `Envío a domicilio` de 17,27 € con tránsito de 1–2 días laborables; y `Envío gratuito` desde 150 € con el mismo tránsito de 1–2 días laborables.
  - **Fiscalidad:** el mercado conserva la configuración heredada `Sin recaudación`. No se abrió ni modificó `Impuestos y aranceles`.
  - **Pantallas revisadas:** `Mercados > Andorra` y `Configuración > Envío y entrega > Perfil general > Andorra`.
  - **Estado revisado (28/07/2026):** Shopify muestra el mercado `Andorra` como `Activo`. El perfil general muestra las dos opciones de Andorra y confirmó `Perfil actualizado`.
- [x] Excluir los restantes destinos internacionales no validados.
  - **Valor anterior:** tras retirar Noruega y Suiza, la zona `Internacional` mantenía 12 países/regiones y una tarifa de 12,99 €, pero no estaba habilitada porque esos países no pertenecían a un mercado activo.
  - **Destinos excluidos:** Emiratos Árabes Unidos, Australia, Canadá, Reino Unido, Hong Kong, Israel, Japón, Corea del Sur, Malasia, Nueva Zelanda, Singapur y Estados Unidos.
  - **Pantalla revisada (28/07/2026):** `Configuración > Envío y entrega > Perfil general > Internacional` muestra el aviso de que los 12 países deben incluirse en un mercado para poder vender y conserva una única opción `Estándar` de 12,99 €.
  - **Conclusión:** la zona puede eliminarse sin afectar a los mercados ni destinos activos. Su eliminación retiraría únicamente esta cobertura y tarifa antiguas; si Lovlory decide vender posteriormente en alguno de esos países, deberá crearse una zona nueva con precios, plazos y condiciones validados.
  - **Aplicación confirmada (28/07/2026):** por confirmación expresa se eliminó la zona `Internacional` y su tarifa antigua de 12,99 €. La comprobación posterior confirma que la zona ya no existe y que permanecen intactas las nueve zonas válidas del perfil.
  - **Criterio futuro:** si Lovlory decide vender posteriormente en alguno de los 12 destinos excluidos, deberá crearse una zona nueva con mercado, tarifas, plazos y tratamiento fiscal/aduanero previamente validados.

### Tarifas nacionales encontradas

- [x] Envío gratuito en España peninsular configurado para pedidos de **50,00 € o más**.
  - **Valor actual:** `Estándar`, tarifa por importe del pedido, mínimo 50,00 €, sin máximo y precio 0,00 €.
  - **Respuesta de Lorena (27/07/2026):** mantener el umbral y añadir 2–5 días laborables.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Estándar gratis > Editar opción de envío`.
  - **Resumen revisado (27/07/2026):** el perfil muestra `Estándar`, pedidos desde 50,00 €, gratis, pero no muestra un plazo. Falta abrir la tarifa para completarlo.
  - **Estado final (27/07/2026):** se mantuvo el tipo `Importe del pedido`, mínimo 50,00 €, sin máximo y precio 0,00 €. Se añadió un tránsito personalizado de 2–5 días hábiles, se guardó el perfil y Shopify confirmó `Perfil actualizado`. Tras separar la zona, esta gratuidad se aplica a `España peninsular`; su aplicación a Baleares sigue pendiente.
- [x] Tarifa estándar de España peninsular configurada en 5,20 € para pedidos de 0,00 € a 49,99 €.
  - **Valor inicial:** `Estándar`, tarifa fija de 4,95 €, sin condiciones por importe y con tiempo de tránsito de 2 a 5 días hábiles.
  - **Respuesta de Lorena (27/07/2026):** confirma que el solapamiento es un error y autoriza configurar correctamente el límite máximo.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Estándar 4,95 € > Editar opción de envío`.
  - **Resumen revisado (27/07/2026):** el perfil muestra 2–5 días hábiles y 4,95 €, pero el resumen no permite confirmar el límite máximo. Falta abrir la tarifa.
  - **Formulario revisado (27/07/2026):** nombre `Estándar`, tipo `Fija`, precio 4,95 €, tránsito de 2–5 días hábiles y envío gratis desactivado. Al ser una tarifa fija, el formulario no muestra condiciones por importe; se confirma que todavía no termina en 49,99 €. No se realizó ningún cambio.
  - **Estado final (27/07/2026):** se cambió el tipo a `Importe del pedido`, con mínimo 0,00 €, máximo 49,99 €, precio 4,95 € y tránsito de 2–5 días hábiles. Se guardó el perfil y el resumen confirma los valores. El solapamiento con el envío gratuito desde 50 € queda corregido.
  - **Actualización guardada (27/07/2026):** por decisión del proyecto se sustituyó el precio de 4,95 € por 5,20 €. El resumen del perfil confirma `Estándar`, pedidos de 0,00 € a 49,99 €, 2–5 días hábiles y 5,20 € dentro de `España peninsular`.
- [x] `Recogida en Lovlory` corresponde a la recogida por el cliente en el despacho de Amposta.
  - **Valor actual:** tarifa fija de 3,95 €, sin condiciones visibles por importe y sin tiempo de tránsito configurado. Aparece como tarifa de envío disponible para toda la zona España, mientras que `Retiro en tienda` y `Puntos de retiro` están desactivados.
  - **Respuesta de Lorena (27/07/2026):** confirma que el cliente recoge el pedido en el despacho y que se cobra un coste de organización de 3,95 € para pedidos inferiores a 100 €; desde 100 € la recogida es gratuita. Solicita 2–5 días laborables y valora cambiar el nombre.
  - **Limitación comprobada:** la función nativa `Retiro en tienda` de Shopify presenta correctamente la recogida en el checkout, pero su tarifa es gratuita y no permite configurar el cobro de 3,95 €. Mantener la regla comercial confirmada requeriría una solución adicional; la tarifa de envío actual no debe darse por válida como recogida porque se ofrece para toda la zona España.
  - **Opción propuesta (27/07/2026):** `Zapiet – Pickup + Delivery` permite mostrar una modalidad de recogida diferenciada y aplicar precios condicionados por el importe del pedido. Configuración prevista: `Recogida en Lovlory`, 3,95 € entre 0,00 € y 99,99 €, gratis desde 100,00 € y preparación estimada de 2–5 días laborables. El plan inicial anunciado es de 29,99 USD/mes, con prueba de 14 días.
  - **Decisión del proyecto (27/07/2026):** se descarta utilizar una aplicación de pago. Se acepta probar la alternativa sin coste mediante tarifas por importe dentro de la zona España, dejando claro en el nombre que no es un envío.
  - **Configuración guardada (27/07/2026):** nombre `Recogida en Lovlory — Amposta (no se envía)`; 3,95 € entre 0,00 € y 99,99 €; gratis desde 100,00 €; plazo de 2–5 días hábiles en ambos tramos. Shopify actualizó el perfil y el resumen muestra la modalidad por importe, el plazo y un rango de precios de 0,00 € a 3,95 €.
  - **Pendiente:** probar ambos importes en el checkout. Shopify seguirá tratando administrativamente los pedidos como envíos y mostrará la opción a clientes con dirección de España peninsular; esta limitación deberá explicarse y verificarse durante el QA. La disponibilidad para Baleares deberá decidirse al crear esa zona.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Recogida en Lovlory` y `Formas de entrega adicionales`.
  - **Resumen revisado (27/07/2026):** se pulsó `Listo`, se guardó el perfil y Shopify conservó el nuevo nombre, los dos tramos y el plazo. No se instaló ninguna aplicación ni se inició ninguna suscripción.
- [x] Servicio urgente configurado para España peninsular.
  - **Valor final configurado:** `Urgente`, 15,01 €, con tránsito de 1–2 días laborables.
  - **Respuesta de Lorena (27/07/2026):** solicita mostrar 24/48 horas e indica entregas en sábado.
  - **Tarifas contrastadas (28/07/2026):** NACEX a domicilio desde 15,01 €, entrega garantizada antes de las 12:00; SEUR desde 7,79 €, antes de las 13:30; Correos Express desde 7,68 €, antes de las 14:00. SEUR antes de las 10:00 no muestra precio. Son costes `Desde` facilitados sin IVA.
  - **Decisión aprobada (28/07/2026):** mantener una única opción genérica, sin mostrar transportista ni prometer una hora concreta, utilizando la referencia disponible más alta a domicilio para permitir que el almacén seleccione la agencia.
  - **Advertencia comercial:** la referencia original continúa siendo `Desde` y sin IVA; revisar margen, pesos y recargos en la validación conjunta, sin modificar opciones fiscales.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Urgente > Editar opción de envío`.
  - **Estado aplicado (28/07/2026):** se sustituyeron los 9,50 € por 15,01 € y se añadió el tránsito de 1–2 días laborables. Shopify confirmó `Perfil actualizado`.
- [~] Lorena confirma que los precios cobrados al cliente deben incluir IVA; la tabla de costes de almacén recibida está expresada sin IVA.
  - **Aclaración revisada (27/07/2026):** la tabla recibida refleja costes orientativos de compra que los transportistas o almacenes cobran a Lovlory; las tarifas fijas de Shopify son precios comerciales de venta que paga el cliente. No es necesario crear en el checkout una tarifa por cada transportista si el cliente verá un único servicio estándar.
  - **Decisión aplicada (27/07/2026):** se fija provisionalmente en Shopify un precio comercial de 5,20 € para el servicio estándar peninsular de pedidos inferiores a 50 €. La cifra coincide con la referencia más alta de entrega a domicilio mostrada en las capturas, pero esa referencia es `Desde` y está expresada sin IVA.
  - **Respuesta adicional de Lorena (28/07/2026):** confirma expresamente que los importes cobrados al cliente por el envío deben incluir IVA y que las tarifas facilitadas por el almacén están expresadas sin IVA.
  - **Estado revisado (28/07/2026):** los importes de pago configurados hasta ahora reproducen provisionalmente referencias netas `Desde` del almacén. Por tanto, no deben considerarse precios finales aprobados: deben convertirse en precios comerciales finales con IVA incluido y margen suficiente antes del cierre.
  - **Pendiente fiscal bloqueante:** la gestoría debe confirmar el tipo y método aplicable al transporte y validar el funcionamiento de Shopify cuando se complete el registro fiscal. No multiplicar automáticamente todas las tarifas por el 21 %, ni activar o modificar opciones fiscales, hasta recibir esa confirmación. La casilla global para incluir el impuesto en el precio del producto y la tarifa de envío ya estaba activada; actualmente Shopify muestra recaudación al 0 % por falta de registro fiscal configurado.
  - **Riesgo pendiente:** los importes guardados pueden no cubrir el coste real según peso, volumen, origen, código postal y recargos. Tras la confirmación fiscal se recalcularán todas las tarifas de pago y se probará en checkout que el cliente ve el total final y que Shopify separa correctamente la parte impositiva.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas y tarifas` y `Configuración > Impuestos y aranceles`.
- [~] Existen condiciones especiales que requieren perfiles o tarifas específicas.
  - **Respuesta de Lorena (27–28/07/2026):** los envíos habituales pesan aproximadamente entre 1 y 5 kg; las muñecas Mistress de tamaño real tienen un coste fijo de envío de 45 € y Mistress se gestiona como colección.
  - **Solución nativa prevista:** crear un perfil de envío personalizado para los productos o variantes Mistress afectados y configurar en él la tarifa fija correspondiente por cada zona autorizada. La pertenencia a la colección sirve para identificar el catálogo, pero deben asignarse al perfil los productos o variantes concretos y mantener esa asignación cuando se incorporen nuevos artículos.
  - **Riesgo de pedidos mixtos:** Shopify combina las tarifas de perfiles distintos. Un carrito con una Mistress y un producto del perfil general podría mostrar 45 € más la tarifa ordinaria. No crear el perfil hasta confirmar la regla comercial deseada para esos carritos.
  - **Pendiente de Lorena o gestoría:** confirmar si los 45 € son el precio final con IVA incluido o un coste neto; si se cobran por pedido, por muñeca o por expedición; los destinos a los que se aplica; si sustituye o queda excluido del envío gratuito; y qué porte debe cobrarse al mezclar Mistress con productos normales.
  - **Estado revisado (28/07/2026):** no se creó ningún perfil ni se modificó ninguna tarifa. La siguiente pantalla será `Configuración > Envío y entrega > Perfiles de envío > Crear nuevo perfil` cuando se confirmen las reglas anteriores.
  - **Pantalla:** `Configuración > Envío y entrega > Perfiles de envío` y `Crear nuevo perfil`.

### Transportista y condiciones del servicio

- [x] Transportistas y costes orientativos recibidos, contrastados y trasladados al modelo genérico por zona.
  - **Respuesta de Lorena (27/07/2026):** GLS para envíos propios nacionales y europeos desde Amposta; NACEX, SEUR y Correos Express desde almacenes de proveedores en España; DHL, DPD y UPS para UE. La agencia depende del almacén de origen.
  - **Criterio de configuración:** no trasladar cada fila de coste ni cada agencia como una tarifa visible. Usar la tabla como base para validar los precios de venta por zona y servicio; crear tarifas diferenciadas solo cuando cambien el precio o la promesa mostrada al cliente, como Península, urgente, Baleares, grupos europeos o productos Mistress.
  - **Capturas nacionales revisadas (27/07/2026):**
    - Península 24/48 h: NACEX desde 4,06 € en oficina y 5,20 € a domicilio; Correos Express desde 4,93 € en ambas modalidades; SEUR desde 4,44 € a domicilio.
    - Península urgente: NACEX desde 15,01 € con entrega antes de las 12:00; SEUR desde 7,79 € antes de las 13:30; Correos Express desde 7,68 € antes de las 14:00. La opción SEUR antes de las 10:00 figura sin precio disponible.
    - Baleares 48–72 h: SEUR desde 7,74 € a domicilio; Correos Express desde 8,62 € en oficina o domicilio.
  - **Distinción operativa:** `En oficina` en estas capturas significa oficina o punto del transportista; no equivale a `Recogida en Lovlory` en el despacho de Amposta.
  - **Indicación adicional de Lorena (27/07/2026):** solicita crear todos los transportistas de la tabla para cubrir todas las necesidades.
  - **Hipótesis provisional aplicada (27/07/2026):** el cliente ve servicios genéricos y el almacén elige internamente NACEX, SEUR o Correos Express según disponibilidad y origen. Las tarifas actuales se han configurado siguiendo esta hipótesis.
- [ ] **Pendiente crítico independiente:** Lorena debe explicar quién elige realmente el transportista cuando intervienen varios proveedores y almacenes: si lo asigna automáticamente el proveedor o su sistema después del pedido, si lo decide Lovlory durante la preparación, o si el cliente debe poder elegir agencia/servicio en el checkout.
  - **Preguntas necesarias:** confirmar qué ocurre cuando un pedido contiene productos de distintos proveedores, si se divide en varios envíos, si se cobran o combinan varios portes, qué agencia y plazo se muestran al cliente y quién asume las diferencias de coste.
  - **Consecuencia de la respuesta:** si la elección es interna o automática, el modelo genérico actual por zona y promesa es válido. Si el cliente elige transportista, habrá que desglosar cada zona por agencia y servicio, con sus precios, plazos y condiciones. Si la selección depende del producto, proveedor o ubicación de origen, habrá que revisar perfiles de envío, ubicaciones y posible combinación de tarifas antes de considerar la configuración terminada.
  - **Estado:** no desglosar todavía las zonas ni eliminar las tarifas genéricas. Esta aclaración es bloqueante para la validación final del envío.
  - **Criterio para importes `Desde`:** no copiar el mínimo anunciado como tarifa fija. Para fijar un precio seguro se necesita, por agencia y servicio, la tabla completa para el intervalo habitual de 1–5 kg, reglas de peso volumétrico, destino/código postal, combustible, zonas remotas y demás recargos. El precio comercial se calculará sobre el coste aplicable máximo o representativo aprobado, más los conceptos que correspondan y menos la parte que Lovlory decida subvencionar; el tratamiento fiscal sigue pendiente de gestoría.
  - **Decisión para Península estándar (27/07/2026):** ofrecer entrega a domicilio y fijar provisionalmente el precio comercial en 5,20 €, tomando como referencia el coste más alto de las capturas para esa modalidad, NACEX desde 5,20 € sin IVA. No ofrecer por ahora `En oficina` del transportista.
  - **Aplicación en Shopify:** se editó la tarifa estándar existente, sin crear otra opción solapada. Quedó guardada en `España peninsular` por 5,20 €, de 0,00 € a 49,99 € y con 2–5 días hábiles.
  - **Modelo provisional sin aplicaciones:** mostrar al cliente nombres genéricos por promesa (`Estándar`, `Urgente`, `Baleares`) y elegir internamente la agencia disponible, sujeto a la aclaración crítica anterior.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas y tarifas` y `Cuentas de empresas de transporte`.
- [x] Modelo de tarifas definido: tarifas comerciales planas y genéricas, sin aplicación de pago ni cálculo en tiempo real.
  - **Valor actual:** no hay ninguna cuenta de empresa de transporte conectada.
  - **Decisión provisional (27/07/2026):** usar tarifas comerciales planas y genéricas en Shopify; no instalar una aplicación de pago ni conectar tarifas calculadas en esta fase.
  - **Pantalla revisada (28/07/2026):** `Configuración > Envío y entrega > Gestionar empresas de transporte preferidas`. Shopify indica expresamente que Correos, SEUR y DHL Express Spain solo se recomiendan al comprar etiquetas de envío y que estas preferencias no influyen en las tarifas de la pantalla de pago.
  - **Decisión:** no marcar ninguna empresa en esta pantalla por ahora. Esta configuración no permite que el cliente elija NACEX, SEUR o Correos Express ni asigna automáticamente una agencia según zona, producto, proveedor o almacén. Solo se configurará más adelante si Lovlory compra etiquetas directamente en Shopify y confirma qué empresas desea priorizar.
  - **Dependencia registrada:** si Lorena indica que el cliente debe elegir agencia, este punto deberá reabrirse y habrá que crear tarifas separadas por transportista y zona. Mientras la elección sea interna o automática, la configuración actual queda aprobada.
  - **Pantallas:** `Configuración > Envío y entrega > Cuentas de empresas de transporte` y `Gestionar empresas de transporte preferidas`.
- [ ] **Único punto pendiente para cerrar la revisión funcional — Validación final conjunta de Lorena:** revisar en una sola comprobación las zonas, servicios visibles, importes finales, umbrales gratuitos y plazos; confirmar el flujo de elección/asignación de transportista y los pedidos con varios proveedores; validar la regla definitiva de Mistress; confirmar justificante/firma; y aprobar el criterio comercial para incidencias de entrega. Las cuestiones fiscales, aduaneras, de catálogo y legales se validarán en sus apartados específicos.
- [x] Seguimiento y seguro confirmados para todos los envíos.
  - **Respuesta de Lorena (27/07/2026):** todos los envíos deben incluir seguimiento y seguro; espera justificante de entrega.
- [ ] Confirmar si el justificante de entrega debe incluir firma y cuál es la modalidad exacta.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Editar opción de envío > Detalles de entrega`.
- [ ] Confirmar los costes y el procedimiento para dirección incorrecta, ausencia, reexpedición, paquete rechazado, pérdida o daño.
  - **Pantalla relacionada:** `Configuración > Políticas` y `Configuración > Envío y entrega > Plantillas`.

### Paquetes y pesos

- [x] Paquetes habituales revisados para la configuración actual.
  - **Valor actual revisado (28/07/2026):** Shopify muestra una única `Caja de muestra`, establecida como predeterminada de la tienda, con medidas 22 × 13,7 × 4,2 cm y peso del embalaje de 0 kg. No coincide con ninguna de las dos medidas facilitadas por Lorena.
  - **Respuesta de Lorena (27/07/2026):** caja grande de 40 × 30 × 15 cm con unos 3 kg de media y caja pequeña de 20 × 10 × 10 cm con 1 kg.
  - **Criterio revisado (28/07/2026):** las tarifas actuales del checkout son planas o dependen del importe del pedido, por lo que estas medidas y pesos no intervienen ahora en el precio mostrado al cliente. Sí son relevantes para etiquetas, tarifas calculadas futuras y control logístico.
  - **Decisión aprobada (28/07/2026):** mantener la `Caja de muestra` sin cambios y conservar las medidas y pesos medios facilitados únicamente como referencia documental. No introducir 1 kg ni 3 kg como tara porque parecen corresponder al paquete completo.
  - **Estado:** punto completado para el modelo actual de tarifas. Solo se reabrirá si Lovlory compra etiquetas o activa tarifas calculadas en Shopify; en ese caso habrá que sustituir la caja de muestra por los dos embalajes reales y obtener su peso en vacío.
  - **Pantalla:** `Configuración > Envío y entrega > Paquetes`.
- [x] No crear sobres, cajas adicionales ni embalajes especiales en Shopify para el lanzamiento.
  - **Decisión (28/07/2026):** la configuración actual no los necesita porque el checkout no calcula las tarifas por peso, dimensiones o tipo de paquete. Se mantienen únicamente las dos referencias logísticas facilitadas por Lorena.
  - **Pantalla revisada:** `Configuración > Envío y entrega > Paquetes`.
- [x] Embalaje discreto confirmado: sin logotipos ni referencias al contenido.
  - **Pantalla relacionada:** `Configuración > Envío y entrega > Documentos > Nombre del remitente en las etiquetas de envío` y configuración de plantillas/etiquetas.
- [ ] **Único pendiente del bloque:** confirmar que todos los productos físicos tienen su peso real en la variante. No incluir el peso medio del pedido ni la tara de la caja dentro del peso del producto. La tara solo se solicitará si posteriormente se utilizan etiquetas o tarifas calculadas en Shopify.
  - **Pantalla:** `Productos > Variante > Envío > Peso`.

### Entrega, recogida y documentación

- [x] Recogida en el despacho resuelta para el alcance actual sin activar formas de entrega adicionales.
  - **Valor actual revisado (28/07/2026):** `Entrega local`, `Retiro en tienda` y `Puntos de retiro` permanecen desactivados. La pantalla `Entrega local` muestra una única sucursal en Amposta con el estado `No ofrece entrega`.
  - **Respuesta de Lorena (27/07/2026):** para Terres de l’Ebre quiere entrega urgente, entrega normal y una modalidad de “momentos especiales”; esta última requiere definir el servicio y su contenido antes de configurarla como forma de entrega.
  - **Recogida resuelta:** mantener desactivado `Retiro en tienda` porque la recogida de Amposta ya está implementada mediante las tarifas del perfil general: 3,95 € por debajo de 100 € y gratuita desde 100 €. Mantener también `Puntos de retiro` desactivado.
  - **Decisión de cierre (28/07/2026):** dar el punto por completado mediante la recogida configurada en el perfil general. No activar `Entrega local` para el lanzamiento. Si posteriormente Lorena desea ofrecer reparto en Terres de l’Ebre, se tratará como una ampliación independiente y habrá que definir previamente su área, modalidades, precios y plazos.
  - **Pantallas revisadas:** `Configuración > Envío y entrega > Formas de entrega adicionales` y `Entrega local`.
  - **Estado de la comprobación:** punto completado sin abrir la ficha de la sucursal ni realizar cambios adicionales.
- [x] Nombre discreto del remitente validado.
  - **Estado revisado (28/07/2026):** el cuadro `Personaliza el nombre del remitente en las etiquetas de envío` tiene seleccionada la opción `Lovlory`. La alternativa `Nombre personalizado` está vacía y admite un máximo de 25 caracteres.
  - **Decisión aprobada (28/07/2026):** se valida `Lovlory` como nombre suficientemente discreto para aparecer como remitente en las etiquetas de envío.
  - **Pantalla revisada:** `Configuración > Envío y entrega > Documentos > Nombre del remitente en las etiquetas de envío`.
  - **Estado de la comprobación:** punto completado sin cambios; no fue necesario pulsar `Guardar` porque `Lovlory` ya estaba seleccionado.
- [ ] Confirmar qué datos deben aparecer en la nota de entrega, factura y lista de picking, evitando contenido sensible innecesario.
  - **Pantalla:** `Configuración > Envío y entrega > Documentos > Plantillas`.
- [~] Criterio operativo de devoluciones recibido, pendiente de validación legal y de aclarar quién asume el coste.
  - **Respuesta de Lorena (27/07/2026):** solo contempla devoluciones en casos específicos de defecto o tara y señala que “el remitente” asume el coste en devoluciones puntuales.
  - **Pendiente:** pedir a la asesoría el texto definitivo, concretar el sujeto que paga el porte y no configurar reglas automáticas hasta aprobarlo.
  - **Pantalla:** `Configuración > Políticas > Política de devoluciones` y configuración operativa de devoluciones.

## Pagos

> La clienta ha autorizado configurar conjuntamente PayPal y Shopify Payments. La autorización no sustituye la validación de compatibilidad del catálogo ni permite completar accesos, verificaciones o datos financieros sin su intervención.

### Decisión general y elegibilidad

- [x] Confirmar quién completará la configuración y qué opciones desea mantener.
  - **Respuesta de Lorena (28/07/2026):** la configuración se hará conjuntamente; PayPal será la opción principal y quiere intentar activar también Shopify Payments.
  - **Estado revisado (28/07/2026):** Shopify Payments continúa pendiente de completar; PayPal aparece con configuración incompleta y no se observa otro proveedor activo.
  - **Pantalla:** `Configuración > Pagos`.
- [ ] Solicitar al cliente que confirme por escrito con Shopify si Shopify Payments acepta el catálogo concreto de LovLory, descrito como venta de juguetes sexuales físicos y productos de bienestar íntimo.
  - **Autorización recibida (28/07/2026):** Lorena solicita que realicemos la consulta con Shopify.
  - **Pendiente:** obtener la confirmación expresa de elegibilidad antes de completar el alta.
  - **Motivo:** Shopify exige revisar la elegibilidad y sus categorías no son exhaustivas; no debemos completar el alta basándonos únicamente en que el botón esté disponible.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Más información / Completar configuración` y soporte de Shopify.
- [x] Confirmar si el cliente quiere intentar usar Shopify Payments en caso de aprobación o si prefiere operar inicialmente solo con PayPal.
  - **Decisión de Lorena (28/07/2026):** PayPal será la opción principal y se intentará activar también Shopify Payments si Shopify confirma la elegibilidad.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments`.
- [ ] Si Shopify Payments no acepta la actividad, confirmar qué proveedor alternativo compatible con el catálogo se utilizará para permitir pagos con tarjeta sin depender únicamente de PayPal.
  - **Antecedente comunicado (28/07/2026):** Stripe retiró o denegó la pasarela por el tipo de actividad.
  - **Interés de la clienta:** valorar Google Pay. No debe tratarse como proveedor alternativo independiente hasta comprobar qué proveedor compatible lo ofrecería; normalmente se habilitaría a través del proveedor principal.
  - **Pantalla:** `Configuración > Pagos > Ver todos los demás proveedores` y `Agregar proveedor`.

### Shopify Payments: datos necesarios solo si se aprueba

- [x] Confirmar la condición de autónoma/persona física y que la titular reside en España.
  - **Configuración registrada (28/07/2026):** en el paso 1 de 4 del alta de Shopify Payments se seleccionó y envió `Persona física / Comerciante único`, con España como país de la entidad.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Tipo de empresa`.
- [ ] Facilitar los datos de identidad y negocio que solicite la verificación: nombre legal completo, segundo apellido, fecha de nacimiento, NIF/NIE, domicilio y documentación acreditativa. Reutilizar los datos ya solicitados en Información comercial y no guardar documentos sensibles en el repositorio.
  - **Avance registrado (28/07/2026):** se completó y envió el paso 2 de 4 con los datos del representante de la cuenta, incluidos DNI y dirección de residencia. En el paso 3 se declaró que no se dispone de número de IVA y que los servicios de Shopify se adquieren con fines comerciales.
  - **Último paso revisado:** Shopify solicita subir un documento de identidad y un documento acreditativo de la dirección residencial antes de `Enviar para verificación`.
  - **Pendiente:** Lorena debe revisar los datos mostrados y cargar personalmente ambos documentos; no se han subido ni enviado para verificación.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Información personal y comercial`.
- [ ] Facilitar una cuenta bancaria en euros compatible con transferencias SEPA, confirmar el IBAN y el nombre exacto de su titular. Transmitir estos datos por un canal seguro, no por este documento.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Cuenta bancaria para pagos`.
- [ ] Confirmar el correo y teléfono que deben usarse para avisos de verificación, pagos, incidencias y contracargos.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Gestionar > Notificaciones y datos de la cuenta`.
- [ ] Confirmar el descriptor reconocible y discreto que debe aparecer en el extracto bancario del comprador.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Gestionar > Descriptor del extracto`.
- [ ] Revisar y aprobar las comisiones reales del plan, el calendario de liquidaciones, las reservas o retenciones y el procedimiento de contracargos antes de activar el proveedor.
  - **Valor mostrado actualmente:** tarifas de tarjeta anunciadas desde 2,1 % + 0,30 €; el coste definitivo debe verificarse para el plan y la cuenta de la tienda.
  - **Bloqueo observado (28/07/2026):** Shopify solicita configurar la autenticación en dos pasos antes de agregar una cuenta bancaria.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Más información / Gestionar` y condiciones del proveedor.

### PayPal

- [x] Confirmar que la cuenta PayPal usada actualmente en WordPress pertenece a la autónoma, es una cuenta Business española, está verificada y no tiene limitaciones.
  - **Confirmación de Lorena (28/07/2026):** responde afirmativamente a todos estos puntos. La comprobación dentro de PayPal se realizará durante la conexión.
  - **Pantalla:** `Configuración > Pagos > Proveedores de pagos adicionales > PayPal > Configuración incompleta` y cuenta de PayPal.
- [ ] Solicitar el correo exacto de la cuenta PayPal Business que debe conectarse y comprobar que coincide con una dirección verificada dentro de PayPal.
  - **Respuesta de Lorena (28/07/2026):** indica que el dato debe estar en el sitio web anterior y propone confirmarlo durante la configuración.
  - **Pendiente:** identificar y validar el correo exacto antes de conectar la cuenta.
  - **Seguridad:** no solicitar ni guardar la contraseña ni códigos de doble autenticación; la propietaria de la tienda debe completar personalmente el acceso y la autorización.
  - **Pantalla:** `Configuración > Pagos > PayPal > Completar configuración`.
- [ ] Confirmar con PayPal que la cuenta puede procesar en Shopify el catálogo completo de LovLory y que el cambio desde WordPress no requiere una nueva revisión o autorización.
  - **Respuesta de Lorena (28/07/2026):** desconoce si PayPal ha confirmado esta compatibilidad.
  - **Motivo:** que PayPal funcione actualmente en WordPress no garantiza por sí solo la aceptación de la nueva integración, del dominio o de todo el catálogo.
  - **Pantalla relacionada:** cuenta PayPal Business, centro de resoluciones y soporte de PayPal.
- [ ] Confirmar la cuenta bancaria de retirada, la divisa principal EUR, el nombre legal del titular y el país España.
  - **Pantalla:** cuenta PayPal Business y `Configuración > Pagos > PayPal`.
- [ ] Confirmar las comisiones vigentes de PayPal y aceptar el coste adicional de Shopify si no se usa Shopify Payments.
  - **Valor mostrado actualmente:** Shopify indica un 2 % de cargo por transacción de terceros, además de las comisiones de procesamiento de PayPal.
  - **Pantalla:** `Configuración > Pagos > Proveedores de pagos adicionales > PayPal`.
- [x] Confirmar si PayPal debe permitir el pago con tarjeta como invitado, cuando esté disponible, para compradores que no tengan cuenta PayPal.
  - **Decisión de Lorena (28/07/2026):** sí debe permitirse.
  - **Comprobación pendiente:** validar su disponibilidad en la cuenta PayPal Business y mediante una prueba del checkout después de conectar PayPal.
  - **Pantalla relacionada:** preferencias de pago de la cuenta PayPal Business y prueba del checkout de Shopify.
- [ ] Tras conectar PayPal, realizar una compra de prueba con una cuenta PayPal distinta de la cuenta receptora y comprobar cobro, cancelación, reembolso total y reembolso parcial.
  - **Pantalla:** tienda online, `Pedidos` y `Configuración > Pagos > PayPal`.

### Funcionamiento de los cobros

- [x] Mantener la captura automática del pago al realizar el pedido.
  - **Decisión de Lorena (28/07/2026):** confirma el cobro automático en el momento de la compra.
  - **Comprobación en Shopify (28/07/2026):** `Automáticamente en la pantalla de pago` ya estaba seleccionado; se mantuvo sin cambios.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Método de captura de pago`.
- [x] Confirmar qué formas de pago manuales se aceptarán.
  - **Decisión de Lorena (28/07/2026):** aceptar Bizum y transferencia bancaria; no aceptar contra reembolso.
- [ ] Definir y activar Bizum y transferencia bancaria.
  - **Estado revisado (28/07/2026):** no hay ninguna forma de pago manual activa.
  - **Datos pendientes para Bizum:** identificador o teléfono de cobro, texto visible en el checkout, instrucciones posteriores al pedido, plazo de pago, reserva de stock y criterio para marcar el pedido como pagado.
  - **Datos pendientes para transferencia:** titular, IBAN por canal seguro, concepto que debe indicar el cliente, instrucciones posteriores al pedido, plazo de pago, reserva de stock y criterio para marcar el pedido como pagado.
  - **Acción realizada:** se revisaron los formularios `Crear forma de pago personalizada` y `Depósito bancario`; no se activaron para evitar publicar instrucciones incompletas.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Formas de pago manuales`.
- [ ] Revisar si existe alguna personalización de formas de pago creada por una aplicación y confirmar si debe conservarse.
  - **Valor actual:** no existe ninguna personalización de pago; Shopify muestra `Aún no has personalizado las formas de pago`.
  - **Criterio:** no instalar ninguna aplicación de personalización salvo que aparezca una necesidad comercial concreta.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Personalizaciones de las formas de pago`.
- [x] Confirmar si LovLory venderá tarjetas de regalo.
  - **Decisión de Lorena (28/07/2026):** sí venderá tarjetas de regalo.
- [ ] Decidir el vencimiento de las tarjetas de regalo y si se habilitarán pases de Apple Wallet.
  - **Estado revisado (28/07/2026):** las tarjetas de regalo están configuradas para no caducar y los pases de Apple Wallet están desactivados.
  - **Pendiente:** confirmar si se mantienen ambos valores.
  - **Aclaración:** `Pases de Apple Wallet` corresponde a tarjetas de regalo y no es la configuración de Apple Pay.
  - **Pantalla:** `Configuración > Pagos > Vencimiento de la tarjeta de regalo` y `Pases de Apple Wallet`.
- [ ] Realizar antes del lanzamiento pruebas de pago aceptado, pago rechazado, 3D Secure si corresponde, devolución, cancelación y recepción de una liquidación real pequeña.
  - **Pantalla:** checkout de prueba, `Pedidos` y panel del proveedor de pagos.

## Cuentas de cliente

- [ ] Confirmar si se mantendrán visibles los enlaces para que los clientes accedan a su cuenta desde la cabecera y el pago.
  - **Valor actual:** `Mostrar enlaces de inicio de sesión` está activado.
  - **Recomendación:** mantenerlo activado para que el cliente pueda consultar pedidos, direcciones y estado de sus compras; esto no obliga a crear una cuenta para comprar.
  - **Pantalla:** `Configuración > Cuentas de cliente > Enlaces de inicio de sesión`.
- [ ] Revisar los métodos de autenticación disponibles y confirmar si se mantendrá el acceso sin contraseña mediante código enviado por correo electrónico.
  - **Valor actual:** inicio de sesión con `Shop` activado; conexiones con Google y Facebook disponibles pero no configuradas.
  - **Decisión técnica propuesta:** mantener Shop activo y no conectar Google ni Facebook mientras no exista una necesidad concreta y las cuentas necesarias.
  - **Pantalla:** `Configuración > Cuentas de cliente > Autenticación > Gestionar`.
- [ ] Confirmar si se desea añadir inicio de sesión con Shop, Google o Facebook. No configurarlo sin las cuentas y autorizaciones correspondientes.
  - **Pantalla:** `Configuración > Cuentas de cliente > Autenticación > Gestionar`.
- [x] Configurar y establecer como principal el subdominio de cuentas de cliente: `cuenta.lovlory.com`.
  - **URL anterior:** `https://shopify.com/95651430743/account`.
  - **Estado final:** `cuenta.lovlory.com` aparece conectado y se ha establecido como dominio principal para las cuentas de cliente.
  - **Comprobación final:** probar el inicio de sesión y el acceso a pedidos durante las pruebas finales; no requiere información adicional del cliente.
  - **Pantalla:** `Configuración > Cuentas de cliente > URL > Cambiar dominio`.
- [ ] Confirmar si se habilitarán devoluciones y cancelaciones de autoservicio.
  - **Valor actual:** desactivadas.
  - **Condición previa:** no activarlas hasta aprobar la política, las reglas de devolución, el plazo, los artículos no retornables por higiene, los costes y las instrucciones.
  - **Pantalla:** `Configuración > Cuentas de cliente > Devoluciones y cancelaciones de autoservicio` y `Configuración > Políticas / Reglas de devolución y cancelación`.
- [x] Confirmar si LovLory utilizará crédito en tienda para reembolsos, fidelización o compensaciones.
  - **Decisión de Lorena (28/07/2026):** confirma que utilizará esta opción.
  - **Comprobación en Shopify (28/07/2026):** `Permite que los clientes vean y gasten el crédito en tienda` está activado; se mantuvo sin cambios.
  - **Pendiente operativo:** revisar la política de emisión, vencimiento, contabilidad, reembolsos y posibles cargos por transacción antes de emitir saldos.
  - **Pantalla:** `Configuración > Cuentas de cliente > Crédito en tienda` y `Clientes > Perfil del cliente > Crédito en tienda`.
- [ ] Confirmar si se personalizarán las cuentas de cliente ahora o después de cerrar el diseño del checkout y la identidad visual.
  - **Pantalla:** `Configuración > Cuentas de cliente > Personalización > Personalizar`.

## Pantalla de pago

- [x] Mantener el correo electrónico como método de contacto obligatorio.
  - **Valor actual:** `Correo electrónico` seleccionado.
  - **Pantalla:** `Configuración > Pago > Método de contacto del cliente`.
- [ ] Confirmar si se mantendrá el enlace para realizar el seguimiento mediante la aplicación Shop, teniendo en cuenta la discreción y privacidad deseadas.
  - **Valor actual:** activado.
  - **Pantalla:** `Configuración > Pago > Método de contacto del cliente > Seguimiento con Shop`.
- [x] Mantener la compra como invitado, sin obligar a iniciar sesión antes del pago.
  - **Valor actual:** `Requerir que los clientes inicien sesión` desactivado.
  - **Pantalla:** `Configuración > Pago > Método de contacto del cliente`.
- [x] Mantener nombre y apellidos obligatorios y la segunda línea de dirección opcional.
  - **Pantalla:** `Configuración > Pago > Información del cliente`.
- [ ] Confirmar si el transportista exige teléfono para la entrega; hasta entonces, mantener el teléfono de envío como opcional.
  - **Valor actual:** opcional.
  - **Pantalla:** `Configuración > Pago > Información del cliente > Teléfono de la dirección de envío`.
- [ ] Confirmar si el lanzamiento será exclusivamente B2C. Hasta recibir respuesta, mantener ocultos el nombre de empresa y el número de IVA de empresa.
  - **Valor actual:** ambos campos configurados como `No incluir`.
  - **Pantalla:** `Configuración > Pago > Información del cliente`.
- [x] Mantener ocultas las casillas de marketing por correo y SMS hasta disponer de la estrategia y los textos de consentimiento aprobados.
  - **Valor actual:** `No mostrar` en ambos canales.
  - **Pantalla:** `Configuración > Pago > Suscripción a marketing`.
- [ ] Confirmar el idioma o idiomas del checkout y la tienda: español únicamente o también catalán.
  - **Valor actual:** español.
  - **Pantalla:** `Configuración > Pago > Idioma de la pantalla de pago` y `Configuración > Idiomas`.
- [x] Desactivar las propinas en el checkout.
  - **Estado final:** desactivadas el 21 de julio de 2026; no se mostrarán al cliente.
  - **Pantalla:** `Configuración > Pago > Propinas`.
- [x] Mantener activado el límite recomendado de artículos en el carrito para proteger el inventario.
  - **Pantalla:** `Configuración > Pago > Preferencias avanzadas > Límite de agregar al carrito`.
- [x] Confirmar que no existen aplicaciones con reglas de carrito o pago.
  - **Valor actual:** ninguna aplicación instalada.
  - **Pantalla:** `Configuración > Pago > Reglas de pago`.
- [x] Revisar la recopilación de direcciones.
  - **Valor aprobado:** permitir direcciones de envío y facturación diferentes; usar la dirección de envío como dirección de facturación predeterminada; validar la dirección de envío.
  - **Pantalla:** `Configuración > Pago > Recopilación de direcciones`.
- [ ] Revisar la configuración visual activa antes de cerrar este bloque.
  - **Valor actual:** configuración activa `Configuración 2 de Lovlory`; existe además el borrador `Configuración de Mi tienda`.
  - **Vista observada:** checkout en español, diseño blanco con botones y enlaces azules, nombre `Lovlory` mostrado como texto y sin logotipo visible. En el pie solo aparecen por ahora los enlaces de privacidad y cookies.
  - **Aclaración:** el producto, la dirección, la tarifa de envío de 10 € y PayPal mostrados en el editor son datos de ejemplo y no validan la configuración real.
  - **Pendiente:** revisar los controles de marca del editor y añadir el resto de políticas cuando Lorena entregue los textos definitivos.
  - **Pantalla:** `Configuración > Pago > Configuraciones > Configuración 2 de Lovlory > Editar`.

## Páginas y textos legales

> **Responsabilidad acordada:** LovLory debe entregar los textos legales definitivos, preparados o validados por su asesoría. Nuestro trabajo se limita a incorporarlos, enlazarlos y comprobar su presentación en Shopify; no redactaremos ni adaptaremos el contenido jurídico.

- [ ] Solicitar el aviso legal definitivo.
- [ ] Solicitar las condiciones generales de compra definitivas.
- [ ] Solicitar la política de envíos definitiva, coherente con las zonas, precios y plazos aprobados.
- [ ] Solicitar la política de devoluciones, cancelaciones y reembolsos definitiva, incluyendo las condiciones aplicables a productos precintados por higiene.
- [ ] Solicitar la política de privacidad definitiva.
- [ ] Solicitar la política de cookies definitiva y las categorías de consentimiento que indique la asesoría.
- [ ] Solicitar la información de contacto, atención y reclamaciones que debe publicarse.
- [ ] Solicitar los textos aprobados sobre garantías, conformidad, seguridad, fabricante/importador y, si corresponde, mayoría de edad.
- [ ] Pedir los documentos en un formato editable o que permita copiar el texto sin errores, indicando fecha y versión aprobada.
  - **Pantalla de destino:** `Configuración > Políticas`, páginas de la tienda, pie de página y checkout.

## Estado

Última actualización: 28 de julio de 2026.
