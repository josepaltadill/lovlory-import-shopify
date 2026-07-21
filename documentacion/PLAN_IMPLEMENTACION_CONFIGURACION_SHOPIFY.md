# Plan maestro de configuración Shopify — LovLory

**Versión:** 1.0  
**Fecha de referencia:** 21 de julio de 2026  
**Ámbito:** configuración general, fiscal, operativa y de lanzamiento de la tienda Shopify de LovLory  
**Estado global:** `[ ] Pendiente de iniciar`

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
| 0 | Decisiones previas | Pendiente | Por asignar | — |
| 1 | Seguridad, empresa y facturación | Pendiente | Por asignar | — |
| 2 | Datos generales | Pendiente | Por asignar | — |
| 3 | Mercados, moneda e idiomas | Pendiente | Por asignar | — |
| 4 | Impuestos | Pendiente | Por asignar | — |
| 5 | Pagos | Pendiente | Por asignar | — |
| 6 | Ubicaciones e inventario | Pendiente | Por asignar | — |
| 7 | Transporte y preparación | Pendiente | Por asignar | — |
| 8 | Checkout y cuentas de cliente | Pendiente | Por asignar | — |
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
- [ ] **GEN-003 — Zona horaria:** `Europe/Madrid`.
- [ ] **GEN-004 — Unidades:** sistema métrico; peso en kg/g y dimensiones en cm.
- [ ] **GEN-005 — Moneda de la tienda:** EUR.
- [ ] **GEN-006 — Correo de contacto:** cuenta activa y atendida del dominio de LovLory.
- [ ] **GEN-007 — Correo del remitente:** autenticarlo para reducir entregas en spam.
- [ ] **GEN-008 — Formato de número de pedido:** mantener uno corto, inequívoco y estable; documentar prefijo o sufijo si se cambia.
- [ ] **GEN-009 — Datos de contacto para clientes:** correo, teléfono o formulario accesible desde el pie de página.
- [ ] **GEN-010 — Revisar favicon, logotipo y nombre del remitente** en todos los puntos visibles.

**Criterio de cierre del bloque:** los datos mostrados, fiscales, bancarios y de contacto no se contradicen.

## 3. Mercados, moneda e idiomas

Ruta orientativa: **Mercados**.

### 3.1 Mercado de lanzamiento

- [ ] **MKT-001 — Crear o revisar el mercado España.**
- [ ] **MKT-002 — Establecer EUR** como moneda del mercado español.
- [ ] **MKT-003 — Activar español** como idioma principal y revisar que tema, checkout y políticas estén traducidos.
- [ ] **MKT-004 — Confirmar disponibilidad del catálogo** para el mercado español.
- [ ] **MKT-005 — Verificar que cada país activo tenga una zona de envío válida.** Un mercado activo sin tarifa puede impedir la compra.

### 3.2 Territorios con tratamiento específico

- [ ] **MKT-006 — Separar Canarias** de Península/Baleares hasta validar IGIC, aduanas, DUA, plazos y transportista.
- [ ] **MKT-007 — Separar Ceuta y Melilla** hasta validar IPSI, aduanas, plazos y transportista.
- [ ] **MKT-008 — Decidir si Baleares tendrá tarifa propia** según el contrato logístico.
- [ ] **MKT-009 — Probar que una dirección no cubierta recibe un mensaje correcto** y no una tarifa errónea.

### 3.3 Expansión a la Unión Europea

- [ ] **MKT-010 — Mantener inactivos los países no preparados** fiscal o logísticamente.
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
- [ ] **TAX-002 — Añadir el registro español de IVA** con el identificador real del negocio.
- [ ] **TAX-003 — Elegir servicio fiscal.** Para tiendas nuevas en la UE desde el 13 de mayo de 2026, revisar Shopify Tax frente a configuración manual, incluyendo coste y necesidades de factura.
- [ ] **TAX-004 — Configurar precios con IVA incluido** para venta B2C en España, si la gestoría lo confirma.
- [ ] **TAX-005 — Confirmar el tratamiento fiscal de los gastos de envío.**
- [ ] **TAX-006 — Revisar la categoría fiscal de cada producto** y evitar anulaciones globales sin justificación.
- [ ] **TAX-007 — Revisar regalos, descuentos y códigos promocionales** con impuestos incluidos.
- [ ] **TAX-008 — Configurar Canarias, Ceuta y Melilla** solo tras recibir instrucciones fiscales y logísticas específicas.
- [ ] **TAX-009 — Registrar la decisión sobre OSS.** El umbral conjunto de ventas B2C intracomunitarias a distancia es de 10.000 € sin IVA en las condiciones descritas por la AEAT.
- [ ] **TAX-010 — Configurar facturas con IVA** o la solución de facturación que utilice la empresa.
- [ ] **TAX-011 — Ejecutar pedidos fiscales de prueba:** Península, Baleares y, si están activos, UE/Canarias/Ceuta/Melilla.
- [ ] **TAX-012 — Comparar el cálculo de Shopify con un cálculo manual** y obtener aprobación de la gestoría.

**Criterio de cierre del bloque:** registros fiscales correctos, precios coherentes y al menos un pedido de prueba aprobado por territorio activo.

## 5. Pagos

Ruta orientativa: **Configuración > Pagos**.

### 5.1 Elegibilidad y alta

- [ ] **PAY-001 — Confirmar por escrito la elegibilidad del catálogo** con el proveedor de pagos. Describirlo como venta de juguetes sexuales físicos y bienestar íntimo.
- [ ] **PAY-002 — Evitar contenido sexual explícito, servicios sexuales y afirmaciones médicas no demostradas** en páginas revisadas por el procesador.
- [ ] **PAY-003 — Publicar contacto, entrega, devolución, desistimiento y descripciones completas** antes de solicitar o completar la revisión.
- [ ] **PAY-004 — Activar Shopify Payments solo si se aprueba la actividad.**
- [ ] **PAY-005 — Verificar identidad y empresa** con datos idénticos a la documentación oficial.
- [ ] **PAY-006 — Conectar cuenta bancaria en EUR compatible con SEPA.** No usar una cuenta de ahorro ni una cuenta multidivisa no admitida.
- [ ] **PAY-007 — Definir un proveedor alternativo compatible** para reducir riesgo operativo si el principal limita la cuenta.

### 5.2 Métodos y operativa

- [ ] **PAY-008 — Activar tarjetas admitidas** y comprobar 3D Secure.
- [ ] **PAY-009 — Activar Apple Pay, Google Pay y Shop Pay** si están disponibles y aprobados.
- [ ] **PAY-010 — Revisar PayPal**: titular, correo, cuenta bancaria, divisa y política de protección.
- [ ] **PAY-011 — No activar Klarna u otros métodos aplazados** hasta confirmar compatibilidad con todo el catálogo y condiciones de la tienda.
- [ ] **PAY-012 — Configurar descriptor bancario reconocible** para reducir contracargos, si el proveedor lo permite.
- [ ] **PAY-013 — Definir captura de pagos:** automática como opción inicial, salvo que el flujo operativo requiera revisión manual.
- [ ] **PAY-014 — Revisar pagos, comisiones, conversión y calendario de liquidaciones.**
- [ ] **PAY-015 — Configurar alertas de fraude y revisión manual** de pedidos de riesgo alto.
- [ ] **PAY-016 — Realizar transacción de prueba, reembolso total y reembolso parcial.**
- [ ] **PAY-017 — Confirmar recepción de una liquidación real pequeña** antes del lanzamiento completo.

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

- [ ] **SHP-001 — Confirmar origen de envío** y horario de recogida.
- [ ] **SHP-002 — Crear paquetes habituales** con dimensiones y tara reales.
- [ ] **SHP-003 — Confirmar peso de todos los productos físicos.** Usar los datos reales del CSV final y bloquear pesos faltantes.
- [ ] **SHP-004 — Definir tiempo de preparación real** y días laborables/festivos.
- [ ] **SHP-005 — Definir si se muestran fechas de entrega manuales** basadas en preparación y tránsito.

### 7.2 Perfil general y zonas

- [ ] **SHP-006 — Revisar el perfil de envío general** y confirmar qué productos contiene.
- [ ] **SHP-007 — Crear zona España peninsular.**
- [ ] **SHP-008 — Crear zona Baleares** si el coste o plazo difiere.
- [ ] **SHP-009 — Crear zonas separadas para Canarias, Ceuta y Melilla** solo cuando estén aprobadas.
- [ ] **SHP-010 — Crear zona UE** solo al activar los países correspondientes en Mercados.
- [ ] **SHP-011 — Comprobar que ningún país aparece en dos zonas del mismo perfil.**
- [ ] **SHP-012 — Excluir destinos a los que no se enviará.**

### 7.3 Tarifas y servicios

- [ ] **SHP-013 — Introducir tarifa estándar de Península** basada en el contrato real.
  - Nombre mostrado: ____________________  Precio: ____________________  Plazo: ____________________
- [ ] **SHP-014 — Configurar envío gratuito** solo a partir del umbral aprobado.
  - Umbral: ____________________  Zona: ____________________
- [ ] **SHP-015 — Introducir tarifa de Baleares** y sus condiciones.
- [ ] **SHP-016 — Introducir tarifas especiales** por peso o valor si son necesarias.
- [ ] **SHP-017 — Evaluar tarifa calculada por SEUR o aplicación del transportista** frente a tarifa plana.
- [ ] **SHP-018 — Definir si habrá recogida local o puntos de recogida.**
- [ ] **SHP-019 — Configurar seguro, seguimiento y firma** según valor de pedido.
- [ ] **SHP-020 — Definir procedimiento de dirección incorrecta, ausencia, reexpedición y paquete rechazado.**
- [ ] **SHP-021 — Definir embalaje discreto** y verificar que etiqueta, remitente y descriptor respeten la política de privacidad de marca.
- [ ] **SHP-022 — Definir proceso de devolución:** dirección, autorización, coste, inspección y reembolso.

**Criterio de cierre del bloque:** cada territorio activo devuelve exactamente una opción válida de envío, con coste y plazo correctos.

## 8. Checkout y cuentas de cliente

- [ ] **CHK-001 — Configurar contacto del cliente:** decidir correo como dato principal y teléfono opcional u obligatorio según transporte.
- [ ] **CHK-002 — Revisar nombre, apellidos, empresa y segunda línea de dirección.** Pedir solo datos útiles.
- [ ] **CHK-003 — Activar validación de dirección** si está disponible y probar códigos postales especiales.
- [ ] **CHK-004 — Decidir si las cuentas de cliente son opcionales.** Recomendación inicial: permitir compra como invitado.
- [ ] **CHK-005 — Revisar consentimiento de marketing** separado de la aceptación necesaria para completar la compra.
- [ ] **CHK-006 — Configurar recuperación de checkout abandonado** y revisar su texto, plazo y descuentos.
- [ ] **CHK-007 — Revisar propinas, venta adicional y aplicaciones del checkout.** Desactivar elementos no necesarios.
- [ ] **CHK-008 — Revisar mensaje de error cuando un destino no tiene envío.**
- [ ] **CHK-009 — Personalizar página de agradecimiento y estado del pedido** sin scripts obsoletos.
- [ ] **CHK-010 — Verificar privacidad del contenido del paquete y comunicaciones** de cara al cliente.

**Criterio de cierre del bloque:** un cliente nuevo puede comprar sin fricción, entiende los consentimientos y recibe información de entrega correcta.

## 9. Políticas, privacidad y cumplimiento

> Las plantillas de Shopify son un punto de partida. Deben revisarse para el negocio, el catálogo y la normativa aplicable.

- [ ] **LEG-001 — Aviso legal:** titular, NIF/CIF, domicilio y contacto.
- [ ] **LEG-002 — Condiciones de compra:** formación del contrato, precio, pago, entrega, incidencias y jurisdicción.
- [ ] **LEG-003 — Política de envíos:** zonas, costes, preparación, tránsito, seguimiento e incidencias.
- [ ] **LEG-004 — Política de devoluciones y reembolsos:** plazos, proceso, costes y estado del producto.
- [ ] **LEG-005 — Validar con asesoría la excepción de desistimiento por higiene** para bienes precintados que no sean aptos para devolución tras desprecintarse; explicarla claramente antes de la compra.
- [ ] **LEG-006 — Política de privacidad:** responsables, finalidades, bases, proveedores, conservación y derechos.
- [ ] **LEG-007 — Política de cookies y banner de consentimiento** adaptados a las herramientas realmente instaladas.
- [ ] **LEG-008 — Información de contacto y reclamaciones** accesible desde el pie de página.
- [ ] **LEG-009 — Revisar textos de mayoría de edad y acceso al catálogo** con asesoría; no usar una barrera de edad como sustituto de cumplimiento.
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
- Shopify, guía para vender juguetes sexuales: <https://www.shopify.com/blog/sell-sex-toys>
- Agencia Tributaria, tipos de IVA: <https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-04-sujetos-pasivos-repercusion-impositivo/tipo-impositivo.html>
- Agencia Tributaria, ventas a particulares de otros Estados miembros: <https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/ventas-particulares-otros-estados-miembros-ue.html>

---

**Próximo paso recomendado:** completar el bloque 0. Con esas decisiones se podrán establecer valores reales en Shopify sin rehacer después impuestos, mercados o tarifas de envío.
