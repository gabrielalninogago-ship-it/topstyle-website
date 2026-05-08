# TopStyle — Sitio web

Sitio estático de **TopStyle**, distribuidora oficial de **Question Professional** en Buenos Aires.
Un único `index.html` con todo el CSS y JS embebidos. Sin dependencias, sin build, sin frameworks.

WhatsApp configurado: **+54 9 11 2739-5984** (`5491127395984`).

---

## Estructura de carpetas

```
topstyle/
├── index.html                    ← sitio completo (HTML + CSS + JS)
├── README.md                     ← este archivo
└── assets/
    ├── logos/
    │   ├── topstyle-logo-tight.png   ← variante usada en el sitio (recortada al contenido)
    │   ├── topstyle-logo-mark.png    ← sólo el medallón (reserva)
    │   ├── topstyle-logo-dark.png    ← original 1024x1024 fondo negro (respaldo)
    │   ├── topstyle-logo-light.png   ← versión para fondos claros
    │   └── topstyle-logo-texture.png ← versión con fondo texturado
    └── productos/                ← fotos de productos Question
        ├── coloration.jpg
        ├── lumiplex-color.jpg
        ├── oxidantes.jpg
        ├── revelador-40vol.jpg
        ├── polvo-decolorante.jpg
        ├── mint-power-plex.jpg
        ├── white-power-plex.jpg
        ├── permanentes.jpg
        ├── ampollas-restauradoras.jpg
        ├── twelve.jpg
        ├── shampoo-linea.jpg
        ├── silver-linea.jpg
        ├── mascara-capilar.jpg
        ├── acid-line.jpg
        ├── theraphy-liss.jpg
        ├── qstyle-*.jpg          (10 productos Q Style)
        ├── is-*.jpg              (8 líneas Intelligent Series)
        └── presentacion-pg-*.jpg (21 páginas del catálogo oficial 2026)
```

Las fotos fueron extraídas del **catálogo oficial Question Professional 2026** que me pasaste.
Son crops centrados sobre cada producto — algunos todavía tienen texto residual en los bordes. Cuando tengas fotos mejores de la web oficial, Instagram o producción propia, simplemente reemplazás el archivo en `assets/productos/` manteniendo el mismo nombre y listo.

---

## Cómo deployar

**Netlify (recomendado, 30 segundos):**
1. Entrá a https://app.netlify.com/drop
2. Arrastrá la carpeta `topstyle/` completa → URL pública al instante

**Vercel:** `npm i -g vercel && cd topstyle && vercel`

**GitHub Pages:** subir la carpeta a un repo → Settings → Pages → Source: main / root.

---

## Catálogo de productos Question Professional

Todo vive en la variable `PRODUCTS` al principio del `<script>` en `index.html`.
Al día de hoy hay **73 productos** cargados, organizados en estas líneas:

**Coloración**

- Coloration Full Plex 60 g (109 tonos, 1 SKU base)
- Lumiplex Color Demi-Permanente 60 g (sin amoníaco)
- Oxidantes 10 / 20 / 30 Vol. 900 cc
- Revelador Superaclarante 40 Vol. 900 cc
- Activadores Lumiplex 3 / 6 / 13 Vol. 900 ml
- Loción Quitamanchas 300 ml

**Decolorantes**

- Polvo Decolorante 500 g
- Mint Power Plex 500 g
- White Power Plex 500 g

**Permanentes**

- Permanente 1 (Naturales) / 2 (Teñidos) / 3 (Decolorados) 300 ml
- Neutralizante 900 cc

**Tratamientos profesionales**

- Ampollas Restauradoras — estuche 4 x 10 ml
- Twelve — Tratamiento Sin Enjuague 210 ml
- Máscara Capilar Línea Salón 1000 cc / 250 cc
- Acid Line: Shampoo, Acondicionador, Máscara (480 / 500 ml)
- Theraphy Liss — Kit Alisado Progresivo (3 pasos, todo 480 ml)

**Shampoos de salón**

- Neutro 900 ml / 4900 ml
- Post Color 900 ml
- Frecuente 4900 ml

**Silver (línea matizadora)**

- Silver Shampoo 200 / 960 ml
- Silver Acondicionador 960 ml
- Silver Máscara 500 ml

**Q Style (línea styling, 10 productos)**

Finish Spray · Hair Fix Mousse · Finish Glow · Curl Cream · Volume Fix · Fixer Paste · Coolfix Gel · Termic Protect · Oil Molecular Flex · Terra.

**Intelligent Series (8 líneas de tratamiento)**

Nutriv Cell (3 SKU) · Color Defense (3 SKU) · Keratin Lift (5 SKU) · Volumizer (3 SKU) · Lumière (5 SKU) · Intensive Repair (3 SKU) · Hair Resist (1 SKU) · Équilibre (3 SKU).

---

## Cómo editar productos (⚡ lo más importante)

Cada producto tiene esta forma:

```javascript
{
  id: 'coloration-full-plex-60g', // slug único, usado por el carrito
  active: true,                    // false = oculto del sitio sin borrarlo
  brand: 'Question Professional',
  name: 'Coloration Full Plex — Pomo 60 g',
  description: 'Coloración en crema permanente con tecnología Plex...',
  category: 'color',               // tratamientos | color | styling | higiene | herramientas
  price: 0,                        // en pesos, número sin comas. 0 = "Consultar"
  image: 'assets/productos/coloration.jpg',
  badge: 'Top ventas'              // opcional. '' para no mostrar
}
```

### Casos de uso frecuentes

**Dar de baja un producto temporalmente (sin borrarlo):**
```javascript
{ ..., active: false, ... }
```

**Agregar precio:** cambiar `price: 0` por el número en pesos. `price: 12500` se muestra como `$ 12.500`.

**Sumar un producto nuevo:** copiás un bloque existente, cambiás el `id` (único), el resto de campos, y listo.

### Categorías usadas

- `color` — coloración, decolorantes, silver, oxidantes, activadores
- `tratamientos` — máscaras, ampollas, permanentes, keratinas, Intelligent Series tratantes
- `higiene` — shampoos y acondicionadores
- `styling` — línea Q Style, Twelve sin enjuague, óleos termo
- `herramientas` — (sin uso hoy, reservada por si sumás planchas/secadores)

---

## Qué falta completar

Todos los `[COMPLETAR:...]` con Ctrl+F en `index.html`. Los que quedan:

**1. Email** (2 veces): `[COMPLETAR:email@topstyle.com.ar]` — tarjeta de contacto + link del footer.

**2. Redes sociales** (footer):
- `[COMPLETAR:URL Instagram]`
- `[COMPLETAR:URL Facebook]`
- `[COMPLETAR:URL TikTok]`

**3. CUIT opcional** en el footer (`[COMPLETAR: CUIT opcional]`) — si no querés, borralo.

**4. Precios** — todos los productos tienen `price: 0` (muestra "Consultar"). Cuando estés lista con la lista mayorista, me la pasás y los completo.

**5. Fotos mejoradas** — las actuales son crops del catálogo PDF. Cuando tengas fotos limpias de producto (fondo blanco) las reemplazamos manteniendo los nombres.

---

## Flujo que propongo

1. **Revisás el catálogo**: abrís el `index.html` en el navegador y vas producto por producto decidiendo `active: true` o `active: false`. Los que no querés vender en el sitio los dejás en `false`.
2. **Me pasás precios mayoristas** de los productos que sí querés publicar.
3. **Yo actualizo** el array `PRODUCTS` con precios y activaciones.
4. **Me pasás** email oficial + links de redes.
5. **Deploy inicial** a Netlify (5 min).
6. **Iteramos** conforme sumes marcas (Millenium y otras).
7. **Fase 2**: login mayorista cuando el catálogo esté firme.

---

## Arquitectura del carrito

El sitio tiene un carrito funcional completo:

- **Trigger**: ícono de bolsa en la navbar con contador.
- **Drawer**: se abre desde la derecha con los ítems, cantidades, subtotal.
- **Controles**: sumar / restar cantidad, eliminar ítem, vaciar carrito.
- **Persistencia**: `localStorage` — si la cliente cierra el navegador y vuelve, su carrito sigue ahí.
- **Checkout**: botón "Finalizar pedido por WhatsApp" arma un mensaje con todos los productos, cantidades y subtotal, y abre WhatsApp.
- **Form integrado**: el formulario de la sección "Pedido" toma los productos del carrito automáticamente. Si además escribe algo en "Productos adicionales", se suma al mensaje.

### Cómo se arma el mensaje de WhatsApp

```
*Nuevo pedido — TopStyle*

• Nombre: María González
• WhatsApp: 11 2345-6789
• Tipo de cliente: Profesional / Peluquería
• Zona: CABA

*Productos solicitados:*
• 2 x Question Professional — Coloration Full Plex — Pomo 60 g — Consultar
• 1 x Question Professional — Silver Shampoo 960 ml — Consultar

*Subtotal estimado:* A confirmar por WhatsApp

*Observaciones:*
Horario preferido: martes a la tarde
```

Los precios finales, stock y forma de pago se confirman después por WhatsApp (así siempre podés ajustar listas mayoristas, promociones, etc.).

---

## Paleta y tipografías

**Paleta** (todas las variables en `:root` dentro de `<style>`):

| Uso | Hex |
|---|---|
| Fondo principal | `#0a0a0a` |
| Fondo secundario | `#121212` |
| Tarjetas | `#181818` |
| Bordes | `#2e2e2e` |
| Plata | `#c8c8c8` |
| Plata claro / CTA | `#f0f0f0` |
| Texto principal | `#f5f5f5` |
| Texto secundario | `#b8b8b8` |
| Magenta Question (acento distributor card) | `#e81b88` |
| Verde WhatsApp | `#25d366` |

**Tipografías:** Playfair Display (títulos) + Inter (texto). Cargan desde Google Fonts.

---

## Funcionalidades implementadas

- Navbar sticky con efecto de scroll + menú hamburguesa mobile
- Scroll suave entre secciones
- Animaciones de entrada al hacer scroll (respeta `prefers-reduced-motion`)
- **Carrito completo** con drawer, cantidades, subtotal, persistencia
- Render dinámico de productos desde `PRODUCTS` array
- Filtro por categoría sin recarga
- Flag `active: true|false` por producto (sin borrar datos)
- Checkout → WhatsApp con mensaje pre-armado completo
- Botón flotante de WhatsApp con animación pulse
- Toast de confirmación al sumar productos
- 100% responsive mobile-first
- Accesibilidad: ARIA labels, focus visible, landmarks semánticos

---

## Fase 2 — Login mayorista (futuro)

El sitio actual es 100% estático. Para tener login real de mayoristas necesitás un backend. Opciones:

**Opción A — Supabase (recomendado)** · Tier gratis generoso, incluye auth + Postgres. Integración con JS vanilla (1 script CDN). La cliente se registra como "Profesional", vos aprobás desde el panel de Supabase, al loguearse se desbloquean precios mayoristas.

**Opción B — Firebase Auth** · Infraestructura Google, similar flujo.

**Opción C — Password compartida** · 0 backend: un input "Soy profesional" con una clave que vos repartís. Pro: 0 infra. Contra: se puede filtrar.

En el código actual ya hay un hook comentado para insertarlo: `// [FASE 2] Login mayorista`.
