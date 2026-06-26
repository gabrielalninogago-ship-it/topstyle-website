# Checkpoint R — Hito R SPEC V1.1 DESKTOP ✅

**Fecha cierre:** 2026-06-25
**Commit final:** f7d4467

## Bloques cerrados

### Block 1 — Card Asesoramiento ✅
Card nueva en sección Contacto, abre modal con info del servicio.

### Block 2 — Catálogo plegable agrupado por línea ✅
Acordeón colapsable por línea, botón "Ver catálogo completo / Cerrar catálogo".

### Block 3 — Ordenar productos ✅
Dropdown "Ordenar:" visible solo en filtro Todos.
- Al elegir un orden → auto-expande el catálogo
- Al cambiar a categoría → resetea orden a "Destacados"
- Opciones visibles con colores hex explícitos (fix listbox nativo)

### Block 4 — Sistema de banners administrable ✅
- F1 carrusel lee banners.json via fetch + fallback hardcodeado (6 slides)
- Franja cupón: 2 banners en grid 2 columnas (lanzamiento + mundial)
  - height:auto sin crop — imágenes completas
  - Barra inferior oscura con botón (cupón o link)
  - Botón "Usar cupón" → abre carrito + aplica LANZA35OFF automáticamente
- admin.html: CRUD banners con export a banners.json
  - DEFAULT_BANNERS incluye b7 (franja lanzamiento) y b8 (franja mundial)
- _headers: Cache-Control no-cache para evitar versiones viejas en Cloudflare

### Block 5 — Admin productos destacados ✅
97 productos catalogados, reorder por drag/flechas, export a destacados.json.
index.html lee destacados.json via fetch con fallback hardcodeado.

### Bonus — Cupón bienvenida ✅
DEFAULT_COUPONS: BIENVENIDA10 → LANZA35OFF (35%, sin vencimiento),
alineado con el banner de lanzamiento.

## Archivos en este checkpoint
- index.html — site completo (commit f7d4467)
- admin.html — panel admin completo (commit f7d4467)
- CHECKPOINT.md — este archivo

## Archivos clave en repo (no incluidos aquí)
- banners.json — 8 banners (b1-b8)
- assets/banners/07_topstyle_lanzamiento.png
- assets/banners/08_topstyle_mundial.png
- _headers — Cache-Control para Cloudflare Pages
