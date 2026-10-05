# Plan maestro de configuración Shopify — LovLory

**Versión:** 1.0  
**Fecha de referencia:** 21 de julio de 2026  
**Ámbito:** configuración general, fiscal, operativa y de lanzamiento de la tienda Shopify de LovLory  
**Estado global:** `[~] En curso`

> Este documento es la lista de control compartida del proyecto. Se irá actualizando a medida que se tomen decisiones, se apliquen ajustes y se verifiquen mediante pedidos de prueba. La configuración fiscal y legal debe validarse con la gestoría o asesoría de LovLory.

## Cómo utilizar este documento

- `[ ]` Pendiente.
- `[~]` En curso.
- `[x]` Terminado y verificado.
- `[!]` Bloqueado o requiere una decisión.
- No marcar una tarea como terminada hasta guardar una evidencia: captura, URL, número de pedido de prueba o nota de validación.
- Registrar cambios importantes en el apartado **Registro de decisiones**.
- Revisar primero los bloques 0–8. Los bloques 9–15 completan la preparación para el lanzamiento.

## Panel de avance

| Bloque | Área | Estado | Responsable | Evidencia / fecha |
|---|---|---|---|---|
| 0 | Decisiones previas | En curso | Por asignar | Información comercial pendiente |
| 1 | Seguridad, empresa y facturación | Pendiente | Por asignar | — |
| 2 | Datos generales | En curso | Por asignar | Revisión de Configuración > General, 21/07/2026 |
| 3 | Mercados, moneda e idiomas | En curso | Por asignar | Mercado España revisado, 21/07/2026 |
| 4 | Impuestos | En curso | Por asignar | Pantalla Unión Europea revisada; registro español pendiente de gestoría, 27/07/2026 |
| 5 | Pagos | En curso | Por asignar | Pantalla revisada; proveedores sin validar, 21/07/2026 |
| 6 | Ubicaciones e inventario | En curso | Por asignar | Sucursal predeterminada de Amposta revisada sin cambios, 27/07/2026 |
| 7 | Transporte y preparación | En curso | Por asignar | Fechas globales desactivadas; plazos por tarifa pendientes, 27/07/2026 |
| 8 | Checkout y cuentas de cliente | En curso | Por asignar | Cuentas de cliente revisadas, 21/07/2026 |
| 9 | Políticas, privacidad y cumplimiento | Pendiente | Por asignar | — |
| 10 | Dominio, correo y notificaciones | Pendiente | Por asignar | — |
| 11 | Catálogo y colecciones | En curso | Por asignar | Artefactos de migración existentes |
| 12 | Analítica y canales | Pendiente | Por asignar | — |
| 13 | Pruebas de aceptación | Pendiente | Por asignar | — |
| 14 | Lanzamiento | Pendiente | Por asignar | — |
| 15 | Seguimiento posterior | Pendiente | Por asignar | — |

---

## 0. Decisiones previas

No configurar impuestos, pagos o portes definitivos hasta completar estas decisiones.

- [ ] **CFG-001 — Confirmar titular de la tienda.** Razón social o nombre del autónomo, NIF/CIF, domicilio fiscal y teléfono.
  - Terminado cuando: los datos coinciden con la documentación fiscal y bancaria.
  - Evidencia: ________________________________________________
- [ ] **CFG-002 — Confirmar URL de administración.** Guardar la dirección `nombre-tienda.myshopify.com`.
  - Valor: ________________________________________________
- [~] **CFG-003 — Confirmar origen de los envíos.** Amposta está confirmada como origen de los pedidos propios; otros pedidos salen por dropshipping desde almacenes de proveedores. Falta revisar la dirección normalizada en Shopify y definir si los proveedores deben representarse como ubicaciones.
  - Valor profesional registrado: Sant Cristòfol 117, despacho/puerta 10, 43870 Amposta (sin almacenar direcciones residenciales ni direcciones completas de proveedores).
- [~] **CFG-004 — Definir alcance geográfico de lanzamiento.** Lorena prevé vender en España peninsular y Baleares, excluyendo Canarias, Ceuta y Melilla, y también en el resto de Europa excepto Reino Unido. Falta concretar los países europeos y validar para cada uno fiscalidad, OSS, transporte y mercado antes de activarlo.
  - Decisión provisional: Península, Baleares y UE por concretar; fuera Canarias, Ceuta, Melilla y Reino Unido.
- [~] **CFG-005 — Confirmar transportista y tarifas contratadas.** Lorena identifica GLS para expediciones propias; NACEX, SEUR y Correos Express para almacenes de proveedores en España; DHL, DPD y UPS para UE, y solicita crear todos los transportistas para cubrir las necesidades. Falta aclarar si se refiere a opciones elegibles por el cliente o a alternativas operativas por almacén. La tabla recibida contiene costes orientativos de compra, expresados sin IVA y con importes `Desde`; esos mínimos no deben copiarse como precios fijos. Se necesita el coste completo para 1–5 kg, peso volumétrico y recargos, además de contrato vigente, asignación por origen y costes de incidencias/devoluciones.
- [~] **CFG-006 — Definir umbral de envío gratuito.** Lorena aprueba 50 € para pedidos nacionales y 150 € para UE. Falta comprobar margen, configurar territorios por separado y validar el resultado en checkout.
- [~] **CFG-007 — Confirmar régimen de IVA y registro OSS con la gestoría.** Lorena confirma alta en ROI y presencia en VIES. El estado de OSS está consultado con la gestoría y, si no consta el alta, ha solicitado su tramitación.
  - Conclusión pendiente: formato exacto del número de IVA, prefijo `ES`, OSS y clasificación fiscal final del catálogo.
- [ ] **CFG-008 — Confirmar procesadores de pago compatibles con el catálogo.** Indicar expresamente que se venden juguetes sexuales físicos, no contenido o servicios sexuales.
  - Proveedor principal: ____________________  Alternativo: ____________________
- [ ] **CFG-009 — Definir política comercial de devoluciones.** Plazo, costes, productos precintados y condiciones de higiene.
  - Decisión: ________________________________________________
- [~] **CFG-010 — Definir plazo real de preparación.** El 27/07/2026 se decidió tratar estándar nacional `2–5 días hábiles`, urgente `1–2 días hábiles` y UE `3–7 días hábiles` como plazos totales visibles por tarifa, sin suma global de preparación. Como cuestión operativa separada, falta confirmar sábados, pedidos posteriores a los cortes de las 16:00/14:00 y el tiempo interno real de preparación por origen.

## 1. Seguridad, empresa y facturación

- [ ] **SEC-001 — Activar autenticación en dos pasos** para todas las cuentas con acceso al panel.
- [ ] **SEC-002 — Revisar usuarios y permisos.** Dar a cada persona solo el acceso necesario y evitar cuentas compartidas.
- [ ] **SEC-003 — Designar propietario y contacto de emergencia** de la tienda.
- [ ] **SEC-004 — Guardar métodos de recuperación** y códigos de respaldo en un lugar seguro.
- [ ] **SEC-005 — Configurar datos de facturación de Shopify** y comprobar el método de pago de la suscripción.
- [ ] **SEC-006 — Revisar el plan contratado** y confirmar que cubre informes, usuarios y funciones de transporte necesarias.
- [ ] **SEC-007 — Registrar aplicaciones instaladas, coste, responsable y permisos.** Eliminar aplicaciones de prueba que no se utilicen.
- [ ] **SEC-008 — Definir rutina de revisión de accesos** mensual durante el lanzamiento y trimestral después.

**Criterio de cierre del bloque:** acceso protegido, usuarios identificados, facturación operativa y ninguna aplicación desconocida.

## 2. Datos generales de la tienda

Ruta orientativa: **Configuración > General**.

- [ ] **GEN-001 — Nombre visible:** LovLory.
- [!] **GEN-002 — Titular, NIF y dirección:** persona física/autónoma, nombre, apellidos y fecha de nacimiento cumplimentados. Sant Cristòfol 117 está confirmado únicamente como domicilio profesional; falta obtener y cargar por canal seguro la dirección residencial particular. También queda pendiente validar el NIF en los apartados fiscal y de pagos.
- [x] **GEN-003 — Zona horaria:** `(GMT+01:00) Madrid`.
- [x] **GEN-004 — Unidades:** sistema métrico; peso predeterminado en gramos (g).
- [x] **GEN-005 — Moneda de la tienda:** EUR; región de copia de seguridad: España.
- [x] **GEN-006 — Correo de contacto:** datos de contacto de la tienda revisados y confirmados.
- [ ] **GEN-007 — Correo del remitente:** autenticarlo para reducir entregas en spam.
- [x] **GEN-008 — Formato de número de pedido:** prefijo `LV-`, sufijo vacío; resultado `LV-1001`.
- [x] **GEN-009 — Datos de contacto para clientes:** sección revisada y confirmada.
- [ ] **GEN-010 — Revisar favicon, logotipo y nombre del remitente** en todos los puntos visibles.
- [x] **GEN-011 — Paso de confirmación antes del pago:** activado para que el cliente revise el pedido antes de confirmar la compra.
- [x] **GEN-012 — Preparación de pedidos físicos:** manual; no preparar automáticamente ninguna línea de artículo.
- [x] **GEN-013 — Archivado automático:** activado para pedidos preparados y pagados o totalmente reembolsados.

**Criterio de cierre del bloque:** los datos mostrados, fiscales, bancarios y de contacto no se contradicen.

## 3. Mercados, moneda e idiomas

Ruta orientativa: **Mercados**.

### 3.1 Mercado de lanzamiento

- [x] **MKT-001 — Crear o revisar el mercado España.** Mercado activo e incluye únicamente España; verificado el 21/07/2026.
- [x] **MKT-002 — Establecer EUR** como moneda del mercado español. Heredado de los valores predeterminados de la tienda.
- [x] **MKT-003 — Activar español** como idioma principal y revisar que tema, checkout y políticas estén traducidos. Dominio `lovlory.com` e idioma español asignados; queda pendiente la revisión completa de textos.
- [x] **MKT-004 — Confirmar disponibilidad del catálogo** para el mercado español. Configurado como `Todos los productos`.
- [~] **MKT-005 — Verificar que cada país activo tenga una zona de envío válida.** España muestra cuatro tarifas; falta revisar destinos, importes, condiciones y exclusiones territoriales.

### 3.2 Territorios con tratamiento específico

- [ ] **MKT-006 — Separar Canarias** de Península/Baleares hasta validar IGIC, aduanas, DUA, plazos y transportista.
- [ ] **MKT-007 — Separar Ceuta y Melilla** hasta validar IPSI, aduanas, plazos y transportista.
- [ ] **MKT-008 — Decidir si Baleares tendrá tarifa propia** según el contrato logístico.
- [ ] **MKT-009 — Probar que una dirección no cubierta recibe un mensaje correcto** y no una tarifa errónea.

### 3.3 Expansión a la Unión Europea

- [x] **MKT-010 — Mantener inactivos los países no preparados** fiscal o logísticamente. No existen otros mercados activos; las opciones de Unión Europea y Estados Unidos son solo sugerencias sin crear.
- [!] **MKT-011 — Antes de activar la UE, confirmar OSS y tributación en destino** con la gestoría. Lorena desea vender en el resto de Europa excepto Reino Unido, pero el estado de OSS sigue pendiente. Revisado el formulario de recaudación transfronteriza el 27/07/2026 sin seleccionar OSS ni registro del país de origen; no activar países mientras no se cierre la fiscalidad y la logística.
- [ ] **MKT-012 — Definir moneda por mercado.** Para la eurozona, EUR; otras monedas solo con una decisión comercial y revisión de costes de conversión.
- [ ] **MKT-013 — Definir idiomas y traducciones** antes de indexar nuevos mercados.
- [ ] **MKT-014 — Revisar precios, redondeos y margen por mercado.**
- [ ] **MKT-015 — Crear zonas y tarifas de envío correspondientes** antes de activar cada mercado.

**Criterio de cierre del bloque:** solo pueden comprar clientes de territorios preparados, con moneda, idioma, impuestos y transporte coherentes.

## 4. Impuestos

Ruta orientativa: **Configuración > Impuestos y aranceles**.

> Validación obligatoria: Shopify ayuda a calcular impuestos, pero LovLory sigue siendo responsable de determinar, declarar y pagar los importes correctos.

- [~] **TAX-001 — Confirmar con gestoría el tipo aplicable al catálogo.** Lorena confirma precios con IVA incluido y señala que la mayoría de los productos tributan al 21 %, pero cree que existen productos de los tres tipos. Está revisando el catálogo y falta recibir la clasificación definitiva; no aplicar otros tipos por suposición.
- [!] **TAX-002 — Añadir el registro español de IVA** con el identificador real del negocio. Lorena confirma que el NIF de la actividad corresponde a su DNI, que está dada de alta en ROI y que consta en VIES; no se registra el número. Revisadas `Configuración > Impuestos y aranceles > Unión Europea` y la ventana `España > Recaudar IVA` el 27/07/2026: el formulario está vacío. Aunque Shopify enseña un ejemplo con prefijo `ES`, falta que la gestoría confirme el formato exacto y el uso del prefijo. No se introdujo ningún dato ni se pulsó `Recaudar el IVA`.
- [x] **TAX-003 — Elegir servicio fiscal.** `Servicios fiscales de Shopify / Shopify Tax` figura activo para la Unión Europea; verificado el 21/07/2026.
- [~] **TAX-004 — Configurar precios con IVA incluido** para venta B2C en España. Lorena ha confirmado que los precios incluyen IVA. Revisadas `Configuración > Impuestos y aranceles > Configuración adicional` y `Mercados > España > Impuestos y aranceles` el 27/07/2026: la casilla global de inclusión del impuesto ya está activada y el mercado España tiene seleccionada `Visualización dinámica de impuestos`; ambas se mantuvieron sin cambios. Shopify muestra `Sin recaudación` y aplica provisionalmente una tasa del 0 % al no existir todavía identificación fiscal configurada. Falta validar la presentación y el cálculo mediante un pedido de prueba tras completar el registro español.
- [!] **TAX-005 — Confirmar el tratamiento fiscal de los gastos de envío.** Revisada la configuración adicional el 27/07/2026: `Cobrar impuesto sobre las ventas en el envío` está desactivado y Shopify indica que el cálculo es automático para la Unión Europea. Lorena confirmó el 28/07/2026 que el precio cobrado al cliente debe incluir IVA y que las tablas de almacén recibidas son costes sin IVA. Los importes de pago configurados reproducen provisionalmente esas referencias netas `Desde` y deben recalcularse como precios comerciales finales antes del cierre. La gestoría debe confirmar el tipo y método aplicable al transporte; no multiplicar automáticamente por el 21 % ni modificar fiscalidad hasta recibir esa validación. Después de completar el registro fiscal, recalcular todas las tarifas de pago y ejecutar un pedido de prueba que confirme el total mostrado y el desglose interno del impuesto.
- [!] **TAX-006 — Revisar la categoría fiscal de cada producto** y evitar anulaciones globales sin justificación. Shopify Tax muestra 193 productos sin categorizar; deben clasificarse y verificarse antes de la prueba fiscal final.
- [ ] **TAX-007 — Revisar regalos, descuentos y códigos promocionales** con impuestos incluidos.
- [!] **TAX-008 — Mantener excluidas Canarias, Ceuta y Melilla** del lanzamiento según la indicación de Lorena. Verificar la exclusión efectiva en mercados y envíos; no configurar recaudación ni transporte para estos territorios.
- [!] **TAX-009 — Registrar la decisión sobre OSS.** Lorena prevé vender en otros países europeos excepto Reino Unido, pero desconoce si está inscrita en OSS y lo ha consultado con la gestoría. Revisado `Unión Europea > Recauda el IVA en ventas transfronterizas > Recaudar IVA` el 27/07/2026: Shopify ofrece OSS o registro del país de origen para microempresas que cumplan sus condiciones; ambas modalidades solicitan país y número de IVA. No se seleccionó ninguna ni se introdujeron datos. La gestoría debe indicar expresamente qué régimen corresponde; el alta en ROI/VIES no se considerará confirmación de OSS.
- [!] **TAX-010 — Configurar facturas con IVA** o la solución de facturación que utilice la empresa. Revisada `Configuración > Impuestos y aranceles > Unión Europea > Facturas con IVA` el 27/07/2026: la generación automática está desactivada y Shopify indica que no está disponible para pedidos con envío a Portugal. Lorena prefiere usar las facturas de Shopify si pueden volcarse a Odoo. Mantener la función desactivada hasta definir y probar la integración o exportación, decidir el tratamiento de Portugal y completar el registro de IVA.
- [ ] **TAX-011 — Ejecutar pedidos fiscales de prueba:** Península, Baleares y, si están activos, UE/Canarias/Ceuta/Melilla.
- [ ] **TAX-012 — Comparar el cálculo de Shopify con un cálculo manual** y obtener aprobación de la gestoría.
- [!] **TAX-013 — Definir la captura del número de IVA de clientes empresariales.** Lorena indica que la venta será mayoritariamente B2C, pero también venderá a asociaciones con NIF. Revisado el 27/07/2026: `Número de IVA de la empresa` aparece activado en la configuración de la UE, mientras que `Configuración > Pago > Información del cliente` mantiene `Nombre de la empresa` y `Número de IVA de la empresa` en `No incluir`. Conservar ambos campos ocultos hasta definir con Lorena y la gestoría el flujo de venta, validación y facturación para asociaciones.

**Criterio de cierre del bloque:** registros fiscales correctos, precios coherentes y al menos un pedido de prueba aprobado por territorio activo.

## 5. Pagos

Ruta orientativa: **Configuración > Pagos**.

### 5.1 Elegibilidad y alta

- [!] **PAY-001 — Confirmar por escrito la elegibilidad del catálogo** con Shopify Payments y PayPal. Describirlo como venta de juguetes sexuales físicos y bienestar íntimo. No basta con que PayPal funcione actualmente en WordPress.
- [ ] **PAY-002 — Evitar contenido sexual explícito, servicios sexuales y afirmaciones médicas no demostradas** en páginas revisadas por el procesador.
- [ ] **PAY-003 — Publicar contacto, entrega, devolución, desistimiento y descripciones completas** antes de solicitar o completar la revisión.
- [!] **PAY-004 — Activar Shopify Payments solo si se aprueba la actividad.** Actualmente está sin configurar y muestra la opción `Completar configuración`; no iniciar el alta hasta recibir confirmación de elegibilidad y autorización del cliente.
- [ ] **PAY-005 — Verificar identidad y empresa** con datos idénticos a la documentación oficial.
- [ ] **PAY-006 — Conectar cuenta bancaria en EUR compatible con SEPA.** No usar una cuenta de ahorro ni una cuenta multidivisa no admitida.
- [!] **PAY-007 — Definir un proveedor alternativo compatible** para reducir riesgo operativo si el principal limita la cuenta. PayPal es la opción prevista, pero su configuración está incompleta y aún debe confirmar la cuenta y el catálogo.

### 5.2 Métodos y operativa

- [ ] **PAY-008 — Activar tarjetas admitidas** y comprobar 3D Secure.
- [ ] **PAY-009 — Activar Apple Pay, Google Pay y Shop Pay** si están disponibles y aprobados.
- [!] **PAY-010 — Revisar PayPal**: titular, correo verificado, cuenta Business española, cuenta bancaria, divisa, elegibilidad del catálogo y política de protección. Solo la propietaria debe completar el acceso; no solicitar contraseñas ni códigos. La pantalla muestra configuración incompleta y un 2 % de cargo de Shopify por transacción de terceros, además de la comisión de PayPal.
- [ ] **PAY-011 — No activar Klarna u otros métodos aplazados** hasta confirmar compatibilidad con todo el catálogo y condiciones de la tienda.
- [ ] **PAY-012 — Configurar descriptor bancario reconocible** para reducir contracargos, si el proveedor lo permite.
- [~] **PAY-013 — Definir captura de pagos:** actualmente está seleccionada `Automáticamente en la pantalla de pago`, por lo que el cobro se captura al realizar el pedido. Falta confirmar si fue una decisión del cliente y si debe mantenerse con el proveedor definitivo.
- [ ] **PAY-014 — Revisar pagos, comisiones, conversión y calendario de liquidaciones.**
- [ ] **PAY-015 — Configurar alertas de fraude y revisión manual** de pedidos de riesgo alto.
- [ ] **PAY-016 — Realizar transacción de prueba, reembolso total y reembolso parcial.**
- [ ] **PAY-017 — Confirmar recepción de una liquidación real pequeña** antes del lanzamiento completo.
- [x] **PAY-018 — Revisar formas de pago manuales y personalizaciones.** No hay métodos manuales activos ni personalizaciones instaladas. Falta como decisión independiente confirmar si el cliente desea transferencia, contra reembolso u otra modalidad manual.
- [ ] **PAY-019 — Confirmar si se venderán tarjetas de regalo.** Solo entonces decidir vencimiento y pases de Apple Wallet; estos pases no corresponden a Apple Pay.
- [!] **PAY-020 — Decidir si se habilitará una forma de pago manual.** Si el cliente solicita transferencia, contra reembolso u otra modalidad, definir instrucciones, costes, reserva de stock y proceso de aprobación antes de activarla.

**Criterio de cierre del bloque:** proveedor aprobado, cobro y reembolso probados, cuenta bancaria validada y alternativa documentada.

## 6. Ubicaciones e inventario

- [x] **INV-001 — Crear la ubicación real de preparación** con dirección y nombre claros. Validada el 27/07/2026: Amposta es la sucursal predeterminada, su dirección profesional es correcta y el nombre interno se cambió de la dirección completa a `LovLory — Amposta`. La dirección no se modificó.
- [ ] **INV-002 — Desactivar ubicaciones ficticias o de prueba** que puedan recibir inventario o pedidos.
- [~] **INV-003 — Definir qué ubicación prepara pedidos online.** Revisado el 27/07/2026: la sucursal predeterminada `LovLory — Amposta` usa su inventario para preparar pedidos online y tiene el envío activado. Para los almacenes de proveedores en dropshipping no se crearán sucursales físicas ni se pedirán direcciones completas por defecto. Primero se inventariarán proveedor, SKU, método de transmisión del pedido, sincronización de stock, destinos, costes, plazos, transportista, seguimiento, seguro, devoluciones y pedidos divididos. Una aplicación podrá crear su ubicación; un proveedor sin aplicación podrá evaluarse como servicio de logística personalizado si acepta solicitudes por correo. La dirección solo se pedirá cuando sea necesaria para etiquetas, tarifas desde origen, devoluciones o una obligación confirmada.
- [ ] **INV-004 — Confirmar que cada variante controla inventario** cuando corresponda.
- [ ] **INV-005 — Importar y validar SKU** sin valores vacíos o duplicados no intencionados.
- [ ] **INV-006 — Importar stock en la ubicación correcta.**
- [ ] **INV-007 — Decidir política de venta sin stock.** Recomendación: no continuar vendiendo productos agotados salvo caso documentado.
- [ ] **INV-008 — Configurar umbral interno de stock bajo** y responsable de reposición.
- [ ] **INV-009 — Verificar inventario de una muestra y después del total del catálogo.**
- [ ] **INV-010 — Documentar cualquier stock reservado, dañado o no vendible.**

**Criterio de cierre del bloque:** todos los SKU vendibles tienen ubicación, cantidad y política de agotado correctas.

## 7. Transporte, entrega y preparación

Ruta orientativa: **Configuración > Envío y entrega**.

> **Estado del bloque (28/07/2026): revisión funcional completada.** Todas las pantallas del bloque han sido inspeccionadas y la configuración logística actual ha quedado documentada. Resta una única puerta de aprobación comercial de Lorena, `SHP-024`. IVA/OSS, aduanas, pesos del catálogo y validación legal conservan sus propias tareas en los bloques fiscal, catálogo y políticas y no se darán por aprobados mediante este cierre.

### 7.1 Datos base

- [~] **SHP-001 — Confirmar origen de envío** y horario de recogida. La ubicación profesional de Sant Cristòfol 117, puerta 10, Amposta quedó validada como correcta el 27/07/2026 y no requiere cambios. La ficha confirma que es la sucursal predeterminada, prepara pedidos online y tiene el envío activado. El nombre interno quedó configurado como `LovLory — Amposta`. Permanecen como tareas independientes el horario de recogida y el modelo de ubicaciones de proveedores.
- [x] **SHP-002 — Revisar los paquetes habituales.** Completado el 28/07/2026. Lorena facilita como referencias logísticas una caja grande de 40 × 30 × 15 cm con unos 3 kg de pedido medio y una caja pequeña de 20 × 10 × 10 cm con 1 kg. Shopify mantiene una única `Caja de muestra` predeterminada de 22 × 13,7 × 4,2 cm y 0 kg. Se aprueba dejarla sin cambios porque las tarifas del checkout son planas o por importe y no dependen del paquete, las dimensiones o el peso. No introducir 1 kg ni 3 kg como tara. El punto solo se reabrirá si se compran etiquetas o se activan tarifas calculadas; entonces se crearán los dos embalajes reales y se solicitará su peso en vacío.
- [ ] **SHP-003 — Único pendiente de paquetes y pesos: confirmar el peso real de todos los productos físicos.** Usar los datos reales del CSV final, bloquear pesos faltantes y no incorporar al peso del producto la tara de la caja ni el peso medio del pedido.
- [x] **SHP-004 — Definir tiempo de preparación real** y días laborables/festivos. Criterio operativo registrado el 27/07/2026: expediciones de lunes a sábado, excepto festivos nacionales; corte nacional a las 16:00 y europeo a las 14:00. Un pedido posterior al corte pasa al siguiente día de expedición disponible. `Fechas de entrega estimadas` permanece `Desactivado` porque Shopify aplica un único tiempo global y no representa dos cortes por destino; el efecto operativo se absorbe en los plazos totales por tarifa. Incluir el criterio en la política de envíos y en la validación final conjunta de Lorena.
- [x] **SHP-005 — Definir si se muestran fechas de entrega manuales** basadas en preparación y tránsito. Configurado el 27/07/2026: `Fechas de entrega estimadas` se cambió de `Manual` a `Desactivado`; Shopify confirmó la actualización. Los intervalos se tratarán como plazos totales visibles por tarifa, sin sumar el día global de preparación: estándar/gratuito nacional `2–5 días hábiles`, urgente `1–2 días hábiles`, UE `3–7 días hábiles` y recogida mediante la descripción `Disponible para recoger en 2–5 días hábiles`. Falta aplicar y verificar cada tarifa.

### 7.2 Perfil general y zonas

- [x] **SHP-006 — Revisar el perfil de envío general** y confirmar qué productos contiene. Revisado el 27/07/2026: contiene todos los productos que no estén en otros perfiles y una ubicación de procesamiento. Tras la configuración nacional, muestra cuatro zonas: `España peninsular`, `Baleares`, `Internacional` y `UE`. Los productos nuevos se agregan por defecto.
- [x] **SHP-007 — Crear zona España peninsular.** Configurada y guardada el 27/07/2026: la zona anterior `España` se renombró `España peninsular` y quedó en `España (47 de 52 provincias)`. Se excluyeron Islas Baleares, Las Palmas, Santa Cruz de Tenerife, Ceuta y Melilla. Baleares queda pendiente de su zona y tarifas propias; los demás territorios permanecen fuera del lanzamiento.
- [x] **SHP-008 — Crear zona Baleares.** Configurada y guardada el 27/07/2026 como `Baleares`, seleccionando exclusivamente `España (Islas Baleares)`. Shopify confirmó `Perfil actualizado`. La tarifa estándar ya se añadió en SHP-015.
- [x] **SHP-009 — Mantener fuera del lanzamiento Canarias, Ceuta y Melilla.** Confirmado por Lorena y aplicado el 27/07/2026: Las Palmas, Santa Cruz de Tenerife, Ceuta y Melilla quedaron fuera de `España peninsular`. Falta probar direcciones de estos territorios durante el QA.
- [x] **SHP-010 — Desglosar la antigua zona UE según las tablas de transporte.** Completado el 28/07/2026: todos los países se trasladaron a mercados y zonas tarifarias específicas y activas; la zona general `UE (Unión Europea)` se eliminó al configurar Chequia y Polonia, sus dos últimos destinos. El cierre es únicamente logístico: siguen pendientes el QA, la validación de precios y margen y la confirmación fiscal de IVA/OSS en TAX-009/TAX-010.
- [x] **SHP-010A — Separar y configurar Portugal.** Aplicado y activado el 28/07/2026 por autorización expresa: se creó el mercado independiente `Portugal`, con moneda EUR; se retiró Portugal de `UE (Unión Europea)`; y se creó la zona `Portugal` con `Estándar Portugal` de 5,20 € entre 0,00 € y 149,99 € y 1–2 días, `Envío gratuito` desde 150 € y 1–2 días, y `Urgente Portugal` de 15,01 € y 1 día laborable. No se muestra agencia ni se promete una hora. Shopify verifica `Portugal — Activo` y `3 tarifas • Envío a Portugal`. La fiscalidad permanece heredada como `Sin recaudación`; no se abrió ni se modificó IVA/OSS. Pendiente únicamente el QA de checkout de los tres escenarios dentro de este punto; la validación fiscal continúa en TAX-009/TAX-010.
- [x] **SHP-010B — Separar y configurar Francia.** Aplicado y activado el 28/07/2026 por autorización expresa: se creó el mercado independiente `Francia` en EUR; se retiró Francia de `UE (Unión Europea)`; y se creó la zona `Francia` con `Estándar Francia` de 8,08 € entre 0,00 € y 149,99 € y `Envío gratuito` desde 150,00 €. Ambas opciones muestran `Entrega en 2–3 días hábiles`. Se usa una denominación genérica, sin mostrar DPD ni UPS; 8,08 € corresponde a la referencia `Desde` más alta de la captura y continúa pendiente de la validación conjunta de margen y costes reales. La comprobación posterior confirmó los dos tramos sin huecos ni solapamientos. La fiscalidad permanece heredada como `Sin recaudación`; no se abrió ni modificó IVA/OSS. Queda pendiente el QA de checkout.
- [x] **SHP-010C — Separar y configurar Italia y Alemania.** Aplicado y activado el 28/07/2026: se creó un único mercado `Italia y Alemania` en EUR porque ambos destinos comparten la misma tabla; se retiraron los dos países de `UE (Unión Europea)`; y se creó una zona conjunta con `Estándar Italia y Alemania` de 11,83 € entre 0,00 € y 149,99 € y plazo visible de 2–3 días hábiles, `Envío gratuito` desde 150,00 € con el mismo plazo, y `Urgente Italia y Alemania` de 15,88 € con plazo visible de 1 día hábil. Los nombres son genéricos y no muestran DPD, UPS ni DHL. La comprobación posterior confirmó ambos países, los tres servicios activos y los tramos sin huecos ni solapamientos. Los importes continúan pendientes de la validación conjunta de costes reales y margen porque son referencias `Desde` sin IVA. No se abrió ni modificó IVA/OSS; queda pendiente el QA de checkout.
- [x] **SHP-010D — Configurar el grupo europeo de 18 países con tarifa estándar de 11,31 €.** Aplicado y activado el 28/07/2026: se creó el mercado y zona `UE — Grupo 11,31 €` para Países Bajos, Bélgica, Luxemburgo, Austria, Bulgaria, Croacia, Dinamarca, Eslovaquia, Eslovenia, Estonia, Finlandia, Grecia, Hungría, Irlanda, Letonia, Lituania, Rumanía y Suecia. Se configuró `Estándar Europa grupo 11,31 €` por 11,31 € entre 0,00 € y 149,99 €, con plazo visible de 2–3 días hábiles; `Envío gratuito` desde 150,00 € con el mismo plazo; y `Urgente Europa grupo 11,31 €` por 16,25 €, con plazo visible de 1 día hábil. Los nombres no muestran DPD, UPS ni DHL. La comprobación posterior confirmó los 18 países, los tres servicios activos y los tramos sin huecos ni solapamientos. Tras configurar también SHP-010E, la zona UE general queda reducida a Chequia y Polonia. Los importes continúan pendientes de la validación conjunta de costes reales y margen porque son referencias `Desde` sin IVA. No se abrió ni modificó IVA/OSS; queda pendiente el QA de checkout.
- [x] **SHP-010E — Configurar el grupo de nueve países con tarifa de 21,75 €.** Aplicado y activado el 28/07/2026: se creó el mercado y zona `Europa — Grupo 21,75 €` para Chipre, Malta, Liechtenstein, Islandia, Moldavia, Noruega, San Marino, Suiza y Ucrania. Se configuró `Estándar Europa grupo 21,75 €` por 21,75 € entre 0,00 € y 149,99 €, con plazo visible de 2 días hábiles, y `Envío gratuito` desde 150,00 € con el mismo plazo. El nombre no muestra DHL. La comprobación posterior confirmó los nueve países, las dos opciones activas y los tramos sin huecos ni solapamientos. Chipre y Malta se retiraron de la zona UE general; Noruega y Suiza se retiraron de `Internacional`. El grupo mezcla destinos comunitarios y no comunitarios: no se abrió ni modificó IVA, OSS o aranceles, y queda pendiente la confirmación fiscal/aduanera, la validación de costes reales y margen y el QA de checkout.
- [x] **SHP-010F — Configurar Polonia y Chequia.** Aplicado y activado el 28/07/2026: se creó el mercado y zona `Polonia y Chequia`; se configuró `Estándar Polonia y Chequia` por 11,83 € entre 0,00 € y 149,99 €, con plazo visible conservador de 4–6 días hábiles, y `Envío gratuito` desde 150,00 € con el mismo plazo. El nombre no muestra DPD ni UPS. La comprobación posterior confirmó ambos países, las dos opciones activas y los tramos sin huecos ni solapamientos. Al ser los dos últimos destinos, se eliminó la antigua zona `UE (Unión Europea)`. No se abrió ni modificó IVA/OSS; quedan pendientes el QA y la validación conjunta de costes reales y margen.
- [ ] **SHP-011 — Comprobar que ningún país aparece en dos zonas del mismo perfil.**
- [x] **SHP-012A — Configurar Andorra como destino internacional no comunitario.** Aprobado y aplicado el 28/07/2026: se creó y activó el mercado independiente `Andorra` con moneda EUR; se creó la zona de envío `Andorra`; se guardó `Envío a domicilio` por 17,27 € con tránsito de 1–2 días laborables; y se añadió `Envío gratuito` desde 150 € con el mismo tránsito. El perfil confirmó `Perfil actualizado`. La configuración fiscal permanece heredada como `Sin recaudación`; no se abrió ni modificó `Impuestos y aranceles`.
- [x] **SHP-012B — Excluir los demás destinos internacionales no validados.** Aplicado el 28/07/2026 por confirmación expresa: se eliminó la zona `Internacional`, que contenía 12 países sin mercado activo y una tarifa antigua `Estándar` de 12,99 €. La comprobación posterior confirma que la zona ya no existe y que permanecen intactas las nueve zonas válidas del perfil. Si se recupera posteriormente alguno de estos destinos, deberá crearse una zona nueva con mercado, tarifas, plazos y tratamiento fiscal/aduanero aprobados.

### 7.3 Tarifas y servicios

> No se revisarán ni modificarán más tarifas individualmente hasta recibir la validación conjunta del cliente, ya que todas utilizan los mismos campos básicos de configuración.

- [x] **SHP-013 — Introducir tarifa estándar de Península** basada en el contrato real. Configurada y guardada el 27/07/2026 en `España peninsular` como `Importe del pedido`, mínimo 0,00 €, máximo 49,99 €, precio 5,20 € y tránsito de 2–5 días hábiles. Se editó la tarifa existente, sin crear solapamientos; la gratuita continúa desde 50 €. Se ofrecerá entrega a domicilio con nombre genérico y no `En oficina`. El precio comercial de 5,20 € se adopta provisionalmente por decisión del proyecto, aunque la referencia de coste es `Desde`, sin IVA; quedan pendientes la validación de margen y el tratamiento fiscal por Lorena o su gestoría. No se modificó ninguna opción fiscal.
- [x] **SHP-014 — Configurar envío gratuito** desde 50 € en España peninsular, con 2–5 días laborables. Configurada y guardada el 27/07/2026 como `Importe del pedido`, mínimo 50,00 €, sin máximo, precio 0,00 € y tránsito personalizado de 2–5 días hábiles. Shopify confirmó la actualización. Su aplicación a Baleares sigue pendiente; falta verificarla en checkout durante el QA.
- [x] **SHP-015 — Introducir tarifa de Baleares** y sus condiciones. Configuradas y guardadas el 27/07/2026 dos tarifas `Estándar Baleares`: 8,62 € entre 0,00 € y 49,99 €, y gratuita desde 50,00 € sin máximo; ambas con tránsito personalizado de 2–3 días hábiles. Shopify confirmó `Perfil actualizado` y el resumen muestra los dos tramos sin huecos ni solapamiento. Queda incluida en la única validación final conjunta de Lorena.
- [!] **SHP-016 — Introducir tarifas especiales** por peso, valor, producto o ámbito local. Recogida guardada el 27/07/2026 como `Recogida en Lovlory — Amposta (no se envía)`: 3,95 € entre 0,00 € y 99,99 €, gratis desde 100,00 € y 2–5 días hábiles en ambos tramos. Pendiente de QA en checkout porque Shopify la gestiona como envío para toda España. El componente `Urgente` quedó aprobado y aplicado el 28/07/2026 como opción genérica, sin prometer hora ni agencia, por 15,01 € y 1–2 días laborables; sustituye los 9,50 € sin plazo y Shopify confirmó `Perfil actualizado`. La referencia original es `Desde` y sin IVA, por lo que margen, pesos y recargos deben incluirse en la validación conjunta sin modificar fiscalidad. Las muñecas Mistress de tamaño real requieren porte fijo de 45 €: se prevé un perfil de envío personalizado con los productos o variantes afectados, pero no se ha creado. Antes hay que confirmar si 45 € es un precio final con IVA o un coste neto, si se cobra por pedido, muñeca o expedición, el ámbito geográfico, su relación con el envío gratuito y la regla para carritos mixtos. Shopify suma las tarifas de perfiles distintos, por lo que una Mistress junto con un producto general podría resultar en 45 € más el porte ordinario. La colección Mistress servirá para identificar el catálogo, pero el perfil debe contener productos o variantes concretos y mantenerse al añadir nuevos artículos. Terres de l’Ebre necesita entrega normal, urgente y una modalidad de “momentos especiales” todavía por definir. Pantalla revisada el 28/07/2026: `Configuración > Envío y entrega > Perfiles de envío`; sin cambios.
- [!] **SHP-017 — Confirmar el flujo real de elección y asignación de transportista.** `Cuentas de empresas de transporte` muestra `Ninguno`; no se conectó ninguna cuenta ni se instaló una aplicación de pago. Revisada el 28/07/2026 la pantalla `Gestionar empresas de transporte preferidas`: Shopify indica que Correos, SEUR y DHL Express Spain solo se recomiendan al comprar etiquetas y que estas preferencias no influyen en las tarifas del checkout. Se dejó sin cambios porque no permite que el cliente elija agencia ni asigna el transporte según zona, producto, proveedor o almacén; solo se configurará si Lovlory compra etiquetas en Shopify y confirma sus empresas preferidas. Las zonas actuales usan provisionalmente tarifas planas y nombres genéricos, asumiendo que el proveedor, el almacén o Lovlory eligen internamente NACEX, SEUR, Correos Express u otra agencia. **Bloqueante antes del cierre:** Lorena debe confirmar si la agencia se asigna automática o internamente después del pedido, o si el cliente debe elegirla en el checkout; también debe explicar qué ocurre con pedidos que contienen productos de varios proveedores, posibles envíos divididos y combinación de portes. Si la elección es interna, se conserva la configuración actual. Si el cliente elige, habrá que desglosar cada zona por transportista y servicio. Si depende del producto, proveedor o ubicación, habrá que revisar perfiles, ubicaciones y tarifas combinadas. No desglosar ni eliminar las opciones genéricas hasta recibir la respuesta.
- [x] **SHP-018 — Definir si habrá recogida local o puntos de recogida.** Completado el 28/07/2026 mediante la alternativa sin aplicación `Recogida en Lovlory — Amposta (no se envía)`: 3,95 € entre 0,00 € y 99,99 €, gratuita desde 100,00 € y 2–5 días hábiles. `Retiro en tienda`, `Puntos de retiro` y `Entrega local` permanecen desactivados. La pantalla `Entrega local` muestra la sucursal de Amposta con el estado `No ofrece entrega`. Se aprueba no activar reparto local para el lanzamiento; una futura entrega en Terres de l’Ebre se tratará como ampliación independiente cuando se definan área, modalidades, precios y plazos. La recogida alternativa continúa pendiente únicamente del QA general de checkout.
- [x] **SHP-019A — Confirmar seguro y seguimiento.** Lorena confirma que todos los envíos deben incluir seguimiento y seguro. Requisito operativo validado.
- [ ] **SHP-019B — Confirmar firma o modalidad del justificante de entrega.** Lorena espera justificante, pero falta concretar si debe incluir firma, qué servicio lo proporciona y cómo se reflejará en la política.
- [ ] **SHP-020 — Definir procedimiento de dirección incorrecta, ausencia, reexpedición y paquete rechazado.**
- [x] **SHP-021 — Definir embalaje discreto** y verificar que etiqueta, remitente y descriptor respeten la política de privacidad de marca. Completado el 28/07/2026: Lorena confirma embalaje sin logotipos y remitente discreto, y se valida `Lovlory` como nombre suficientemente discreto para las etiquetas. La pantalla `Documentos > Nombre del remitente en las etiquetas de envío` ya tenía seleccionada esa opción; no fue necesario cambiarla ni pulsar `Guardar`.
- [!] **SHP-022 — Definir proceso de devolución:** Lorena solo contempla devoluciones por defecto o tara y dice que “el remitente” asume el porte en casos puntuales. La asesoría debe validar el texto y aclarar quién paga antes de configurar automatizaciones.
- [ ] **SHP-023 — Completar información aduanera antes de vender internacionalmente.** Actualmente 0 de 196 variantes tienen país de origen y 0 de 196 tienen código del sistema armonizado (SA). No bloquea el lanzamiento exclusivamente nacional.
- [!] **SHP-024 — Validación comercial final conjunta de Envío y preparación por Lorena.** Única puerta pendiente para cerrar funcionalmente el bloque: aprobar zonas y destinos, servicios visibles, importes finales con margen, umbrales de gratuidad, plazos, asignación de agencia y pedidos de varios proveedores, regla de porte Mistress, justificante/firma y criterio comercial de incidencias. Las validaciones fiscal/OSS, aduanera, de pesos de catálogo y legal permanecen fuera de esta puerta y continúan en sus tareas específicas.

**Criterio de cierre del bloque:** cada territorio activo devuelve exactamente una opción válida de envío, con coste y plazo correctos.

> **Aviso fiscal observado (27/07/2026):** la ficha de la sucursal muestra un aviso para gestionar una posible obligación tributaria en Tarragona. No se abrió ni se modificó; cualquier actuación fiscal permanece bloqueada hasta confirmación de Lorena o de su gestoría.

## 8. Checkout y cuentas de cliente

- [~] **CHK-001 — Configurar contacto del cliente:** correo obligatorio; teléfono de envío opcional hasta confirmar si lo exige el transportista. Seguimiento mediante Shop activado y pendiente de validar por privacidad/discreción.
- [~] **CHK-002 — Revisar nombre, apellidos, empresa y segunda línea de dirección.** Revisado el 27/07/2026: nombre y apellidos obligatorios; segunda línea opcional; nombre de empresa y número de IVA configurados como `No incluir`. Lorena prevé ventas mayoritariamente B2C y algunas ventas a asociaciones con NIF; mantener los campos ocultos hasta concretar el flujo fiscal y de facturación.
- [x] **CHK-003 — Activar validación de dirección.** Se permiten direcciones de envío y facturación diferentes, la dirección de envío se usa como valor predeterminado para facturación y la validación de entrega está activada. Probar códigos postales especiales durante el QA.
- [x] **CHK-004 — Decidir si las cuentas de cliente son opcionales.** Compra como invitado permitida; no se exige iniciar sesión antes del pago.
- [~] **CHK-005 — Revisar consentimiento de marketing** separado de la aceptación necesaria para completar la compra. Correo y SMS están ocultos hasta disponer de estrategia y textos aprobados.
- [ ] **CHK-006 — Configurar recuperación de checkout abandonado** y revisar su texto, plazo y descuentos.
- [x] **CHK-007 — Revisar propinas, venta adicional y aplicaciones del checkout.** Propinas desactivadas el 21/07/2026 y ninguna aplicación con reglas de carrito o pago instalada.
- [ ] **CHK-008 — Revisar mensaje de error cuando un destino no tiene envío.**
- [ ] **CHK-009 — Personalizar página de agradecimiento y estado del pedido** sin scripts obsoletos.
- [ ] **CHK-010 — Verificar privacidad del contenido del paquete y comunicaciones** de cara al cliente.
- [x] **CHK-011 — Mostrar enlaces de inicio de sesión.** Actualmente están activados en la cabecera de la tienda y en el pago; mantenerlos salvo decisión contraria.
- [x] **CHK-012 — Revisar autenticación de las cuentas de cliente.** `Shop` está activo; Google y Facebook no están conectados. Mantener Shop y no añadir conexiones sociales sin una necesidad concreta.
- [x] **CHK-013 — Configurar un subdominio propio para cuentas de cliente.** `cuenta.lovlory.com` está conectado y establecido como principal; incluir inicio de sesión, estado del pedido y consulta de pedidos en el QA final.
- [!] **CHK-014 — Mantener desactivadas las devoluciones y cancelaciones de autoservicio** hasta aprobar política, reglas, plazos, costes y exclusiones de higiene.
- [!] **CHK-015 — Decidir el uso del crédito en tienda.** Actualmente está activado por defecto; falta aprobar su finalidad, vencimiento, tratamiento contable, reembolsos y posibles cargos por transacción.
- [ ] **CHK-016 — Personalizar las cuentas de cliente** junto con el diseño final del checkout, sin instalar aplicaciones innecesarias.

**Criterio de cierre del bloque:** un cliente nuevo puede comprar sin fricción, entiende los consentimientos y recibe información de entrega correcta.

## 9. Políticas, privacidad y cumplimiento

> Las plantillas de Shopify son un punto de partida. Deben revisarse para el negocio, el catálogo y la normativa aplicable.
>
> **Responsabilidad:** la clienta debe entregar todos los textos legales definitivos, preparados o validados por su asesoría. El proyecto solo los incorporará y verificará en Shopify; no realizará redacción ni adaptación jurídica.

- [ ] **LEG-001 — Recibir y publicar el aviso legal definitivo:** titular, NIF/CIF, domicilio y contacto.
- [ ] **LEG-002 — Recibir y publicar las condiciones de compra definitivas:** formación del contrato, precio, pago, entrega, incidencias y jurisdicción.
- [ ] **LEG-003 — Recibir y publicar la política de envíos definitiva:** zonas, costes, preparación, tránsito, seguimiento e incidencias.
- [ ] **LEG-004 — Recibir y publicar la política de devoluciones y reembolsos definitiva:** plazos, proceso, costes y estado del producto.
- [ ] **LEG-005 — Recibir de la clienta el texto validado sobre la excepción de desistimiento por higiene** para bienes precintados que no sean aptos para devolución tras desprecintarse.
- [ ] **LEG-006 — Recibir y publicar la política de privacidad definitiva:** responsables, finalidades, bases, proveedores, conservación y derechos.
- [ ] **LEG-007 — Recibir la política de cookies definitiva y configurar el banner de consentimiento** según las instrucciones de la asesoría y las herramientas realmente instaladas.
- [ ] **LEG-008 — Recibir y publicar la información de contacto y reclamaciones** accesible desde el pie de página.
- [ ] **LEG-009 — Recibir los textos aprobados sobre mayoría de edad y acceso al catálogo, si corresponden.** No usar una barrera de edad como sustituto de cumplimiento.
- [ ] **LEG-010 — Revisar descripciones e imágenes:** producto físico, materiales, medidas, uso, limpieza y seguridad; sin afirmaciones médicas no sustentadas.
- [ ] **LEG-011 — Revisar garantías y conformidad de producto.**
- [ ] **LEG-012 — Revisar etiquetado, fabricante/importador y obligaciones de seguridad** aplicables al catálogo.
- [ ] **LEG-013 — Añadir enlaces permanentes a políticas** en pie de página y checkout.
- [ ] **LEG-014 — Guardar fecha y versión de cada política aprobada.**

**Criterio de cierre del bloque:** asesoría ha revisado los textos y todas las políticas son accesibles antes de pagar.

## 10. Dominio, correo y notificaciones

### 10.1 Dominio y correo

- [ ] **DOM-001 — Conectar el dominio principal** y elegir una única versión canónica.
- [ ] **DOM-002 — Verificar SSL activo** y ausencia de advertencias del navegador.
- [ ] **DOM-003 — Configurar redirección desde dominios secundarios.**
- [ ] **DOM-004 — Configurar SPF, DKIM y DMARC** del dominio de correo según el proveedor.
- [ ] **DOM-005 — Probar recepción y respuesta** desde las direcciones de atención.

### 10.2 Notificaciones

- [ ] **NTF-001 — Revisar confirmación de pedido.**
- [ ] **NTF-002 — Revisar confirmación y actualización de envío.**
- [ ] **NTF-003 — Revisar entrega, cancelación y reembolso.**
- [ ] **NTF-004 — Revisar recuperación de checkout abandonado.**
- [ ] **NTF-005 — Aplicar identidad visual y tono de LovLory.**
- [ ] **NTF-006 — Evitar contenido sensible innecesario en asuntos o previsualizaciones.**
- [ ] **NTF-007 — Probar notificaciones en móvil y escritorio.**
- [ ] **NTF-008 — Verificar enlaces a ayuda, seguimiento y políticas.**

**Criterio de cierre del bloque:** dominio seguro, correo autenticado y ciclo completo de notificaciones probado.

## 11. Catálogo, colecciones y búsqueda

Este bloque se coordina con el flujo de migración WooCommerce → Shopify existente en el repositorio.

- [ ] **CAT-001 — Importar únicamente desde el CSV final validado.**
- [ ] **CAT-002 — Conservar la categoría WooCommerce original** para trazabilidad.
- [ ] **CAT-003 — Verificar por producto:** título, `Body (HTML)`, precio, SKU, vendor, tipo, tags, colecciones, stock, peso y SEO.
- [ ] **CAT-004 — No inventar descripciones ni imágenes.**
- [ ] **CAT-005 — Mantener en borrador productos sin precio, imagen o stock disponible.**
- [ ] **CAT-006 — Comprobar handles duplicados y SKU vacíos.**
- [ ] **CAT-007 — Validar pesos faltantes en productos físicos.**
- [ ] **CAT-008 — Verificar imágenes en Shopify CDN y estado de media `READY`.**
- [ ] **CAT-009 — Documentar productos con URL de imagen fallida.**
- [ ] **CAT-010 — Revisar colecciones automáticas y manuales** con el plan de colecciones del proyecto.
- [ ] **CAT-011 — Revisar navegación principal, filtros y búsqueda.**
- [ ] **CAT-012 — Revisar SEO title, SEO description, URL y contenido duplicado.**
- [ ] **CAT-013 — Revisar texto alternativo de imágenes.**
- [ ] **CAT-014 — Revisar recomendaciones y productos relacionados** para evitar asociaciones inadecuadas.
- [ ] **CAT-015 — Ejecutar verificación reproducible y guardar resumen JSON.**

**Criterio de cierre del bloque:** recuentos coinciden, productos inválidos permanecen en borrador y el muestreo visual/operativo está aprobado.

## 12. Analítica, privacidad de marketing y canales

- [ ] **ANA-001 — Configurar Google Analytics** solo con la propiedad correcta.
- [ ] **ANA-002 — Configurar píxeles publicitarios** mediante integraciones compatibles, sin duplicar eventos.
- [ ] **ANA-003 — Vincular Search Console** y enviar sitemap tras el lanzamiento.
- [ ] **ANA-004 — Configurar banner y regiones de consentimiento.** Comprobar que las etiquetas respetan la elección del usuario.
- [ ] **ANA-005 — Definir eventos clave:** vista de producto, añadir al carrito, iniciar checkout, compra y reembolso.
- [ ] **ANA-006 — Excluir tráfico interno** cuando sea posible.
- [ ] **ANA-007 — Revisar retención y acceso a datos.**
- [ ] **ANA-008 — Evaluar elegibilidad de Google Merchant Center y otros canales** para productos adultos antes de sincronizar.
- [ ] **ANA-009 — Marcar correctamente productos para adultos** en feeds que lo exijan y respetar restricciones publicitarias.
- [ ] **ANA-010 — Revisar canal Shop.** Algunos productos o contenidos maduros pueden no ser elegibles aunque la tienda online funcione.

**Criterio de cierre del bloque:** medición sin duplicados, consentimiento probado y ningún canal recibe productos no elegibles.

## 13. Pruebas de aceptación antes del lanzamiento

Crear una hoja de resultados con fecha, dispositivo, dirección utilizada, pedido y resultado.

### 13.1 Catálogo y navegación

- [ ] **QA-001 — Buscar productos por título, marca y SKU.**
- [ ] **QA-002 — Probar filtros, colecciones, migas de pan y productos relacionados.**
- [ ] **QA-003 — Revisar una muestra de productos por marca:** ORGIE, SVAKOM, TENGA y MISTRESS.
- [ ] **QA-004 — Confirmar imágenes, precio con IVA, stock, variantes y peso.**

### 13.2 Carrito, impuestos y transporte

- [ ] **QA-005 — Pedido España peninsular por debajo del envío gratis.**
- [ ] **QA-006 — Pedido España peninsular por encima del envío gratis.**
- [ ] **QA-007 — Pedido Baleares.**
- [ ] **QA-008 — Dirección de Canarias/Ceuta/Melilla según su estado activo o bloqueado.**
- [ ] **QA-009 — Dirección de país no atendido.**
- [ ] **QA-010 — Carrito de varios productos y pesos.**
- [ ] **QA-011 — Código de descuento y combinación de promociones.**
- [ ] **QA-012 — Comparar IVA y total con cálculo esperado.**

### 13.3 Pago y posventa

- [ ] **QA-013 — Pago satisfactorio en móvil.**
- [ ] **QA-014 — Pago satisfactorio en escritorio.**
- [ ] **QA-015 — Pago rechazado y reintento.**
- [ ] **QA-016 — Flujo 3D Secure.**
- [ ] **QA-017 — Preparar pedido y añadir seguimiento.**
- [ ] **QA-018 — Reembolso parcial.**
- [ ] **QA-019 — Reembolso total y cancelación.**
- [ ] **QA-020 — Confirmar actualización correcta del inventario.**
- [ ] **QA-021 — Revisar todas las notificaciones recibidas.**
- [ ] **QA-022 — Confirmar que analítica registra compra una sola vez.**

### 13.4 Calidad técnica y contenido

- [ ] **QA-023 — Revisar móvil, tableta y escritorio.**
- [ ] **QA-024 — Revisar enlaces rotos, redirecciones y página 404.**
- [ ] **QA-025 — Revisar rendimiento de páginas principales.**
- [ ] **QA-026 — Revisar accesibilidad básica:** teclado, contraste, etiquetas y texto alternativo.
- [ ] **QA-027 — Revisar políticas y contacto desde todas las páginas clave.**
- [ ] **QA-028 — Registrar incidencias, responsable y fecha de corrección.**

**Criterio de cierre del bloque:** cero errores bloqueantes y aprobación formal de pagos, impuestos, transporte, catálogo y legal.

## 14. Lanzamiento

- [ ] **LCH-001 — Congelar cambios de catálogo y configuración** durante la ventana de lanzamiento.
- [ ] **LCH-002 — Realizar copia/exportación de configuración y datos disponibles.**
- [ ] **LCH-003 — Confirmar dominio principal, SSL y redirecciones.**
- [ ] **LCH-004 — Desactivar contraseña de la tienda** solo con autorización final.
- [ ] **LCH-005 — Activar exclusivamente mercados, pagos y zonas aprobados.**
- [ ] **LCH-006 — Confirmar inventario final** inmediatamente antes de abrir.
- [ ] **LCH-007 — Ejecutar compra real de control** y validar liquidación.
- [ ] **LCH-008 — Comprobar indexación, sitemap y robots.**
- [ ] **LCH-009 — Preparar soporte y protocolo de incidencias** para las primeras 72 horas.
- [ ] **LCH-010 — Registrar fecha, hora y responsables del lanzamiento.**

**Criterio de cierre del bloque:** tienda accesible, compra real verificada y equipo preparado para incidencias.

## 15. Seguimiento posterior al lanzamiento

- [ ] **OPS-001 — Revisar diariamente pedidos, pagos fallidos y fraude** durante la primera semana.
- [ ] **OPS-002 — Revisar inventario negativo o desajustes** diariamente durante la primera semana.
- [ ] **OPS-003 — Revisar errores de envío y direcciones sin tarifa.**
- [ ] **OPS-004 — Revisar fallos de imágenes y media.**
- [ ] **OPS-005 — Revisar contracargos y consultas sobre el descriptor bancario.**
- [ ] **OPS-006 — Comparar costes reales de transporte con tarifas cobradas.**
- [ ] **OPS-007 — Revisar conversión y abandono de checkout** después de acumular datos suficientes.
- [ ] **OPS-008 — Conciliar pedidos, pagos, reembolsos e impuestos** con contabilidad.
- [ ] **OPS-009 — Revisar aplicaciones y costes mensualmente.**
- [ ] **OPS-010 — Revisar políticas, mercados e impuestos** cuando cambie la operación o la normativa.

## Puertas de aprobación

| Puerta | Condición | Aprobación | Fecha | Evidencia |
|---|---|---|---|---|
| A — Base | Bloques 0–3 terminados | Pendiente | — | — |
| B — Cobro y fiscalidad | Bloques 4–5 aprobados | Pendiente | — | — |
| C — Operación | Bloques 6–10 aprobados | Pendiente | — | — |
| D — Catálogo y medición | Bloques 11–12 aprobados | Pendiente | — | — |
| E — Salida | Bloque 13 sin errores bloqueantes | Pendiente | — | — |
| F — Lanzamiento | Bloque 14 completado | Pendiente | — | — |

## Registro de decisiones

| ID | Fecha | Decisión | Motivo | Responsable | Impacto / seguimiento |
|---|---|---|---|---|---|
| DEC-001 | — | Mercado inicial por definir | Validar logística y fiscalidad | Por asignar | Actualizar MKT y SHP |
| DEC-002 | — | Transportista por definir | Faltan tarifas reales | Por asignar | Actualizar SHP-013 a SHP-019 |
| DEC-003 | — | Proveedor de pagos por confirmar | Revisión de catálogo adulto | Por asignar | Actualizar PAY-001 a PAY-007 |
| DEC-004 | — | Servicio fiscal por elegir | Shopify Tax frente a manual | Por asignar | Actualizar TAX-003 |
| DEC-005 | 21/07/2026 | Usar identificadores de pedido con formato `LV-1001` | Mejorar legibilidad e identificación de pedidos | Configuración de tienda | Prefijo `LV-`; sufijo vacío |
| DEC-006 | 21/07/2026 | Activar el paso de confirmación antes del pago | Permitir que el cliente revise los datos del pedido antes de comprar | Configuración de tienda | Verificar durante el pedido de prueba |
| DEC-007 | 27/07/2026 | Lanzamiento logístico nacional limitado a Península y Baleares; Canarias, Ceuta y Melilla excluidas | Confirmación de Lorena | Configuración de tienda | Separar zonas y probar direcciones excluidas |
| DEC-008 | 27/07/2026 | Umbral gratuito de 50 € para nacional y 150 € para UE | Confirmación comercial de Lorena | Configuración de tienda | UE no se activa hasta cerrar OSS, países y precios |
| DEC-009 | 27/07/2026 | Mantener la UE inactiva durante la revisión logística | Faltan OSS, países exactos y tarifas finales con IVA | Configuración de tienda / gestoría | No activar mercado ni zona todavía |
| DEC-010 | 27/07/2026 | Nombrar la sucursal predeterminada `LovLory — Amposta` | Identificación clara en inventario y preparación | Configuración de tienda | Nombre guardado; dirección sin cambios |
| DEC-011 | 27/07/2026 | No crear sucursales físicas para proveedores de dropshipping hasta definir su integración | Shopify puede usar ubicaciones de aplicaciones o servicios de logística personalizados; faltan SKU y flujo operativo | Configuración de tienda | Recopilar datos operativos mínimos; pedir direcciones solo cuando sean necesarias |
| DEC-012 | 27/07/2026 | Desactivar las fechas manuales globales y mostrar plazos totales por tarifa | Evitar que Shopify sume un día global de preparación a los intervalos aprobados | Configuración de tienda | Global guardado; configurar y probar cada tarifa |
| DEC-013 | 27/07/2026 | Limitar la tarifa estándar de 4,95 € a pedidos de 0,00 € a 49,99 € | Corregir su solapamiento con el envío gratuito desde 50 € | Configuración de tienda | Tarifa y perfil guardados; verificar en checkout |
| DEC-014 | 27/07/2026 | Mantener envío nacional gratuito desde 50 € y mostrar 2–5 días hábiles | Confirmación comercial de Lorena y coherencia con la tarifa estándar | Configuración de tienda | Tarifa y perfil guardados; verificar en checkout |
| DEC-015 | 27/07/2026 | Implementar la recogida de Amposta sin aplicación mediante una tarifa por importe claramente identificada | Mantener 3,95 € por debajo de 100 € y gratuidad desde 100 € sin coste recurrente | Configuración de tienda | Tarifa y perfil guardados; verificar ambos tramos y la claridad del checkout |
| DEC-016 | 27/07/2026 | Ofrecer para Península estándar la modalidad a domicilio y fijar provisionalmente un precio comercial de 5,20 € | Evitar modalidades de oficina sin selector de punto y tomar como referencia el mayor coste a domicilio observado | Configuración de tienda | Tarifa guardada; la base NACEX es `Desde` y sin IVA, por lo que margen y fiscalidad siguen pendientes |
| DEC-017 | 27/07/2026 | Mostrar servicios genéricos y dejar que el almacén elija internamente la agencia | En dropshipping la agencia depende del origen y no siempre puede respetarse una elección del cliente | Configuración de tienda | No crear tarifas visibles por NACEX, SEUR o Correos Express; revisar costes reales por almacén |

## Registro de incidencias

| ID | Fecha | Área / pedido | Descripción | Severidad | Responsable | Estado | Resolución |
|---|---|---|---|---|---|---|---|
| INC-001 | — | — | — | — | — | Abierta | — |

## Datos pendientes para comenzar

1. URL `*.myshopify.com` o URL de administración.
2. Razón social/autónomo, NIF/CIF y dirección fiscal.
3. Modelo de ubicaciones para Amposta y almacenes de proveedores en dropshipping; horario completo y cortes.
4. Contratos/tarifas definitivas por origen y precios comerciales finales con IVA.
5. Países exactos de la UE y aclaración de los países europeos no UE incluidos en la tabla.
6. Validación de margen para los umbrales confirmados: 50 € nacional y 150 € UE.
7. Confirmación de la gestoría sobre IVA, OSS y territorios especiales.
8. Estado de Shopify Payments, PayPal y cualquier proveedor alternativo.
9. Separación entre preparación, tránsito y plazo total; tratamiento de sábados y pedidos posteriores al corte.
10. Política de devoluciones aprobada o borrador actual.

## Fuentes de referencia

- Shopify, configuración de monedas para mercados: <https://help.shopify.com/es/manual/markets/customizations/local-currencies>
- Shopify, impuestos de la Unión Europea: <https://help.shopify.com/en/manual/taxes/eu>
- Shopify, funciones de Shopify Tax para UE y Reino Unido: <https://help.shopify.com/es/manual/taxes/shopify-tax/shopify-tax-eu>
- Shopify, zonas y tarifas de envío: <https://help.shopify.com/es/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates>
- Shopify, Shopify Payments en España: <https://help.shopify.com/es/manual/payments/shopify-payments/supported-countries/spain>
- Shopify, requisitos bancarios de Shopify Payments en España: <https://help.shopify.com/es/manual/payments/shopify-payments/supported-countries/spain/requirements>
- Shopify, elegibilidad de Shopify Payments: <https://help.shopify.com/es/manual/payments/shopify-payments/onboarding/eligibility>
- Shopify, configuración de PayPal Express Checkout: <https://help.shopify.com/es/manual/payments/paypal/set-up-paypal>
- Shopify, autorización y captura de pagos: <https://help.shopify.com/es/manual/payments/payment-authorization/>
- PayPal, política de uso aceptable: <https://www.paypal.com/es/legalhub/paypal/acceptableuse-full?locale.x=es_ES>
- Shopify, configuración y gestión de cuentas de cliente: <https://help.shopify.com/es/manual/customers/customer-accounts/manage>
- Shopify, crédito en tienda: <https://help.shopify.com/es/manual/customers/store-credit>
- Shopify, guía para vender juguetes sexuales: <https://www.shopify.com/blog/sell-sex-toys>
- Agencia Tributaria, tipos de IVA: <https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-04-sujetos-pasivos-repercusion-impositivo/tipo-impositivo.html>
- Agencia Tributaria, ventas a particulares de otros Estados miembros: <https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/ventas-particulares-otros-estados-miembros-ue.html>

---

**Próximo paso recomendado:** completar el bloque 0. Con esas decisiones se podrán establecer valores reales en Shopify sin rehacer después impuestos, mercados o tarifas de envío.
