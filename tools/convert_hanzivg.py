"""Convert HanziVG SVG files into Hanzi-Writer JSON format.

Usage:
    python tools/convert_hanzivg.py                # convert *all* SVGs
    python tools/convert_hanzivg.py 我你张            # convert specific chars
    python tools/convert_hanzivg.py 6211 5f20       # by hex codepoints
"""

import json, sys
from pathlib import Path
from svgpathtools import parse_path, Path as SvgPath
from xml.etree import ElementTree as ET

SRC = Path('hanzivg/hanzi')
OUT = Path('data_hzw'); OUT.mkdir(exist_ok=True)

# HanziVG SVG coordinate system is ~109×109. Hanzi-Writer expects 1024×1024.
SCALE_FACTOR = 1024 / 109


def scale_path(d: str, s: float) -> str:
    """Return the path string scaled by factor *s*."""
    p = parse_path(d)
    p_scaled = SvgPath(*[seg.scaled(s) for seg in p])
    return p_scaled.d()


def median_points(d: str, num: int = 30):
    """Sample *num* equally-spaced points along *d* for Hanzi-Writer medians."""
    path = parse_path(d)
    return [[round(pt.real, 1), round(pt.imag, 1)]
            for pt in (path.point(i / (num - 1)) for i in range(num))]


# ------------------------------------------------------------
# Determine which SVGs to convert
# ------------------------------------------------------------
if len(sys.argv) > 1:
    targets = set()
    for arg in sys.argv[1:]:
        # accept either a literal character or hex string
        if len(arg) == 1:
            targets.add(f"{ord(arg):05x}")
        else:
            targets.add(arg.lower().zfill(5))
    svg_files = [SRC / f"{code}.svg" for code in targets if (SRC / f"{code}.svg").exists()]
else:
    svg_files = list(SRC.glob('*.svg'))

print(f"Converting {len(svg_files)} HanziVG SVG(s) → Hanzi-Writer JSON …")

success = 0; failed = 0
for svg_file in svg_files:
    code_hex = svg_file.stem.lower()
    try:
        ch = chr(int(code_hex, 16))
    except ValueError:
        failed += 1; continue

    try:
        tree = ET.parse(svg_file)
        root = tree.getroot()

        strokes, medians = [], []
        for path_el in root.findall('.//{http://www.w3.org/2000/svg}path'):
            d_raw = path_el.get('d')
            if not d_raw:
                continue
            try:
                d_scaled = scale_path(d_raw, SCALE_FACTOR)
                strokes.append(d_scaled)
                medians.append(median_points(d_scaled))
            except Exception:
                # Skip paths parse_path can't handle (e.g., exotic commands)
                continue

        if not strokes:
            failed += 1; continue

        with open(OUT / f"{ch}.json", 'w', encoding='utf-8') as f:
            json.dump({'strokes': strokes, 'medians': medians}, f, ensure_ascii=False)

        success += 1
    except Exception as e:
        failed += 1

print(f"Done. Created {success} character files to {OUT} (skipped {failed}).") 