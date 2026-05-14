# TopStyle — Estado del proyecto

> **Última actualización:** 13/05/2026 · **Checkpoint estable:** `J`
> Documento autosuficiente para retomar el proyecto en cualquier contexto.

---

## 1. Qué es

**TopStyle** es la distribuidora oficial de **Question Professional** (cosmética capilar) en Buenos Aires, propiedad de **Gabb**. Vende a peluquerías (mayorista) y al consumidor final.

El proyecto es un **sitio web vidriera + catálogo + checkout por WhatsApp** — no e-commerce con pagos online. La cliente arma su pedido en el sitio y se cierra la venta por chat.

**Datos de contacto del negocio:**
- Email: `topstyledistribuidora@gmail.com`
- WhatsApp: `+54 9 11 2739 5984` (formato internacional `5491127395984`)

---

## 2. Stack técnico

100% **estático**, monolítico.

| Capa | Tech |
|---|---|
| Frontend | HTML + CSS + Vanilla JS, todo en un solo archivo |
| Tipografías | Google Fonts: Playfair Display (display) + Inter (body) |
| Estado del cliente | `localStorage` (carrito, cupones, tema, fechas) |
| Auditoría avanzada | File System Access API + IndexedDB (Chrome) |
| Imágenes | Locales en `assets/`, base64 embebido en `review.html` |
| Hosting esperado | Cualquier static host (Netlify / Vercel / GitHub Pages / Cloudflare Pages) |
| Build | Ninguno — el archivo se sirve como está |

**Sin backend.** Cualquier feature que requiera persistencia compartida (cuentas, stock real-time, cupones únicos por persona, métricas propias) está fuera del alcance actual y queda anotada para cuando se sume backend / CRM.

**Versión recomendada de navegador:** Chrome / Edge (para File System Access API en `review.html`). El sitio principal funciona en todos.

---

## 3. Estructura de archivos

```
Topstyle/
├── index.html                     ← sitio completo (~240 KB, 6100+ líneas)
├── review.html                    ← herramienta de auditoría visual (regenerable)
├── PROJECT-STATE.md               ← este documento
├── TODO-mejoras.md                ← pendientes y log de sesiones
├── README.md                      ← descripción para humanos del proyecto
├── topstyle-catalogo-revision.xlsx ← (legacy, sin uso activo)
│
├── assets/
│   ├── logos/                     ← logos TopStyle + Question
│   ├── pdfs/                      ← color books Question (Lumiplex, Coloration), presentación
│   └── productos/
│       ├── *.jpg / *.png          ← fotos legacy del primer pase
│       ├── hd/                    ← fotos HD (segunda ronda)
│       ├── oficiales/             ← fotos oficiales (3a ronda)
│       ├── oficiales-v2/          ← FOTOS ACTUALES enlazadas en PRODUCTS (post-audits)
│       └── nuevas/                ← bandeja de entrada (audit la usa con FSA API)
│
├── _audit/
│   ├── build_review.py            ← genera review.html con estado actual del catálogo
│   ├── migrate_photos.py          ← busca fotos por nombre en mounts y las copia a oficiales-v2/
│   ├── feedback-2026-04-29.md     ← audit 1 (56 fotos, 7 quitar)
│   └── feedback-2026-05-04.md     ← audit 2 (22 fotos, 14 quitar, 1 rename)
│
└── _checkpoints/                  ← snapshots por hito
    ├── A/   ← inicial
    ├── B/   ← hero + carrusel auto-scroll + sidebar + pop-up bienvenida
    ├── C/   ← audit 1 aplicado (56 fotos)
    ├── D/   ← selector de color integrado
    ├── E/   ← confirmación selector de color
    ├── F/   ← email cableado
    ├── G/   ← audit 2 fotos (parcial)
    ├── H/   ← audit 2 cerrado al 100%
    ├── I/   ← categorías reorganizadas según Question
    └── index-pre-qr-panel.html  ← backup antes de integrar el panel pedido rápido (checkpoint J)
```

**Workspace montado en VM:** `/sessions/.../mnt/Topstyle/` ↔ `C:\Users\Gabb\.claude\Topstyle\`

**Carpetas auxiliares con acceso:**
- `Desktop\topstyle\INTELLIGENT SERIES\` — fotos oficiales del catálogo
- `Desktop\INTELLIGENT SERIES\` — copia / variantes
- `Downloads\` y subcarpetas (`Fotos Productos`, `Catalogos`, etc.)
- `Documents\`, `Pictures\`

---

## 4. Lo que está construido

### Navegación / Layout
- **Header / Hero** con logo agrandado, eyebrow "Representante oficial Question Professional · Buenos Aires", título grande con gradiente, CTAs y trust bar.
- **Switch claro/oscuro** en el nav (`#themeToggle`). Modo claro por omisión, oscuro como opción. Tema persistido en localStorage.
- **Sidebar lateral izquierda** desplegable: línea Question + accesos rápidos + WhatsApp.
- **Carrito drawer** lateral derecha con descuento, cupón, finalizar por WhatsApp.

### Bestsellers
- **Carrusel "Más vendidos"** con flechas overlay, auto-scroll cada 3.5 s, pausa en hover/touch/focus/visibility, loop al final, respeta `prefers-reduced-motion`.
- 7 productos curados (twelve-spray-210, is-keratin-lift-spray, is-lumiere-oleo, qstyle-curl-cream, qstyle-termic-protect, coloration-full-plex-60g, is-lumiere-ampollas).

### Categorías y catálogo
- Sección **#categorias** con 4 tarjetas siguiendo la estructura oficial Question:
  - Línea Coloración · Intelligent Series · Línea Styling · Línea Salón
- **Filter chips** arriba del grid de productos alineados con las mismas 4 líneas.
- Catálogo de **72 productos** (57 activos + 14 desactivados con `active: false`).
- Distribución: Coloración 12 · Intelligent 26 · Salón 24 · Styling 10.
- Cada producto: id, brand, name, description, category, price, image, badge, active.
- Filtrado por línea vía mapeo `PRODUCT_LINES` (prefijos de id) → `getProductLine(id)`.

### Selector de color (variantes)
- Modal completo (`#colorModalBg`) que se abre al hacer "Agregar" en `lumiplex-color-60g` y `coloration-full-plex-60g`.
- Buscador, filtros por familia, grid de tarjetas con swatch + código + nombre.
- Toggle "Varios tonos / 1 tono".
- Stepper de cantidad por tono seleccionado, total dinámico.
- Cada tono se agrega como **ítem separado** al carrito (con swatch + código + nombre visibles).
- **Paletas curadas:** `LUMIPLEX_PALETTE` (47 tonos) y `COLORATION_PALETTE` (~90 tonos) extraídas de los color books PDF oficiales. Hex de los swatches son aproximaciones — pendiente reemplazar por imágenes oficiales.

### Carrito
- Estructura de items: `{id, qty, variant?: {code, name, hex, line}}`.
- Coincidencia de items: por `id + variant.code` (mismo producto, distinto tono = ítems separados).
- Métodos: `add`, `update`, `remove`, `clear`, `count`, `subtotal`, `hasPrices`.
- Persistencia en `localStorage` bajo clave `topstyle_cart_v1`.
- **Cupones soportados:**
  - `BIENVENIDA10` — 10% off — vence 7 días desde primera visita
  - `TOPSTYLE15` — 15% off — mín $25.000 — sin expiración
  - `PRO20` — 20% off — mín $50.000 — sin expiración
- Input de cupón en el cart drawer ("¿Tenés un cupón?").
- Pop-up de bienvenida (`#welcomeModal`) auto-mostrado en primera visita con copy del código.
- Checkout: arma mensaje de WhatsApp con productos, cupón aplicado, total. Abre `wa.me/?text=...`.

### Auditoría visual (review.html)
- Generador en `_audit/build_review.py` que parsea el `PRODUCTS` actual y arma una página interactiva.
- Cada producto: thumbnail base64 + checkboxes (Quitar / Desactivar / Renombrar / Cambiar foto) + textarea de notas.
- **Auto-copiado de fotos** vía File System Access API:
  - Botón "Conectar carpeta nuevas/" pide permiso a la usuaria una vez.
  - Handle persistido en IndexedDB (sobrevive recargas; reotorga permiso con 1 click si caduca).
  - Al elegir foto en un producto, se copia automáticamente a `assets/productos/nuevas/<product-id>.<ext>`.
- Botón "🗑 Limpiar todo" para resetear sin perder la conexión.
- Botón "Exportar feedback" → texto formateado que se pega en chat.
- Migrate script (`migrate_photos.py`) busca cada foto referenciada por nombre en todas las carpetas montadas, las copia con nombre limpio a `oficiales-v2/`, y actualiza el campo `image:` en el array `PRODUCTS` del index.

### Otras secciones
- **Públicos** (peluquerías + consumidor final).
- **Acceso profesional** con form corto para mayoristas.
- **Cómo comprar** (paso a paso).
- **Contacto** con email + WhatsApp + dirección.
- **Footer** con info y links.
- **Toast** de confirmación al sumar al carrito.
- **WhatsApp button** flotante.
- **Panel Pedido Rápido** (`#qrPanel`) — sidebar derecha, trigger `#qrTrigger` fijo en el borde. 4 tabs (Coloración · Intelligent · Styling · Pileta/Salón), lista productos de la línea activa con imagen + nombre + precio + botón agregar/elegir color. Footer muestra total ítems y botón "Ver pedido →" que cierra el panel y abre el cart drawer. Z-index 155 (entre sidebar 150 y cart drawer 160). Código completamente dentro del IIFE existente en un bloque `{}`.

### Admin de cupones (`admin.html`)
- Panel dark para gestionar cupones sin tocar código.
- **Persistencia via localStorage** (`topstyle_coupons_admin`): sin File System Access API, sin permisos de archivo.
- Flujo: crear/editar/eliminar → guarda automático en localStorage.
- `index.html` lee `topstyle_coupons_admin` al iniciar y mergea sobre el `COUPONS` hardcodeado con `Object.assign`.
- Cupones soportados: % de descuento, mínimo de compra, vencimiento por días desde primera visita o por fecha fija, activar/desactivar.

---

## 5. Decisiones de diseño tomadas

### Paleta y look
- **Beauty / dark luxury → modo claro femenino**: blush · violeta mauve · champagne · plum profundo.
- **Modo claro por omisión** (vs el dark luxury inicial). El oscuro se mantiene como opción.
- **Tipografías**: Playfair Display (titulares) + Inter (UI / body).
- **Imágenes**: HD oficiales en formato cuadrado preferido. Las fotos verticales con ratio extremo se procesan con padding rosado claro (`#fcf6fa`) para que el `object-fit: cover` no las amplíe en exceso.

### UX
- **Selección múltiple por defecto** en el selector de color (cubre el caso 1-tono también con 1 click).
- **Carrito unificado**: pomos de color + shampoos + mascarillas + lo que sea, todo en un solo drawer.
- **Soft delete** (`active: false`) preferido sobre borrado físico — preserva datos para reactivar.
- **Cupones manuales** mientras no haya backend (códigos los pasa Gabb por WhatsApp a clientes correspondientes).
- **Pop-up de bienvenida** se muestra **una sola vez** (recordado en localStorage). No interrumpe en cada visita.
- **Auto-scroll del carrusel** se pausa en cualquier interacción humana y respeta `prefers-reduced-motion`.

### Escalabilidad sin backend
- Productos como array JS hardcoded → fácil de editar pero requiere edición de archivo.
- Cupones como objeto JS → idem; no son únicos por persona.
- Stock no validado → confirmación final por WhatsApp (Gabb verifica).
- Para escalar: migrar a backend o CMS (Shopify/Tiendanube/admin propio).

---

## 6. Workflows establecidos

### Agregar / cambiar / quitar productos masivamente (audit)

1. Gabb abre `review.html` (Chrome).
2. Conecta la carpeta `assets/productos/nuevas/` una vez (queda guardada en IndexedDB).
3. Marca por producto las acciones: Quitar, Desactivar, Renombrar, Cambiar foto.
4. Si conecta carpeta + cambia foto → la foto se copia automáticamente con nombre limpio.
5. Click "Exportar feedback" → texto formateado.
6. Pega el texto en chat.
7. Yo corro `migrate_photos.py` (busca fotos por nombre en todas las carpetas montadas si la auto-copia no funcionó), actualizo `index.html`, hago checkpoint.

### Agregar productos nuevos (workflow propuesto, pendiente)

1. Armo planilla Excel con columnas: id, brand, name, description, category, price, badge, archivo de foto.
2. Gabb carga los nuevos en bulk.
3. Yo ingiero la planilla → agrego al array `PRODUCTS` + copio fotos a `oficiales-v2/`.

### Restaurar un checkpoint

```bash
cp _checkpoints/I/index.html .
cp _checkpoints/I/review.html .
cp _checkpoints/I/TODO-mejoras.md .
```

---

## 7. Estado del catálogo (al checkpoint I)

| Línea | Productos | Activos |
|---|---|---|
| Coloración | 12 | 12 |
| Intelligent Series | 26 | 24 |
| Línea Salón | 24 | 14 |
| Línea Styling | 10 | 7 |
| **TOTAL** | **72** | **57** |

**Desactivados (14):** permanente-1/2/3-naturales/tenidos/decolorados-300, neutralizante-900, shampoo-neutro-4900, shampoo-frecuente-4900, theraphy-liss-kit/shampoo-480/alisador-480/mascara-480, silver-shampoo-960, qstyle-coolfix-gel, qstyle-oil-molecular-flex, ampollas-restauradoras.

**Bestsellers (7):** twelve-spray-210, is-keratin-lift-spray, is-lumiere-oleo, qstyle-curl-cream, qstyle-termic-protect, coloration-full-plex-60g, is-lumiere-ampollas.

**Precios:** lista oficial mayorista Question, abril 2026.

---

## 8. Restricciones técnicas conocidas

- **WebFetch bloqueado** para `questioncolor.com.ar` y dominios externos similares (egress proxy de Anthropic). Para usar referencias del sitio oficial: capturas de pantalla, HTML guardado, o descripción.
- **File pickers del navegador** no exponen rutas absolutas (limitación de seguridad). Solución: la auditoría usa File System Access API + handle persistido para que los archivos se copien directo. Si falla, el script `migrate_photos.py` busca por nombre en las carpetas montadas.
- **localStorage** ~5 MB de límite. Hoy usamos: cart, theme, welcome_seen, first_visit_at, active_coupon, review_v3 → margen amplio.
- **Borrado físico de productos** desaconsejado: usamos `active: false` para preservar IDs y datos.
- **Color swatches** son aproximaciones hex calculadas (no son los oficiales del color book PDF). Pendiente: extraer las imágenes oficiales del PDF y reemplazarlas.

---

## 9. Pendientes (TODO-mejoras.md)

### Datos pendientes de Gabb
- **Productos nuevos**: armar planilla Excel y cargar en bulk.
- **Segundo pase de auditoría**: si encuentra más cosas al usar el sitio.

### Mejoras de funcionalidad
- **Cupón frecuente automático**: check "Soy clienta frecuente" en form de pedido aplica `TOPSTYLE15` automático.
- **Captura de WhatsApp / lead-gen**: definir destino de los contactos (manual / Google Sheets / CRM).
- **Cupones con vigencia configurable**: hoy `BIENVENIDA10` vence relativo a primera visita; agregar opción de fecha fija.
- **Sidebar derecha — "Probá tu color"** (color preview AI): linkear a herramienta oficial Question, iframe, o API de terceros.

### Mejoras de diseño
- **Paleta noche más alegre** (sin prioridad — solo modo oscuro).
- **Swatches reales del color picker**: extraer imágenes oficiales del color book PDF y reemplazar los hex aproximados.

### Backend (cuando aplique)
- Cuentas de cliente / login para descuentos automáticos por historial.
- Stock por producto / por color.
- Panel de admin para Gabb (alta de productos sin tocar código).
- Procesamiento de pagos online.

---

## 10. Cómo retomar (cheat sheet para próxima sesión)

1. **Lee este archivo** — tenés todo el contexto.
2. **Lee `TODO-mejoras.md`** — pendientes priorizados.
3. **Verificá el estado actual**:
   ```bash
   ls _checkpoints/                    # último checkpoint
   wc -l index.html                    # tamaño actual
   python3 -c "import re; html=open('index.html').read(); m=re.search(r'const PRODUCTS = \[(.*?)\n    \];', html, re.DOTALL); print('productos:', len(re.findall(r\"id:\", m.group(1))))"
   ```
4. **Usá `migrate_photos.py`** para cualquier cambio de fotos en bulk.
5. **Antes de cambios destructivos**, hacé un nuevo checkpoint:
   ```bash
   mkdir -p _checkpoints/J
   cp index.html review.html TODO-mejoras.md _checkpoints/J/
   cp -r _audit _checkpoints/J/
   echo "# Checkpoint J — fecha\nDescripción..." > _checkpoints/J/CHECKPOINT.md
   ```
6. **Carpetas que conviene tener montadas** desde el primer prompt:
   - `C:\Users\Gabb\Desktop`
   - `C:\Users\Gabb\Downloads`
   - `C:\Users\Gabb\Documents`
   - `C:\Users\Gabb\Pictures`

   Se piden con el tool `request_cowork_directory(path=...)`.

---

## 11. Decisiones recientes (sesiones del 04/05/2026)

- ✅ Auditoría v2 aplicada al 100%: 22 fotos cambiadas + 8 desactivaciones nuevas + 1 rename + 1 reactivación.
- ✅ silver-shampoo-960 sacado del carrusel bestsellers (estaba desactivado).
- ✅ Fotos sobredimensionadas (volumizer-mascara, volume-fix, termic-protect) con padding 18% rosado claro.
- ✅ Categorías home + filter chips alineados con estructura Question (Coloración, Intelligent, Styling, Salón).
- ✅ Mapeo `PRODUCT_LINES` por prefijo de id — 72/72 productos clasificados automáticamente.
- ✅ `review.html` v3: persistencia IndexedDB del handle de carpeta + botón "Limpiar todo".

---

_Documento mantenido en sync con `_checkpoints/I/` (último estable). Si hacés cambios sustanciales, actualizá este archivo y bumpeá el checkpoint._
