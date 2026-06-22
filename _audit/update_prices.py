"""
update_prices.py - Actualiza precios en index.html a partir de un CSV.

Uso:
    python _audit/update_prices.py precios.csv
    python _audit/update_prices.py precios.csv --dry-run

Formato del CSV (con encabezado):
    id,precio
    coloration-full-plex-60g,9500
    is-keratin-lift-spray,22000

Columnas aceptadas:
    id / product_id / producto_id
    precio / price / monto
    (acepta punto o coma decimal, ignora $ y puntos de miles)
"""

import csv
import re
import sys
import argparse
from pathlib import Path

ROOT  = Path(__file__).parent.parent
INDEX = ROOT / 'index.html'


def load_csv(path):
    prices = {}
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {k.strip().lower(): v.strip() for k, v in row.items()}
            pid = row.get('id') or row.get('product_id') or row.get('producto_id')
            raw = row.get('precio') or row.get('price') or row.get('monto')
            if not pid or not raw:
                continue
            # Normalizar: quitar $, convertir punto-miles y coma-decimal
            clean = raw.replace('$', '').replace(' ', '')
            # Si tiene coma => formato argentino (1.234,56 -> 1234.56)
            if ',' in clean:
                clean = clean.replace('.', '').replace(',', '.')
            try:
                prices[pid] = float(clean)
            except ValueError:
                print(f"  WARN: precio invalido para '{pid}': {raw!r} -- omitido")
    return prices


def update_html(html, prices):
    updated = []
    skipped = []
    for pid, new_price in prices.items():
        pat = rf"(id:\s*'{re.escape(pid)}'[\s\S]*?price:\s*)([0-9]+(?:\.[0-9]+)?)([,\s])"
        m = re.search(pat, html)
        if not m:
            skipped.append(pid)
            continue
        old_price = float(m.group(2))
        html = html[:m.start()] + m.group(1) + f'{new_price:.2f}' + m.group(3) + html[m.end():]
        updated.append((pid, old_price, new_price))
    return html, updated, skipped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', help='CSV con columnas id,precio')
    parser.add_argument('--dry-run', action='store_true',
                        help='Muestra cambios sin modificar el archivo')
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        sys.exit(f"Error: no se encuentra '{csv_path}'")

    prices = load_csv(csv_path)
    if not prices:
        sys.exit("El CSV no tiene precios validos. Revisa el formato.")

    print(f"\n{len(prices)} productos en la lista\n")

    html  = INDEX.read_text(encoding='utf-8')
    new_html, updated, skipped = update_html(html, prices)

    if updated:
        print("Cambios:")
        for pid, old, new in updated:
            pct = ((new - old) / old * 100) if old else 0
            print(f"  OK  {pid:<45}  $ {old:>12,.2f}  ->  $ {new:>12,.2f}  ({pct:+.1f}%)")
    else:
        print("  Sin cambios detectados.")

    if skipped:
        print(f"\n  WARN: {len(skipped)} IDs no encontrados en PRODUCTS:")
        for pid in skipped:
            print(f"    - {pid}")

    if args.dry_run:
        print("\n  (dry-run: no se modifico nada)")
        return

    if updated:
        INDEX.write_text(new_html, encoding='utf-8')
        print(f"\n{len(updated)} precios actualizados en index.html")
        print("  Revisa: git diff index.html")
        print("  Deploy: git add index.html && git commit -m 'precios julio 2026' && git push")


if __name__ == '__main__':
    main()
