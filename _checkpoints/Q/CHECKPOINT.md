# Checkpoint Q — V1 rev2 (listo para 2ª revisión)

**Fecha inicial:** 2026-06-23 · **Commit base:** c1a8c81
**Última actualización:** 2026-06-24 · **Commit:** aa1e272
**Estado:** Post-revisión Ari + hero above-the-fold — en producción

---

## ✦ Sub-hito Q2 — Hero above-the-fold desktop (2026-06-24)

Commit `aa1e272` — Hero compacto para desktop: todo el contenido visible en la primera pantalla sin scroll.

- Grid hero: `align-items: stretch` — columna izquierda se estira al alto del logo
- Columna izquierda: `flex-direction: column`
- Título: hasta **80px** (`clamp(40px, 6.2vw, 80px)`)
- Lead: **18px**, `line-height: 1.55`
- Botones: `margin-top: auto` — flotan debajo del texto, separados naturalmente
- Stats: se anclan al pie del logo
- Solo afecta desktop (`min-width: 960px`), mobile sin cambios

---

## Qué hay en este checkpoint

### Cambios sobre Checkpoint P

**Copy / textos:**
- "Buenos Aires" eliminado del hero lead
- Stat → "años asesorando a profesionales"
- Stats hero: "Despachos en el día", "Envíos a todo el país", "Asesoramiento técnico para profesionales", "precios promocionales" (2 instancias)

**Layout / UX:**
- Hero trust: 3 stats siempre en la misma línea horizontal (flex:1 en trust-item)
- Banners: click navega a la sección del slide (wasSwipe flag, BANNERS[current].link)
- Flechas del banner no disparan navegación de sección

**Catálogo — distribuidor:**
- Chip "Twelve Spray" eliminado de la card distribuidor
- "Silver · matizador" renombrado a "Línea Salón"

**Catálogo — productos:**
- Card Twelve Spray: agregada (faltaba, tenía banner)
- Foto Lumiplex 3 Vol: reemplazada (pomo → frasco correcto)
- Nuevos: Lumiplex 19 Vol 900ml, Crema Enjuague 900ml, Máscara Post Color 1000ml y 250ml
- Finish Spray: dividido en Normal y Fuerte con fotos propias

**Imágenes cards:**
- mascara-capilar-250: object-fit cover anclado abajo (pote visible, sin espacio vacío arriba)
- mascara-capilar-post-color-250: ídem

---

## Todo lo incluido desde Checkpoint P

- F1 Banner carrusel 6 slides (auto-scroll 1800ms, flechas, dots, drag/swipe)
- F2 Sección "Los más elegidos" — 4 productos curados
- F3a Foto shoppable IS con 7 pins por sub-línea
- F3b Catálogo IS agrupado por sub-línea
- F3a-IR Kits Intensive Repair (Chico y Grande)
- QR Panel — drawer lateral con tabs por línea
- Carrito + cupones + checkout WhatsApp
- PEC: cupones segmentados por línea (LANZA35OFF: 35% IS)
- Email: hola@topstyle.com.ar + ventas@topstyle.com.ar
- admin.html con gestión de cupones y checkboxes de líneas

---

## Deploy
- **URL:** https://topstyle.com.ar
- **Hosting:** Cloudflare Pages
- **Repo:** github.com/gabrielalninogago-ship-it/topstyle-website

---

## Pendiente (V2)
- P1 Beauty Color
- Test mobile real en dispositivo físico
- Precios julio 2026 (script listo en `_audit/update_prices_from_pdf.py`)
