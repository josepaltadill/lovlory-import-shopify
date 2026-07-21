# Datos pendientes de solicitar al cliente

Este documento registra únicamente la información que falta por solicitar o confirmar para configurar la tienda Shopify. No deben guardarse aquí datos personales completos, documentos de identidad, contraseñas ni información bancaria.

## Información comercial y del titular

- [ ] Confirmar que el titular desarrolla la actividad como autónomo individual y no mediante una sociedad (por ejemplo, SL o SLU).
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Tipo de empresa`.
- [ ] Solicitar el segundo apellido del titular, exactamente como aparece en su documentación oficial.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Nombre y apellidos`.
- [ ] Solicitar la fecha de nacimiento del titular, exactamente como aparece en su documentación oficial.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Fecha de nacimiento`.
- [ ] Confirmar que la dirección actual es: **Sant Cristòfol, 117, Despacho n.º 10, 43870 Amposta (Tarragona)**.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Dirección residencial`.
- [ ] Aclarar si esa dirección es también la dirección residencial acreditable del titular o solamente el domicilio profesional/fiscal, ya que el formulario de persona física de Shopify solicita la dirección residencial.
  - **Pantalla:** `Configuración > General > Información comercial > Editar información comercial > Dirección residencial`.

## Información fiscal

- [ ] Solicitar o confirmar el NIF de la autónoma (normalmente coincide con su DNI/NIE) y pedir a la gestoría el **número de IVA exacto que debe introducirse en Shopify**, incluido si debe usarse el formato `ES` + NIF. Confirmar también si está dada de alta en el ROI y aparece en VIES. No guardar el número completo en el repositorio.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Recauda el IVA en un país de la UE > España > Recaudar IVA > Número de IVA`.
- [ ] Confirmar con la gestoría si los precios de venta deben mostrarse con IVA incluido y el tipo de IVA aplicable al catálogo.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Configuración adicional > Incluir impuesto sobre las ventas en el precio del producto y la tarifa de envío` y `Mercados > España > Impuestos y aranceles > Visualización de impuestos`.
- [ ] Confirmar si la autónoma está inscrita en el régimen OSS o si inicialmente solo declarará ventas en España.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Recauda el IVA en ventas transfronterizas > Recaudar IVA`.
- [ ] Confirmar si utiliza un programa externo para emitir facturas o si desea activar las facturas con IVA automáticas de Shopify.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Facturas con IVA > Generar y mostrar facturas cuando se realicen pedidos`.
- [ ] Confirmar si la tienda venderá también a empresas y necesitará gestionar números de IVA de clientes, o si el lanzamiento será exclusivamente B2C.
  - **Pantalla:** `Configuración > Impuestos y aranceles > Unión Europea > Número de IVA de la empresa > Gestionar`.

## Preparación del correo

- [x] Solicitudes incorporadas al correo conjunto y enviadas a Lorena el 21 de julio de 2026.
- [ ] Registrar las respuestas de Lorena y actualizar cada bloque pendiente cuando las recibamos.

## Decisiones operativas por confirmar

- [x] Aprobado y configurado el formato de pedidos: **LV-1001, LV-1002, LV-1003…** (prefijo `LV-` y sufijo vacío).
  - **Pantalla:** `Configuración > General > Formato del ID del pedido`.

## Envío y preparación

> Toda la configuración encontrada en este apartado se considera **existente pero no validada**. El cliente debe confirmar expresamente cada valor, aunque ya aparezca configurado en Shopify.

> **Decisión de revisión:** no se abrirán ni modificarán más tarifas individualmente, ya que comparten los mismos campos de configuración. Se solicitará al cliente una validación conjunta de todas las modalidades, importes, condiciones y plazos actuales.

- [ ] Confirmar si el cliente configuró personalmente las zonas, tarifas, plazos y modalidades de envío que aparecen actualmente en Shopify, y si siguen siendo las condiciones comerciales que desea aplicar.
  - **Si la respuesta es sí:** pedirle que valide expresamente los valores actuales y aclare las incidencias señaladas debajo.
  - **Si la respuesta es no o no está seguro:** solicitar toda la información de este apartado antes de cambiar nada: origen de los pedidos, destinos, transportista, tabla de precios, umbral gratuito, modalidades, plazos, preparación, embalajes, recogida, devoluciones y condiciones especiales.
  - **Criterio de trabajo:** no modificar, eliminar ni activar ninguna tarifa o zona hasta recibir esta confirmación.
  - **Pantalla:** `Configuración > Envío y entrega` y `Configuración > Envío y entrega > Perfiles de envío > Perfil general`.

### Origen, sucursal y preparación

- [ ] Confirmar si la ubicación actual es realmente el lugar desde el que se almacenan, preparan y entregan los paquetes al transportista.
  - **Valor actual:** `C/ Sant Cristofol 117 puerta 10, 43870 Amposta, Tarragona, España`.
  - **Diferencia detectada:** en la información facilitada anteriormente figura `Sant Cristòfol, 117, Despacho n.º 10`.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Ubicación de procesamiento` y `Configuración > Sucursales`.
- [ ] Confirmar el nombre interno que debe tener la sucursal y si existe alguna otra ubicación con stock o desde la que se preparen pedidos.
  - **Pantalla:** `Configuración > Sucursales` y `Configuración > Envío y entrega > Perfil general > Ubicación de procesamiento`.
- [ ] Confirmar el plazo habitual de preparación antes de entregar el paquete al transportista.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas`.
- [ ] Confirmar días laborables, festivos, hora límite diaria y qué ocurre con los pedidos realizados después de esa hora.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas`.
- [ ] Confirmar si el plazo mostrado al cliente debe expresar solo el tránsito o la suma de preparación y tránsito.
  - **Pantalla:** `Configuración > Envío y entrega > Fechas de entrega estimadas` y `Perfil general > Editar opción de envío > Tiempo de tránsito`.

### Destinos y zonas

- [ ] Confirmar los destinos del lanzamiento por separado: España peninsular, Baleares, Canarias, Ceuta y Melilla.
  - **Valor actual:** existe una única zona llamada `España`, por lo que debemos verificar qué provincias incluye realmente.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zona España > Editar zona`.
- [ ] Confirmar si Baleares tendrá precios o plazos diferentes de la Península.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas de envío`.
- [ ] Confirmar si Canarias, Ceuta y Melilla deben quedar bloqueadas inicialmente o si se ofrecerán tarifas específicas con gestión aduanera.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas de envío` y `Mercados > España`.
- [ ] Confirmar si se venderá próximamente a otros países de la Unión Europea y qué países concretos se aprobarán.
  - **Valor actual:** existe una zona `UE (Unión Europea)` con 26 países/regiones y una tarifa de 8,99 €, pero no está habilitada porque esos países no pertenecen a un mercado activo.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > UE (Unión Europea)` y `Mercados`.
- [ ] Confirmar si se venderá fuera de la Unión Europea y qué países concretos se aprobarán.
  - **Valor actual:** existe una zona `Internacional` con 14 países/regiones y una tarifa de 12,99 €, pero no está habilitada porque esos países no pertenecen a un mercado activo.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Internacional` y `Mercados`.

### Tarifas nacionales encontradas

- [ ] Confirmar si el envío gratis debe aplicarse a pedidos de **50,00 € o más**.
  - **Valor actual:** `Estándar`, tarifa por importe del pedido, mínimo 50,00 €, sin máximo y precio 0,00 €.
  - **Plazo actual:** no tiene tiempo de tránsito configurado; Shopify avisa de que no mostrarlo puede afectar a la conversión. Confirmar qué plazo de entrega debe ver el cliente.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Estándar gratis > Editar opción de envío`.
- [ ] Confirmar el precio y las condiciones del envío estándar para pedidos inferiores al umbral gratuito.
  - **Valor actual:** `Estándar`, tarifa fija de 4,95 €, sin condiciones por importe y con tiempo de tránsito de 2 a 5 días hábiles.
  - **Incidencia a confirmar:** al no tener límite máximo, esta tarifa puede mostrarse también en pedidos de 50 € o más junto con la opción gratuita. Preguntar si ese comportamiento fue configurado de forma intencionada.
  - **Si no fue intencionado:** pedir que confirme si la tarifa de 4,95 € debe aplicarse únicamente a pedidos inferiores a 50 €, sin hacer el cambio hasta recibir su aprobación.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Estándar 4,95 € > Editar opción de envío`.
- [ ] Aclarar qué significa exactamente `Recogida en Lovlory`, quién presta el servicio, dónde recoge el cliente y por qué cuesta 3,95 €.
  - **Valor actual:** tarifa fija de 3,95 €, sin condiciones visibles por importe y sin tiempo de tránsito configurado. Aparece como tarifa de envío disponible para toda la zona España, mientras que `Retiro en tienda` y `Puntos de retiro` están desactivados.
  - **Incidencia a confirmar:** Shopify advierte de que no mostrar el tiempo de tránsito puede afectar a la conversión. Preguntar qué modalidad representa realmente y qué plazo debe mostrarse.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Recogida en Lovlory` y `Formas de entrega adicionales`.
- [ ] Confirmar si se ofrece realmente un servicio urgente, su transportista, precio, plazo, hora límite y destinos cubiertos.
  - **Valor actual:** `Urgente`, 9,50 €, sin plazo visible en el resumen.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > España > Urgente > Editar opción de envío`.
- [ ] Confirmar si los precios de transporte comunicados incluyen IVA y si coinciden con la política comercial y la facturación.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas y tarifas` y `Configuración > Impuestos y aranceles`.
- [ ] Confirmar si existen límites por peso, volumen, importe máximo, productos excluidos o recargos que deban reflejarse en las tarifas.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Editar opción de envío > Condiciones`.

### Transportista y condiciones del servicio

- [ ] Confirmar el transportista o transportistas contratados y facilitar la tabla vigente de precios por destino, peso y modalidad.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Zonas y tarifas` y `Cuentas de empresas de transporte`.
- [ ] Confirmar si las tarifas deben ser planas, calculadas en tiempo real por el transportista o gestionadas mediante una aplicación.
  - **Valor actual:** no hay ninguna cuenta de empresa de transporte conectada.
  - **Pantalla:** `Configuración > Envío y entrega > Cuentas de empresas de transporte`.
- [ ] Confirmar si el envío incluye seguimiento, seguro o firma y desde qué valor de pedido deben ser obligatorios.
  - **Pantalla:** `Configuración > Envío y entrega > Perfil general > Editar opción de envío > Detalles de entrega`.
- [ ] Confirmar los costes y el procedimiento para dirección incorrecta, ausencia, reexpedición, paquete rechazado, pérdida o daño.
  - **Pantalla relacionada:** `Configuración > Políticas` y `Configuración > Envío y entrega > Plantillas`.

### Paquetes y pesos

- [ ] Confirmar las dimensiones y el peso en vacío de la caja configurada actualmente.
  - **Valor actual:** existe una caja, pero todavía no se han revisado sus medidas ni su tara.
  - **Pantalla:** `Configuración > Envío y entrega > Paquetes`.
- [ ] Confirmar si se utilizan sobres, cajas adicionales o embalajes especiales y cuándo debe aplicarse cada uno.
  - **Pantalla:** `Configuración > Envío y entrega > Paquetes`.
- [ ] Confirmar que el embalaje será discreto y que no mostrará referencias al contenido del pedido.
  - **Pantalla relacionada:** `Configuración > Envío y entrega > Documentos > Nombre del remitente en las etiquetas de envío` y configuración de plantillas/etiquetas.
- [ ] Confirmar que los pesos de los productos corresponden al artículo preparado para el envío y si deben incluir embalaje individual adicional.
  - **Pantalla:** `Productos > Variante > Envío > Peso` y `Configuración > Envío y entrega > Paquetes`.

### Entrega, recogida y documentación

- [ ] Confirmar si se ofrecerá entrega local, retiro en tienda o puntos de retiro.
  - **Valor actual:** las tres opciones están desactivadas.
  - **Pantalla:** `Configuración > Envío y entrega > Formas de entrega adicionales`.
- [ ] Confirmar el nombre discreto que debe aparecer como remitente en las etiquetas de envío.
  - **Pantalla:** `Configuración > Envío y entrega > Documentos > Nombre del remitente en las etiquetas de envío`.
- [ ] Confirmar qué datos deben aparecer en la nota de entrega, factura y lista de picking, evitando contenido sensible innecesario.
  - **Pantalla:** `Configuración > Envío y entrega > Documentos > Plantillas`.
- [ ] Confirmar la dirección de devolución, quién asume el coste y las condiciones especiales para productos precintados por higiene.
  - **Pantalla:** `Configuración > Políticas > Política de devoluciones` y configuración operativa de devoluciones.

## Pagos

> Toda la configuración encontrada se considera **existente pero no validada**. No se activará ni conectará ningún proveedor hasta conocer quién realizó la configuración, confirmar la compatibilidad del catálogo y recibir autorización del cliente.

### Decisión general y elegibilidad

- [ ] Confirmar si el cliente configuró personalmente el apartado de pagos y si desea mantener las opciones que aparecen actualmente.
  - **Valor actual:** Shopify Payments está pendiente de completar; PayPal aparece con configuración incompleta y no se observa otro proveedor activo.
  - **Pantalla:** `Configuración > Pagos`.
- [ ] Solicitar al cliente que confirme por escrito con Shopify si Shopify Payments acepta el catálogo concreto de LovLory, descrito como venta de juguetes sexuales físicos y productos de bienestar íntimo.
  - **Motivo:** Shopify exige revisar la elegibilidad y sus categorías no son exhaustivas; no debemos completar el alta basándonos únicamente en que el botón esté disponible.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Más información / Completar configuración` y soporte de Shopify.
- [ ] Confirmar si el cliente quiere intentar usar Shopify Payments en caso de aprobación o si prefiere operar inicialmente solo con PayPal.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments`.
- [ ] Si Shopify Payments no acepta la actividad, confirmar qué proveedor alternativo compatible con el catálogo se utilizará para permitir pagos con tarjeta sin depender únicamente de PayPal.
  - **Pantalla:** `Configuración > Pagos > Ver todos los demás proveedores` y `Agregar proveedor`.

### Shopify Payments: datos necesarios solo si se aprueba

- [ ] Confirmar la condición de autónoma/persona física y que la titular reside en España.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Tipo de empresa`.
- [ ] Facilitar los datos de identidad y negocio que solicite la verificación: nombre legal completo, segundo apellido, fecha de nacimiento, NIF/NIE, domicilio y documentación acreditativa. Reutilizar los datos ya solicitados en Información comercial y no guardar documentos sensibles en el repositorio.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Información personal y comercial`.
- [ ] Facilitar una cuenta bancaria en euros compatible con transferencias SEPA, confirmar el IBAN y el nombre exacto de su titular. Transmitir estos datos por un canal seguro, no por este documento.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Completar configuración > Cuenta bancaria para pagos`.
- [ ] Confirmar el correo y teléfono que deben usarse para avisos de verificación, pagos, incidencias y contracargos.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Gestionar > Notificaciones y datos de la cuenta`.
- [ ] Confirmar el descriptor reconocible y discreto que debe aparecer en el extracto bancario del comprador.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Gestionar > Descriptor del extracto`.
- [ ] Revisar y aprobar las comisiones reales del plan, el calendario de liquidaciones, las reservas o retenciones y el procedimiento de contracargos antes de activar el proveedor.
  - **Valor mostrado actualmente:** tarifas de tarjeta anunciadas desde 2,1 % + 0,30 €; el coste definitivo debe verificarse para el plan y la cuenta de la tienda.
  - **Pantalla:** `Configuración > Pagos > Shopify Payments > Más información / Gestionar` y condiciones del proveedor.

### PayPal

- [ ] Confirmar que la cuenta PayPal usada actualmente en WordPress pertenece a la autónoma, es una cuenta Business española, está verificada y no tiene limitaciones.
  - **Pantalla:** `Configuración > Pagos > Proveedores de pagos adicionales > PayPal > Configuración incompleta` y cuenta de PayPal.
- [ ] Solicitar el correo exacto de la cuenta PayPal Business que debe conectarse y comprobar que coincide con una dirección verificada dentro de PayPal.
  - **Seguridad:** no solicitar ni guardar la contraseña ni códigos de doble autenticación; la propietaria de la tienda debe completar personalmente el acceso y la autorización.
  - **Pantalla:** `Configuración > Pagos > PayPal > Completar configuración`.
- [ ] Confirmar con PayPal que la cuenta puede procesar en Shopify el catálogo completo de LovLory y que el cambio desde WordPress no requiere una nueva revisión o autorización.
  - **Motivo:** que PayPal funcione actualmente en WordPress no garantiza por sí solo la aceptación de la nueva integración, del dominio o de todo el catálogo.
  - **Pantalla relacionada:** cuenta PayPal Business, centro de resoluciones y soporte de PayPal.
- [ ] Confirmar la cuenta bancaria de retirada, la divisa principal EUR, el nombre legal del titular y el país España.
  - **Pantalla:** cuenta PayPal Business y `Configuración > Pagos > PayPal`.
- [ ] Confirmar las comisiones vigentes de PayPal y aceptar el coste adicional de Shopify si no se usa Shopify Payments.
  - **Valor mostrado actualmente:** Shopify indica un 2 % de cargo por transacción de terceros, además de las comisiones de procesamiento de PayPal.
  - **Pantalla:** `Configuración > Pagos > Proveedores de pagos adicionales > PayPal`.
- [ ] Confirmar si PayPal debe permitir el pago con tarjeta como invitado, cuando esté disponible, para compradores que no tengan cuenta PayPal.
  - **Pantalla relacionada:** preferencias de pago de la cuenta PayPal Business y prueba del checkout de Shopify.
- [ ] Tras conectar PayPal, realizar una compra de prueba con una cuenta PayPal distinta de la cuenta receptora y comprobar cobro, cancelación, reembolso total y reembolso parcial.
  - **Pantalla:** tienda online, `Pedidos` y `Configuración > Pagos > PayPal`.

### Funcionamiento de los cobros

- [ ] Confirmar el método de captura actual y decidir si los pagos se cobran automáticamente al realizar el pedido o se revisan y capturan manualmente.
  - **Valor actual:** `Automáticamente en la pantalla de pago`; el cobro se captura cuando el cliente realiza el pedido.
  - **Confirmación necesaria:** preguntar si esta opción fue elegida por el cliente y si desea mantener el cobro inmediato. La captura manual exigiría actuar antes de que venza cada autorización. No cambiarla hasta conocer el flujo del cliente y el proveedor definitivo.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Método de captura de pago`.
- [ ] Confirmar si se aceptará alguna forma de pago manual, como transferencia bancaria o contra reembolso, y definir instrucciones, costes, plazo de reserva de stock y criterio para marcar el pedido como pagado.
  - **Valor actual:** no hay ninguna forma de pago manual activa; solo aparece la opción `Forma de pago manual` para añadir una.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Formas de pago manuales`.
- [ ] Revisar si existe alguna personalización de formas de pago creada por una aplicación y confirmar si debe conservarse.
  - **Valor actual:** no existe ninguna personalización de pago; Shopify muestra `Aún no has personalizado las formas de pago`.
  - **Criterio:** no instalar ninguna aplicación de personalización salvo que aparezca una necesidad comercial concreta.
  - **Pantalla:** `Configuración > Pagos > Configuración de pagos > Personalizaciones de las formas de pago`.
- [ ] Confirmar si LovLory venderá tarjetas de regalo. Solo en ese caso, decidir su vencimiento y si se habilitarán pases de Apple Wallet.
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
- [ ] Confirmar si LovLory utilizará crédito en tienda para reembolsos, fidelización o compensaciones.
  - **Valor actual:** activado; Shopify lo activa de forma predeterminada y permite que los clientes consulten y gasten los saldos emitidos.
  - **Comprobación necesaria:** revisar la política de emisión, vencimiento, contabilidad, reembolsos y posibles cargos por transacción antes de utilizarlo.
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

Última actualización: 21 de julio de 2026.
