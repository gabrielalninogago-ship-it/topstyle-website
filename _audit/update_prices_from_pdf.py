"""
update_prices_from_pdf.py — Lee la lista de precios PDF de Question y actualiza index.html.

Uso:
    python _audit/update_prices_from_pdf.py "assets/precios/QUESTION Online Julio 2026.pdf"
    python _audit/update_prices_from_pdf.py "assets/precios/QUESTION Online Julio 2026.pdf" --dry-run

Cada cuatrimestre Question actualiza el PDF con los nuevos precios sugeridos.
Solo cambia el mes/año en el nombre del archivo.
"""

import re
import sys
import argparse
import pdfplumber
from pathlib import Path

ROOT  = Path(__file__).parent.parent
INDEX = ROOT / 'index.html'

# Código del PDF → id del producto en PRODUCTS[]
# Los códigos son estables entre listas — solo cambian los precios.
CODE_TO_ID = {
    # Shampoo
    '310': 'shampoo-neutro-4900',
    '314': 'shampoo-neutro-900',
    '315': 'shampoo-post-color-900',
    # Oxigenadas / Emulsión Lumiplex
    '322': 'oxidante-10-vol-900',
    '323': 'oxidante-20-vol-900',
    '324': 'oxidante-30-vol-900',
    '325': 'revelador-40-vol-900',
    '382': 'lumiplex-activador-3vol-900',
    '246': 'lumiplex-activador-6vol-900',
    '247': 'lumiplex-activador-13vol-900',
    # Quitamanchas
    '366': 'locion-quitamanchas-300',
    # Permanentes
    '340': 'permanente-1-naturales-300',
    '341': 'permanente-2-tenidos-300',
    '342': 'permanente-3-decolorados-300',
    '343': 'neutralizante-900',
    # Tratantes
    '349': 'ampollas-restauradoras',
    '356': 'mascara-capilar-1000',
    '357': 'mascara-capilar-250',
    '383': 'twelve-spray-210',
    # Decolorantes
    '367': 'polvo-decolorante-500',
    '249': 'mint-power-plex-500',
    '250': 'white-power-plex-500',
    # Q Style
    '869': 'qstyle-curl-cream',
    '870': 'qstyle-fixer-paste',
    '871': 'qstyle-termic-protect',
    '872': 'qstyle-finish-spray',
    '874': 'qstyle-finish-glow',
    '875': 'qstyle-hair-fix-mousse',
    '379': 'qstyle-volume-fix',
    # Therapy Liss
    '913': 'theraphy-liss-shampoo-480',
    '914': 'theraphy-liss-alisador-480',
    '915': 'theraphy-liss-mascara-480',
    # Silver
    '906': 'silver-shampoo-200',
    '908': 'silver-shampoo-960',
    '909': 'silver-acondicionador-960',
    '917': 'silver-mascara-500',
    # Acid Line
    '820': 'acid-line-shampoo-480',
    '821': 'acid-line-acondicionador-480',
    '822': 'acid-line-mascara-500',
    # IS — Nutriv Cell
    '826': 'is-nutriv-cell-shampoo',
    '827': 'is-nutriv-cell-mascara',
    '828': 'is-nutriv-cell-acond',
    '829': 'is-nutriv-cell-shampoo-1500',
    '830': 'is-nutriv-cell-mascara-850',
    '831': 'is-nutriv-cell-acond-1500',
    # IS — Volumizer
    '832': 'is-volumizer-shampoo',
    '833': 'is-volumizer-mascara',
    '834': 'is-volumizer-acond',
    '835': 'is-volumizer-shampoo-1500',
    '836': 'is-volumizer-mascara-850',
    '837': 'is-volumizer-acond-1500',
    # IS — Color Defense
    '838': 'is-color-defense-shampoo',
    '839': 'is-color-defense-mascara',
    '840': 'is-color-defense-acond',
    '841': 'is-color-defense-shampoo-1500',   # nota: mismo código que Hair Resist 1500 (typo en el PDF)
    '842': 'is-color-defense-mascara-850',
    '843': 'is-color-defense-acond-1500',
    # IS — Hair Resist (1500ml usa código 844 para 330ml; 1500ml lo resuelve TEXT_TO_ID)
    '844': 'is-hair-resist-shampoo',
    # IS — Lumiere
    '847': 'is-lumiere-shampoo',
    '848': 'is-lumiere-mascara',
    '849': 'is-lumiere-shampoo-1500',
    '850': 'is-lumiere-mascara-850',
    '910': 'is-lumiere-spray',
    '378': 'is-lumiere-oleo',
    '911': 'is-lumiere-ampollas',
    # IS — Keratin Lift
    '852': 'is-keratin-lift-shampoo',
    '853': 'is-keratin-lift-mascara',
    '854': 'is-keratin-lift-shampoo-1500',
    '855': 'is-keratin-lift-mascara-850',
    '809': 'is-keratin-lift-spray',
    '819': 'is-keratin-lift-oleo',
    '808': 'is-keratin-lift-ampollas',
    # IS — Equilibre
    '857': 'is-equilibre-shampoo',
    '858': 'is-equilibre-mascara',
    '859': 'is-equilibre-acond',
    '860': 'is-equilibre-shampoo-1500',
    '861': 'is-equilibre-mascara-850',
    '862': 'is-equilibre-acond-1500',
    # IS — Intensive Repair
    '863': 'is-intensive-shampoo',
    '864': 'is-intensive-mascara',
    '865': 'is-intensive-balsamo',
    '866': 'is-intensive-shampoo-1500',
    '867': 'is-intensive-mascara-850',
    '868': 'is-intensive-balsamo-1500',
    # Hair Mist
    '823': 'qstyle-terra-100',
}

# Productos sin código en el PDF — substring normalizado del nombre → id
# Se checan ANTES que el código para resolver ambigüedades (ej: código 841 duplicado).
TEXT_TO_ID = {
    'tintura crema':      'coloration-full-plex-60g',
    'tintura lumiplex':   'lumiplex-color-60g',
    'hair resist x 1500': 'is-hair-resist-shampoo-1500',  # código 841 repetido en el PDF
}


def clean_price(raw):
    """'$ 2 2.723' o '$ 138.127' → 22723. Quita todo lo que no sea dígito."""
    digits = re.sub(r'[^\d]', '', raw)
    return int(digits) if digits else None


def normalize(text):
    return re.sub(r'\s+', ' ', text.lower().strip())


def parse_pdf(pdf_path):
    """Extrae {id_producto: precio_sugerido} de todas las páginas del PDF."""
    prices = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ''
            for line in text.splitlines():
                parts = line.split('$')
                if len(parts) < 2:
                    continue
                left      = parts[0].strip()
                price_raw = parts[1]
                price     = clean_price(price_raw)
                if not price:
                    continue

                norm = normalize(left)
                pid  = None

                # 1. Texto primero (resuelve productos sin código y el código 841 duplicado)
                for key, text_pid in TEXT_TO_ID.items():
                    if key in norm:
                        pid = text_pid
                        break

                # 2. Código numérico de 3 dígitos al final de la parte izquierda
                if not pid:
                    m = re.search(r'\b(\d{3})\s*$', left)
                    if m:
                        pid = CODE_TO_ID.get(m.group(1))

                if pid and pid not in prices:
                    prices[pid] = price

    return prices


def update_html(html, prices):
    updated, skipped = [], []
    for pid, new_price in prices.items():
        pat = rf"(id:\s*'{re.escape(pid)}'[\s\S]*?price:\s*)([0-9]+(?:\.[0-9]+)?)([,\s])"
        m = re.search(pat, html)
        if not m:
            skipped.append(pid)
            continue
        old_price = float(m.group(2))
        if old_price == new_price:
            continue
        html = html[:m.start()] + m.group(1) + str(new_price) + m.group(3) + html[m.end():]
        updated.append((pid, old_price, new_price))
    return html, updated, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf', help='PDF de precios (ej: "assets/precios/QUESTION Online Julio 2026.pdf")')
    ap.add_argument('--dry-run', action='store_true', help='Muestra cambios sin modificar nada')
    args = ap.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        sys.exit(f"Error: no se encuentra '{pdf_path}'")

    print(f"\nLeyendo {pdf_path.name} ...")
    prices = parse_pdf(pdf_path)
    print(f"{len(prices)} productos encontrados en el PDF\n")

    html = INDEX.read_text(encoding='utf-8')
    new_html, updated, skipped = update_html(html, prices)

    if updated:
        print("Cambios:")
        for pid, old, new in updated:
            pct = ((new - old) / old * 100) if old else 0
            print(f"  OK  {pid:<48}  $ {old:>10,.0f}  ->  $ {new:>10,}  ({pct:+.1f}%)")
    else:
        print("  Sin cambios de precio.")

    if skipped:
        print(f"\n  WARN: {len(skipped)} IDs del PDF no encontrados en index.html:")
        for pid in skipped:
            print(f"    - {pid}")

    all_mapped = set(CODE_TO_ID.values()) | set(TEXT_TO_ID.values())
    missed = all_mapped - set(prices.keys())
    if missed:
        print(f"\n  INFO: {len(missed)} productos del sitio no encontrados en el PDF (sin cambio):")
        for pid in sorted(missed):
            print(f"    - {pid}")

    if args.dry_run:
        print("\n  (dry-run: no se modifico nada)")
        return

    if updated:
        INDEX.write_text(new_html, encoding='utf-8')
        print(f"\n{len(updated)} precios actualizados en index.html")
        print("  Revisa:  git diff index.html")
        print("  Deploy:  git add index.html && git commit -m 'precios julio 2026' && git push")
    else:
        print("\nNada que guardar.")


if __name__ == '__main__':
    main()
