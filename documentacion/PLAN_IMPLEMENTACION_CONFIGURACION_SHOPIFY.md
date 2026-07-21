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
| 4 | Impuestos | Pendiente | Por asignar | — |
| 5 | Pagos | En curso | Por asignar | Pantalla revisada; proveedores sin validar, 21/07/2026 |
| 6 | Ubicaciones e inventario | Pendiente | Por asignar | — |
| 7 | Transporte y preparación | Pendiente | Por asignar | — |
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
- [ ] **CFG-003 — Confirmar origen de los envíos.** Dirección física, provincia, código postal y horario de recogida.
  - Valor: ________________________________________________
- [ ] **CFG-004 — Definir alcance geográfico de lanzamiento.** Recomendación inicial: España peninsular y Baleares; Canarias, Ceuta, Melilla y otros países solo después de validar impuestos, aduanas y costes.
  - Decisión: ________________________________________________
- [ ] **CFG-005 — Confirmar transportista y tarifas contratadas.** Incluir coste por zona, peso, combustible, reexpediciones y devoluciones.
  - Transportista / contrato: ________________________________________________
- [ ] **CFG-006 — Definir umbral de envío gratuito.** Calcularlo con margen medio, ticket objetivo y coste logístico; no elegir una cifra arbitraria.
  - Umbral aprobado: ________________________________________________
- [ ] **CFG-007 — Confirmar régimen de IVA y registro OSS con la gestoría.**
  - Conclusión de la gestoría: ________________________________________________
- [ ] **CFG-008 — Confirmar procesadores de pago compatibles con el catálogo.** Indicar expresamente que se venden juguetes sexuales físicos, no contenido o servicios sexuales.
  - Proveedor principal: ____________________  Alternativo: ____________________
- [ ] **CFG-009 — Definir política comercial de devoluciones.** Plazo, costes, productos precintados y condiciones de higiene.
  - Decisión: ________________________________________________
- [ ] **CFG-010 — Definir plazo real de preparación.** Recomendación provisional: 1–2 días laborables si la operación puede cumplirlo.
  - Plazo aprobado: ________________________________________________

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
- [ ] **GEN-002 — Razón social, NIF/CIF y dirección:** introducir datos reales y consistentes con pagos y facturación.
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
- [ ] **MKT-011 — Antes de activar la UE, confirmar OSS y tributación en destino** con la gestoría.
- [ ] **MKT-012 — Definir moneda por mercado.** Para la eurozona, EUR; otras monedas solo con una decisión comercial y revisión de costes de conversión.
- [ ] **MKT-013 — Definir idiomas y traducciones** antes de indexar nuevos mercados.
- [ ] **MKT-014 — Revisar precios, redondeos y margen por mercado.**
- [ ] **MKT-015 — Crear zonas y tarifas de envío correspondientes** antes de activar cada mercado.

**Criterio de cierre del bloque:** solo pueden comprar clientes de territorios preparados, con moneda, idioma, impuestos y transporte coherentes.

## 4. Impuestos

Ruta orientativa: **Configuración > Impuestos y aranceles**.

> Validación obligatoria: Shopify ayuda a calcular impuestos, pero LovLory sigue siendo responsable de determinar, declarar y pagar los importes correctos.

- [ ] **TAX-001 — Confirmar con gestoría el tipo aplicable al catálogo.** Punto de partida esperado para productos físicos ordinarios: IVA general del 21 %, salvo productos con tratamiento específico.
- [!] **TAX-002 — Añadir el registro español de IVA** con el identificador real del negocio. El mercado España muestra actualmente `Sin recaudación`; faltan datos fiscales y validación de la gestoría.
- [x] **TAX-003 — Elegir servicio fiscal.** `Servicios fiscales de Shopify / Shopify Tax` figura activo para la Unión Europea; verificado el 21/07/2026.
- [~] **TAX-004 — Configurar precios con IVA incluido** para venta B2C en España, si la gestoría lo confirma. El mercado España tiene seleccionada la `Visualización dinámica de impuestos`; quedará operativa cuando se configure la recaudación y deberá validarse con un pedido de prueba.
- [~] **TAX-005 — Confirmar el tratamiento fiscal de los gastos de envío.** La casilla global está desmarcada, pero Shopify Tax calcula automáticamente el impuesto del transporte en la UE cuando corresponde. Falta validarlo con la gestoría y mediante un pedido de prueba.
- [!] **TAX-006 — Revisar la categoría fiscal de cada producto** y evitar anulaciones globales sin justificación. Shopify Tax muestra 193 productos sin categorizar; deben clasificarse y verificarse antes de la prueba fiscal final.
- [ ] **TAX-007 — Revisar regalos, descuentos y códigos promocionales** con impuestos incluidos.
- [ ] **TAX-008 — Configurar Canarias, Ceuta y Melilla** solo tras recibir instrucciones fiscales y logísticas específicas.
- [ ] **TAX-009 — Registrar la decisión sobre OSS.** El umbral conjunto de ventas B2C intracomunitarias a distancia es de 10.000 € sin IVA en las condiciones descritas por la AEAT.
- [~] **TAX-010 — Configurar facturas con IVA** o la solución de facturación que utilice la empresa. La generación automática de Shopify está desactivada; falta confirmar si se usará esta función o un programa externo y completar primero el registro de IVA.
- [ ] **TAX-011 — Ejecutar pedidos fiscales de prueba:** Península, Baleares y, si están activos, UE/Canarias/Ceuta/Melilla.
- [ ] **TAX-012 — Comparar el cálculo de Shopify con un cálculo manual** y obtener aprobación de la gestoría.

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

- [ ] **INV-001 — Crear la ubicación real de preparación** con dirección y nombre claros.
- [ ] **INV-002 — Desactivar ubicaciones ficticias o de prueba** que puedan recibir inventario o pedidos.
- [ ] **INV-003 — Definir qué ubicación prepara pedidos online.**
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

### 7.1 Datos base

- [!] **SHP-001 — Confirmar origen de envío** y horario de recogida. La ubicación actual muestra `C/ Sant Cristofol 117 puerta 10, 43870 Amposta`; no se considera validada y difiere de la referencia `Despacho n.º 10`.
- [~] **SHP-002 — Crear paquetes habituales** con dimensiones y tara reales. Existe una caja configurada; faltan revisar dimensiones y peso en vacío.
- [ ] **SHP-003 — Confirmar peso de todos los productos físicos.** Usar los datos reales del CSV final y bloquear pesos faltantes.
- [ ] **SHP-004 — Definir tiempo de preparación real** y días laborables/festivos.
- [~] **SHP-005 — Definir si se muestran fechas de entrega manuales** basadas en preparación y tránsito. La tienda usa actualmente fechas manuales; falta revisar sus valores.

### 7.2 Perfil general y zonas

- [~] **SHP-006 — Revisar el perfil de envío general** y confirmar qué productos contiene. Perfil general único, todos los productos, una sucursal y tres zonas. Antes de modificarlo, preguntar al cliente si configuró personalmente las zonas, tarifas, plazos y modalidades actuales; si no lo hizo o no está seguro, solicitar todos los datos logísticos documentados.
- [!] **SHP-007 — Crear zona España peninsular.** La zona actual `España` debe revisarse para conocer qué provincias incluye; no se considera aprobada.
- [!] **SHP-008 — Crear zona Baleares** si el coste o plazo difiere. Actualmente no existe una zona separada.
- [!] **SHP-009 — Crear zonas separadas para Canarias, Ceuta y Melilla** solo cuando estén aprobadas. Actualmente no existen zonas separadas.
- [~] **SHP-010 — Crear zona UE** solo al activar los países correspondientes en Mercados. Existe una zona UE con 26 países y tarifa de 8,99 €, pero está inoperativa por no existir mercado activo.
- [ ] **SHP-011 — Comprobar que ningún país aparece en dos zonas del mismo perfil.**
- [~] **SHP-012 — Excluir destinos a los que no se enviará.** Existe una zona internacional con 14 países y tarifa de 12,99 €, actualmente inoperativa por no pertenecer a un mercado activo; falta decidir si se conserva o elimina.

### 7.3 Tarifas y servicios

> No se revisarán ni modificarán más tarifas individualmente hasta recibir la validación conjunta del cliente, ya que todas utilizan los mismos campos básicos de configuración.

- [!] **SHP-013 — Introducir tarifa estándar de Península** basada en el contrato real. La configuración actual no se considera aprobada.
  - Valor actual: `Estándar`, tarifa fija de 4,95 €, sin condiciones por importe y con tránsito de 2 a 5 días hábiles. Puede ofrecerse también desde 50 € junto con la tarifa gratuita; preguntar si este solapamiento es intencionado y no modificarlo sin aprobación.
- [!] **SHP-014 — Configurar envío gratuito** solo a partir del umbral aprobado.
  - Valor actual: `Estándar`, por importe del pedido, mínimo 50,00 €, sin máximo, precio 0,00 € y sin tiempo de tránsito. Falta aprobar el umbral, definir el plazo mostrado y comprobar que la tarifa de 4,95 € termine en 49,99 €.
- [ ] **SHP-015 — Introducir tarifa de Baleares** y sus condiciones.
- [!] **SHP-016 — Introducir tarifas especiales** por peso o valor si son necesarias. `Recogida en Lovlory` es actualmente una tarifa fija de 3,95 €, sin condiciones visibles ni tiempo de tránsito; `Urgente` figura por 9,50 €. Ambas deben justificarse y validarse conjuntamente con el cliente antes de cualquier cambio.
- [~] **SHP-017 — Evaluar tarifa calculada por SEUR o aplicación del transportista** frente a tarifa plana. No hay ninguna cuenta de empresa de transporte conectada; aparecen Correos, SEUR y otra empresa entre las opciones de etiquetas.
- [~] **SHP-018 — Definir si habrá recogida local o puntos de recogida.** Entrega local, retiro en tienda y puntos de retiro están desactivados; falta confirmación comercial.
- [ ] **SHP-019 — Configurar seguro, seguimiento y firma** según valor de pedido.
- [ ] **SHP-020 — Definir procedimiento de dirección incorrecta, ausencia, reexpedición y paquete rechazado.**
- [ ] **SHP-021 — Definir embalaje discreto** y verificar que etiqueta, remitente y descriptor respeten la política de privacidad de marca.
- [ ] **SHP-022 — Definir proceso de devolución:** dirección, autorización, coste, inspección y reembolso.
- [ ] **SHP-023 — Completar información aduanera antes de vender internacionalmente.** Actualmente 0 de 196 variantes tienen país de origen y 0 de 196 tienen código del sistema armonizado (SA). No bloquea el lanzamiento exclusivamente nacional.

**Criterio de cierre del bloque:** cada territorio activo devuelve exactamente una opción válida de envío, con coste y plazo correctos.

## 8. Checkout y cuentas de cliente

- [~] **CHK-001 — Configurar contacto del cliente:** correo obligatorio; teléfono de envío opcional hasta confirmar si lo exige el transportista. Seguimiento mediante Shop activado y pendiente de validar por privacidad/discreción.
- [~] **CHK-002 — Revisar nombre, apellidos, empresa y segunda línea de dirección.** Nombre y apellidos obligatorios; segunda línea opcional; empresa y número de IVA ocultos mientras no se confirme venta B2B.
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

## Registro de incidencias

| ID | Fecha | Área / pedido | Descripción | Severidad | Responsable | Estado | Resolución |
|---|---|---|---|---|---|---|---|
| INC-001 | — | — | — | — | — | Abierta | — |

## Datos pendientes para comenzar

1. URL `*.myshopify.com` o URL de administración.
2. Razón social/autónomo, NIF/CIF y dirección fiscal.
3. Dirección y provincia desde la que salen los pedidos.
4. Transportista y tabla de tarifas contratadas.
5. Destinos de lanzamiento: Península, Baleares, Canarias, Ceuta/Melilla y/o UE.
6. Umbral comercial deseado para envío gratuito o datos para calcularlo.
7. Confirmación de la gestoría sobre IVA, OSS y territorios especiales.
8. Estado de Shopify Payments, PayPal y cualquier proveedor alternativo.
9. Plazo real de preparación de pedidos.
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
