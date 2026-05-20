# TopStyle — Lista de mejoras pendientes

Anotado el 21/04/2026. Última actualización: 14/05/2026.

---

## ✅ Hechas

### Sesión del 20/05/2026 (checkpoint K2)

- **COLORATION_PALETTE corregida al 100%**: 109 tonos oficiales en 29 familias, validado contra `Question_ColorBook (2025) DIGITAL` con Gabb.
  - Diff con la versión anterior:
    - **+19 tonos** agregados (Cenizas Irisados 8.11/9.11, Tonos Fríos 9.10/7.17/10.21/10.51, Marrones Cálidos 7.35, Tabacos 6.52/7.52/8.52, Marrones Elementales 5ME/6ME/7ME/8ME, Dorados Miel 8.32/10.32, Dorados Intensos 9.33, Cobres 8.34/9.34, Cobrizos Vibrantes 7.46V/8.43V, Rojos 7.62, Malvas 8.2/9.2, Aclarantes 10).
    - **−5 tonos eliminados** que no existían en el PDF oficial (7.13, 7.4, ME genérico, 0/0 Mix neutro, duplicados varios).
    - **Recategorizaciones**: 9.13/10.13 (Irisados → Dorados Beige), 5.62 (Caobas → Violáceos), 5.65/7.65 (Caobas → Rojos), 6.52/7.52 (Caobas → Tabacos), 6.23/7.23 (Marrones genéricos → Marrones Fríos), 5.35/6.35 (Marrones genéricos → Marrones Cálidos), 7.17 (Tabacos → Tonos Fríos como "Lead Ice").
    - **Renombres**: ajustados a nombres del PDF oficial (e.g. `912` = "Súper aclarante ceniza malva"; `9.31` = "dorado ceniza" no "beige"; `5MK/6MK` = "moka mousse"; etc.).
    - **Familias unificadas**: "Max Súper Aclarantes" fusionada en "Súper Aclarantes" (5 tonos); "Correctores" y "Mix" fusionados en "Mix Correctores" (6 tonos: Azul, Plata, Verde Mate, Violeta, Rojo, Dorado, sin prefijo).
- **Hex de swatches**: siguen siendo aproximaciones algorítmicas. Pendiente extraerlos del PDF (45/109 son rects planos detectables con pdfplumber; el resto son fotos embebidas que necesitan otro approach).

### Sesión del 13-14/05/2026 (checkpoint K)

- **Roadmap priorizado** (10 puntos) consensuado con Gabb. Orden: (1) strips por línea ✅, (2) selector de color v2, (3) UX tipo Meli iterativo, (4) lead capture (Web3Forms recomendado), etc.
- **4 strips por línea distribuidos en la home**:
  - Coloración antes de `#categorias`, Intelligent antes de `#productos`, Styling (fondo alt) antes de `#como-comprar`, Salón antes de `#pedido`.
  - Cards mini 130 → 145 → 160 px (mobile / tablet / desktop). Solo imagen + nombre 2 líneas + precio + botón "+" circular.
  - Auto-scroll continuo CSS (`@keyframes linear infinite`) a 55 px/s. Loop infinito por duplicación de contenido en JS.
  - Pausa en `:hover` y `:focus-within` puramente por CSS. Respeta `prefers-reduced-motion`.
  - Header con título + eyebrow + "Ver todo →" que filtra el catálogo abajo.
  - Hasta 18 productos por strip (`LINE_STRIP_MAX`).
- **Refactor del motor de auto-scroll**: migrado de `requestAnimationFrame` a CSS keyframes. Más simple y robusto.

### Sesión anterior
- **Botón deslizante de tema claro/oscuro** en el nav (al lado del carrito). Modo claro por omisión, manteniendo la paleta rosa / violeta / champagne. Tu preferencia se guarda y se respeta al volver a entrar.

### Sesión del 04/05/2026 (checkpoint I)
- **Categorías reorganizadas según estructura oficial Question**:
  - Tarjetas de la home: 5 genéricas → 4 líneas oficiales (Coloración, Intelligent Series, Styling, Salón).
  - Filter chips arriba del catálogo: alineados con las mismas 4 líneas.
  - Mapeo `PRODUCT_LINES` con prefijos de id que clasifica los 72 productos automáticamente.
  - Distribución: Coloración 12 · Intelligent 26 · Salón 24 · Styling 10.
- **Padding en fotos sobredimensionadas**: is-volumizer-mascara y qstyle-volume-fix con 18% margen rosado (la termic-protect ya estaba corregida en H).
- **review.html v3**:
  - Persistencia IndexedDB para que la conexión a la carpeta `nuevas/` sobreviva entre recargas (un click reactiva permiso si caduca).
  - Botón "🗑 Limpiar todo" en la toolbar para resetear feedback sin perder la conexión.

### Sesión del 04/05/2026 (checkpoints G + H)
- **Auditoría v2 aplicada en su totalidad**:
  - 22 fotos cambiadas (todas localizadas en `Desktop/topstyle/INTELLIGENT SERIES/` o `Desktop/INTELLIGENT SERIES/`).
  - 1 rename: `silver-acondicionador-960` → "Silver Acondicionador 160 ml".
  - 8 productos desactivados (soft delete `active: false`): los 4 Theraphy Liss, silver-shampoo-960, qstyle-coolfix-gel, qstyle-oil-molecular-flex, ampollas-restauradoras.
  - silver-shampoo-960 sacado del carrusel bestsellers (carrusel ahora con 7 productos).
  - is-keratin-lift-oleo reactivado con foto nueva.
  - Estado final: 71 totales, 57 activos, 14 desactivados.

### Sesión del 03/05/2026 (checkpoint F)
- **Email de contacto cableado**: `topstyledistribuidora@gmail.com` aplicado en sección de contacto y footer (`mailto:` + texto visible).

### Sesión del 30/04/2026 (checkpoint D)
- **Selector de color integrado al sitio real**:
  - Modal en `index.html` para `lumiplex-color-60g` y `coloration-full-plex-60g`.
  - Buscador, filtros por familia, selección múltiple con stepper de cantidad y total dinámico.
  - Toggle "Varios tonos / 1 tono" arriba a la derecha del modal.
  - Cada tono se guarda como ítem separado en el carrito (con swatch + código + nombre).
  - WhatsApp incluye `(tono X.X — Nombre)` por línea.
  - Mockup standalone preservado en `_mockups/color-picker.html` por si querés volver a comparar.
  - Pendientes menores: reemplazar swatches aproximados por imágenes oficiales del color book PDF + confirmar precios de los pomos en el array `PRODUCTS`.

### Sesión del 29/04/2026 (checkpoint C)
- **Auditoría visual aplicada en su totalidad**:
  - 7 productos QUITAR → desactivados (ocultos sin perder los datos).
  - 56/56 fotos del feedback localizadas en `Desktop/topstyle/INTELLIGENT SERIES/` (y carpetas adyacentes), copiadas a `assets/productos/oficiales-v2/` con nombres limpios y enlazadas en el `PRODUCTS` del index.
  - 3 productos Theraphy Liss reactivados (estaban desactivados pero la auditoría pidió foto nueva).
  - Estado final: 71 productos totales, 64 activos, 7 desactivados.

### Sesión del 23/04/2026 (checkpoint B)

- **1. Header / Hero**: subí el contenido ~28 px. Ahora la altura del nav pasó de 72 → 84 px y el logo de 60 → 72 px (desktop). Se redujo el espacio muerto arriba del hero así el título y el eyebrow "Representante oficial" entran sin scrollear.
- **3. Carrusel "Más vendidos"**:
  - Flechas ahora están **overlay sobre los productos** (no al costado afuera). Fondo blanco translúcido con blur, más femenino.
  - **Auto-scroll** cada 3.5 s hacia la derecha, con loop al llegar al final.
  - Pausa al pasar el mouse, al tocar (mobile), al foquear con teclado, cuando la pestaña queda en segundo plano, y cuando el carrusel sale del viewport.
  - Retoma automáticamente 6 s después de que el usuario deja de interactuar.
  - Respeta `prefers-reduced-motion` — si el usuario pidió menos animaciones, no auto-scrollea.
- **5. Sidebar**: panel lateral desplegable a la izquierda.
  - Trigger vertical sobre el borde izquierdo que dice "Menú rápido".
  - Al abrir: links a las 7 líneas Question (Coloration Full Plex, Lumiplex, Intelligent Series, Q Style, Acid Line, Theraphy Liss, Silver) + accesos rápidos (más vendidos, para quién, soy profesional, cómo comprar, contacto) + botón WhatsApp abajo.
  - Al tocar una línea, filtra el catálogo por esa línea y cierra la sidebar.
  - Cierra con botón, backdrop o tecla Escape.
- **6. Descuentos y fidelización**:
  - **Pop-up de bienvenida** con código `BIENVENIDA10` (10 % OFF), válido 7 días desde la primera visita. Se muestra una sola vez (se recuerda en el navegador).
  - **Botón "Copiar"** del código con feedback visual.
  - **Input de cupón en el carrito** (sección desplegable "¿Tenés un cupón?").
  - Cupones disponibles:
    - `BIENVENIDA10` → 10 % off (con expiración)
    - `TOPSTYLE15` → 15 % off para clientas frecuentes (mínimo $25.000)
    - `PRO20` → 20 % off para peluquerías (mínimo $50.000)
  - El descuento se muestra como línea aparte en el resumen del carrito y se incluye en el mensaje que se manda por WhatsApp al finalizar pedido.

---

## 📋 Por hacer

### A. Datos pendientes de tu lado

#### A1. Segundo pase de auditoría visual
- Gabb va a hacer otra ronda de revisión sobre el sitio en su estado actual (post-checkpoint F).
- Cuando tilde "cambiar foto" en un producto, el archivo lo selecciona desde su PC. Aclaración técnica: el navegador me da **el nombre del archivo, no la ruta completa** (restricción de seguridad).
- **Workflow** (igual que el de sesión 29/04): con acceso a `Desktop`, `Downloads`, `Documents` y `Pictures`, mi script `_audit/migrate_photos.py` busca el archivo por nombre en todas esas carpetas, lo copia a `assets/productos/oficiales-v2/<product-id>.<ext>` con nombre limpio, y actualiza el `image:` en el `PRODUCTS` del index. Tolera variantes de nombre (espacios, mayúsculas, acentos).
- Pendiente próxima sesión: que Gabb me pase el feedback nuevo y corro el script.

#### A2. Productos nuevos — planilla
- Listado de productos para agregar al catálogo. Voy a armar una **planilla Excel** con las columnas: id, brand, name, description, category, price, badge, archivo de foto. Vos cargás los datos, me la pasás, y los meto en bulk.

### B. Mejoras de diseño

#### B1. Paleta noche (sin prioridad)
- Aclarar un poco el tono — versión más alegre / luminosa. **Solo para la versión noche.** Cuando quieras pruebo 2-3 variantes alternativas y elegís.

#### B2. Grilla de productos al estilo questioncolor.com
- **Bloqueado por mi acceso**: no puedo navegar el sitio oficial (proxy bloqueado). Para destrabarlo necesito uno de estos tres:
  1. Capturas de pantalla (home, grilla del shop, una tarjeta individual, header).
  2. Bullets con 5-8 detalles concretos que te gusten.
  3. La página guardada como HTML (Ctrl+S → "Página web, solo HTML") tirada en la carpeta `Topstyle/`.

### C. Funcionalidad

#### C0. Selector de color — pendiente menor
- **Swatches reales**: extraer las imágenes oficiales de los color books PDF (Lumiplex y Coloration) y reemplazar los hex aproximados.
- **Precios de los pomos**: confirmar que el precio en `PRODUCTS` para `lumiplex-color-60g` y `coloration-full-plex-60g` está correcto.
- (Funcionalidad principal ya integrada en checkpoint D — ver arriba.)

#### C0b. Captura de WhatsApp / lead generation
- Incentivar a las consumidoras a dejar el contacto para enviarles promos, cupones, regalos.
- Ideas a evaluar (combinables):
  1. **Pop-up de bienvenida** ya activo — sumarle campo de WhatsApp opcional.
  2. **Banner sticky** en la home: "Sumate al newsletter de TopStyle y recibí un cupón de bienvenida".
  3. **Pantalla intermedia antes del checkout**: "Antes de mandar el pedido, ¿querés recibir promos por WhatsApp?".
  4. **Sección dedicada** en la home: "Comunidad TopStyle — ofertas exclusivas para suscriptoras".
  5. **Cupón a cambio de WhatsApp**: el `BIENVENIDA10` pasa de ser auto-revelado a aparecer recién después de dejar el contacto.
- **Decisión necesaria**: ¿adónde van esos contactos? Tres opciones:
  - **Vos las recibís por WhatsApp / email tuyo manualmente** (simplísimo, 0 backend).
  - **Hoja de cálculo Google Sheets** que se llena solo (medio: necesitamos un endpoint).
  - **CRM dedicado** (Mailchimp, Brevo, ActiveCampaign — varían precio).

#### C1. Cupón frecuente automático
- Propuesta: agregar en el formulario de pedido un check **"Soy clienta frecuente"** → si tilda, aplica `TOPSTYLE15` automático sin que tenga que tipear el código.
- Pendiente: confirmar si te sirve esa solución o querés algo distinto.

#### C1b. Sidebar derecha — "Probá tu color" (color preview AI)
- Reservar el otro lado del menú rápido (lado derecho) para una herramienta de probar tonos sobre una foto.
- Como Question tiene esa funcionalidad en su sitio oficial, las opciones son:
  1. **Linkear directo** a la herramienta de Question si tiene URL pública (lo más rápido, 0 esfuerzo).
  2. **Iframe-embebido** dentro del sitio (depende de los headers de questioncolor.com.ar).
  3. **API de terceros** (Modiface, Perfect Corp) — tiene costo mensual.
- **Pendiente**: que Gabb confirme cómo funciona la herramienta oficial (URL, si pide registro, etc.). Más adelante.

#### C2. Cupones con vigencia configurable
- Hoy `BIENVENIDA10` vence a los 7 días desde la primera visita.
- Si querés crear cupones con **fecha fija** (ej: "válido hasta 31/05/2026") o cupones temáticos (Día de la Madre, Black Friday, etc.), me decís nombre + % + fecha de cierre.

---

_Decime por dónde arrancamos._
