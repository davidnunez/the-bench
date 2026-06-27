#!/usr/bin/env python3
"""
scripts/generate-labels.py
Reads design-system/tokens.yaml → writes design-system/labels/the-bench-labels.svg

Output: the-bench wordmark (aubergine on cream) + eight-label ink-legend card.
No bin label (Phase 2+). No zone/mode label (Phase 5+, D-16/D-17).

Dependencies: PyYAML (pip install PyYAML)
Security: yaml.safe_load() only — the unsafe loader is forbidden (prevents
          arbitrary object instantiation from a crafted tokens.yaml, ASVS V5).
"""

import yaml
import pathlib
import xml.dom.minidom
from xml.sax.saxutils import escape as _xml_escape

TOKENS_PATH = pathlib.Path("design-system/tokens.yaml")
OUTPUT_PATH = pathlib.Path("design-system/labels/the-bench-labels.svg")

# Google Fonts import. NOTE: the bare '&' separating the two `family=` params is
# illegal in XML (SVG is XML) and breaks the parser ("EntityRef: expecting ';'").
# It is XML-escaped to &amp; on emit; the XML parser unescapes it back to '&'
# before the CSS @import URL is used, so the fonts still load correctly.
FONT_IMPORT_URL = (
    "https://fonts.googleapis.com/css2?family=Archivo:wght@700"
    "&family=IBM+Plex+Mono:wght@400;700&display=swap"
)


def xesc(value):
    """XML-escape any dynamic text/attribute content emitted into the SVG.

    Escapes &, <, > (and, for attributes, the quote chars). This prevents any
    token value containing &, <, or > — or the bare '&' in the font URL — from
    producing malformed XML.
    """
    return _xml_escape(str(value), {'"': "&quot;", "'": "&apos;"})


# ── SVG canvas ────────────────────────────────────────────────────────────────
SVG_W = 480
LEGEND_BOTTOM_MARGIN = 18   # space below the last swatch row

# ── Wordmark ──────────────────────────────────────────────────────────────────
WM_H = 110
WM_PADDING_X = 36
WM_PADDING_Y = 70

# ── Legend grid ───────────────────────────────────────────────────────────────
LEGEND_TOP = WM_H + 20
SWATCH_W = 218
SWATCH_H = 64               # bumped from 58 to seat up to two wrapped meaning lines
SWATCH_GAP_X = 8
SWATCH_GAP_Y = 8
SWATCH_COLS = 2
LEGEND_LEFT = 12

# ── Swatch text geometry ──────────────────────────────────────────────────────
# IBM Plex Mono is truly monospaced: advance width = 0.6em. At font-size F the
# per-char advance is 0.6*F px, so chars_per_line is derived, never hardcoded.
SWATCH_PAD_X = 10                                  # inner left = right padding
MEANING_FONT_SIZE = 10                             # matches .label-meaning CSS
MEANING_CHAR_ADVANCE = 0.6 * MEANING_FONT_SIZE     # monospace advance per char
MEANING_INNER_W = SWATCH_W - 2 * SWATCH_PAD_X      # usable text width (px)
MEANING_CHARS_PER_LINE = int(MEANING_INNER_W // MEANING_CHAR_ADVANCE)
TYPE_Y = 20                # type-name baseline
MEANING_Y0 = 38            # first meaning-line baseline
MEANING_LINE_H = 12        # baseline-to-baseline for wrapped meaning lines
MEANING_MAX_LINES = 2      # current strings wrap to at most two lines
SWATCH_BOTTOM_INSET = 4    # keep descenders off the card's bottom edge


def load_tokens():
    """Load tokens using yaml.safe_load (never yaml.load)."""
    with open(TOKENS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def wrap_meaning(text, max_chars):
    """Word-wrap on spaces so each line fits within max_chars (monospace metric).

    Breaks only on word boundaries — the longest single word in the token set
    ("built-to-travel", 15 chars) is well under the line budget, so no mid-word
    splitting is needed.
    """
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= max_chars:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def assert_swatch_fits(name, lines):
    """Structural overflow guard — hard-fail the build if a swatch would clip.

    Mirrors the XML well-formedness guard: makes future description overflow a
    non-zero build failure instead of a defect a human has to spot visually.
    Checks both axes: each line fits horizontally, the block fits vertically.
    """
    for ln in lines:
        px = len(ln) * MEANING_CHAR_ADVANCE
        if px > MEANING_INNER_W:
            raise SystemExit(
                f"ERROR: swatch '{name}' line overflows card width — "
                f"{len(ln)} chars = {px:.1f}px > {MEANING_INNER_W}px inner; "
                f"line={ln!r}"
            )
    if len(lines) > MEANING_MAX_LINES:
        raise SystemExit(
            f"ERROR: swatch '{name}' wraps to {len(lines)} lines "
            f"(max {MEANING_MAX_LINES}) — would overflow card height"
        )
    last_baseline = MEANING_Y0 + (len(lines) - 1) * MEANING_LINE_H
    descender = 0.2 * MEANING_FONT_SIZE
    limit = SWATCH_H - SWATCH_BOTTOM_INSET
    if last_baseline + descender > limit:
        raise SystemExit(
            f"ERROR: swatch '{name}' text exceeds card height — last baseline "
            f"{last_baseline} + descender {descender:.1f} > {limit}px"
        )


def swatch(name, type_data, x, y):
    """Render a single type swatch: bg rect + type name + wrapped meaning text.

    All token-derived values are XML-escaped — colors flow into attributes,
    name/meaning into text content — so no token value can break the SVG.
    The meaning is word-wrapped to the card width and emitted as <tspan> lines.
    """
    bg = xesc(type_data["bg"])
    fg = xesc(type_data["on"])
    name_x = xesc(name)

    lines = wrap_meaning(type_data["meaning"], MEANING_CHARS_PER_LINE)
    assert_swatch_fits(name, lines)

    tspans = []
    for i, ln in enumerate(lines):
        dy = "" if i == 0 else f' dy="{MEANING_LINE_H}"'
        tspans.append(f'<tspan x="{SWATCH_PAD_X}"{dy}>{xesc(ln)}</tspan>')
    meaning_tspans = "".join(tspans)

    return (
        f'  <g transform="translate({x},{y})">\n'
        f'    <rect width="{SWATCH_W}" height="{SWATCH_H}" fill="{bg}" rx="4"/>\n'
        f'    <text x="{SWATCH_PAD_X}" y="{TYPE_Y}" class="label-type" '
        f'fill="{fg}">{name_x}</text>\n'
        f'    <text x="{SWATCH_PAD_X}" y="{MEANING_Y0}" class="label-meaning" '
        f'fill="{fg}">{meaning_tspans}</text>\n'
        f'  </g>'
    )


def build_svg(tokens):
    """Build the full SVG: wordmark + 8-label ink-legend card."""
    types = tokens["types"]
    roles = tokens["roles"]
    base  = tokens["base"]

    aubergine = xesc(roles["structure"]["hex"])   # probe identity = The Bench
    cream     = xesc(base["paper"]["hex"])
    font_import = xesc(FONT_IMPORT_URL)            # bare '&' → '&amp;' (valid XML)

    # Ink-legend swatches (8 types, 2 columns)
    swatches = []
    for i, (name, data) in enumerate(types.items()):
        col = i % SWATCH_COLS
        row = i // SWATCH_COLS
        x = LEGEND_LEFT + col * (SWATCH_W + SWATCH_GAP_X)
        y = LEGEND_TOP + row * (SWATCH_H + SWATCH_GAP_Y)
        swatches.append(swatch(name, data, x, y))

    swatches_svg = "\n".join(swatches)

    # Canvas height derived from the actual row count so it always fits.
    rows = (len(types) + SWATCH_COLS - 1) // SWATCH_COLS
    legend_bottom = LEGEND_TOP + (rows - 1) * (SWATCH_H + SWATCH_GAP_Y) + SWATCH_H
    svg_h = legend_bottom + LEGEND_BOTTOM_MARGIN

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated by scripts/generate-labels.py from design-system/tokens.yaml -->
<!-- Open in Inkscape with fonts installed for print-ready PDF export        -->
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {SVG_W} {svg_h}" width="{SVG_W}" height="{svg_h}">
  <style>
    @import url('{font_import}');
    .wordmark     {{ font-family: 'Archivo', system-ui, sans-serif;
                    font-weight: 700; font-size: 34px; }}
    .wordmark-sub {{ font-family: 'IBM Plex Mono', 'Courier New', monospace;
                    font-size: 11px; }}
    .label-type   {{ font-family: 'IBM Plex Mono', 'Courier New', monospace;
                    font-size: 13px; font-weight: 700; }}
    .label-meaning {{ font-family: 'IBM Plex Mono', 'Courier New', monospace;
                    font-size: {MEANING_FONT_SIZE}px; }}
  </style>

  <!-- Wordmark: the-bench — Probe identity (aubergine on cream) -->
  <rect x="0" y="0" width="{SVG_W}" height="{WM_H}" fill="{aubergine}"/>
  <text x="{WM_PADDING_X}" y="{WM_PADDING_Y}"
        class="wordmark" fill="{cream}">the-bench</text>
  <text x="{WM_PADDING_X}" y="{WM_PADDING_Y + 22}"
        class="wordmark-sub" fill="{cream}">Signal Path — Probe</text>

  <!-- Ink legend: 8-type Signal Path semantic system -->
{swatches_svg}
</svg>'''


def assert_well_formed_xml(path):
    """Parse the written SVG back as XML; hard-fail the build if malformed.

    SVG is XML, so any unescaped '&', '<', or '>' yields an invalid file that a
    browser refuses to render. Parsing it back here makes invalid SVG a non-zero
    build failure instead of a silent regression caught only by a human.
    """
    text = pathlib.Path(path).read_text(encoding="utf-8")
    try:
        xml.dom.minidom.parseString(text)
    except Exception as exc:  # xml.parsers.expat.ExpatError and friends
        raise SystemExit(
            f"ERROR: generated SVG is not well-formed XML ({path}): {exc}"
        )


def main():
    tokens = load_tokens()
    svg = build_svg(tokens)   # swatch() asserts no description overflows
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(svg, encoding="utf-8")
    assert_well_formed_xml(OUTPUT_PATH)
    print(f"Generated: {OUTPUT_PATH} (well-formed XML, no overflow)")


if __name__ == "__main__":
    main()
