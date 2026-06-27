# The Bench

My home office/studio — modeled as version-controlled code. **Space as code, built in public.**

---

## The Point

The Bench exists in a before state. The desk is fine. The cable situation is not. The maker zone is aspirational. Nothing is where it belongs yet, and "after" is a long way off.

This repo is the execution arm of a redesign I'm running in public — not as a renovation blog, but as a **Signal Path Probe**: a hands-on exploration with documented process, committed artifacts, and a measurable end state. Every milestone ships something tangible. Nothing waits behind a closed gate.

The defining inversion: **the code leads; the physical space hangs off it.** I'm modeling the room before I move a single piece of furniture, because the model is the proof-of-work — and proof-of-work is the point.

Two ideas are load-bearing here:

**Before → "alive."** The goal isn't a renovated office. It's a *living, version-controlled model* of the space — one that drifts forward as I iterate the room, and backward when I look up the old layout. The physical Bench is what the model drives; the model is what you can follow.

**Environment-as-provenance.** The physical context in which work is made is part of the work's soul — not background noise. A parametric model of the Bench captures not just dimensions but the active configuration, the three modes (deep-focus / creator-filming / electronics-maker), the stuff that has a drawer and the stuff that doesn't. That's the original idea here, and it's genuinely the differentiator: this isn't a furniture-layout project.

The deliberate over-engineering — lines of OpenSCAD just to place a desk — is the hook, not a bug. The over-engineering is on display, legible, version-controlled, diffable. **That's the artifact.** Heaviness-as-proof is only embarrassing if you're hiding it.

This Probe lives in the **Signal Path framework** I use to structure exploratory work. Signal → Probe → Pulse: the curiosity spark, the hands-on exploration, the quick share. The Bench is a Probe — meaning *aubergine on cream* is its identity ink by definition, not by preference. Weekly proof-of-work artifacts are Pulses. If you want the strategic layer, the governing Signal lives at [davidnunez.com](https://davidnunez.com) — that's where The Bench has a public presence and where field notes land.

---

## What's in the Repo

```
the-bench/
├── README.md                           # You are here
├── LICENSE                             # MIT 2026 David Nunez
├── Makefile                            # make labels  make validate  make renders (Phase 2+)
├── design-system/
│   ├── tokens.yaml                     # Semantic brand token system (Board-provenance)
│   └── labels/
│       └── the-bench-labels.svg        # Generated wordmark + ink-legend card
├── scripts/
│   └── generate-labels.py             # token → SVG label generator (~80 lines, PyYAML)
└── decisions/
    ├── ADR-001-openscad-include-vs-use.md
    ├── ADR-002-dollhouse-print-scale.md
    ├── ADR-003-modular-dollhouse-walls.md
    └── ADR-004-semantic-color-integrity.md
```

The `design-system/` directory holds the brand token system as structured data — the full Signal Path semantic color system, not a flat palette — and the label SVG generated from it. `make labels` re-runs the generator on demand.

The `decisions/` directory holds four load-bearing ADRs, written before any `.scad` file exists. They lock the choices that would be expensive to change later — OpenSCAD include/use convention, print scale, modular wall architecture, and semantic color integrity. Reading them gives you the reasoning I'd otherwise reconstruct from commit messages.

---

## How It Works

The pipeline is intentionally transparent:

1. **Brand tokens** live in `design-system/tokens.yaml` — a pinned snapshot of the Signal Path semantic color system (eight content-type inks, base palette, typography stack). Board-provenance cited; re-synced when the Board changes.
2. `make labels` runs `scripts/generate-labels.py` → produces the committed SVG (wordmark + ink-legend card).
3. `make renders` (Phase 2+) runs the OpenSCAD CLI headlessly → committed PNGs. Every render is a buildable, diff-able artifact.
4. The `.scad` source files under `models/` are the room in code — parametric, git-diffable, plain text. `params.scad` is the single surface you edit to change a dimension.

Phase 1 (current) ships the spine and the design system. Room modeling starts in Phase 2.

---

## Status

**Phase 1 — Public Spine + Design System + ADRs.** In progress.

| Phase | What ships | Status |
|-------|-----------|--------|
| 1 — Public Spine + Design System + ADRs | README, brand tokens, label SVG, four load-bearing ADRs | In progress |
| 2 — Parametric Foundation | OpenSCAD installed, `params.scad`, room shell, first committed render | Not started |
| 3 — Furniture Primitives + First Render | Furniture modules, before-state model, on-brand committed render | Not started |
| 4 — Measurement Refinement | Room measured once; params replaced with real dims | Not started |
| 5 — Three Modes + Equipment Manifest | Mode annotations, equipment manifest as structured data | Not started |
| 6 — Doll-House Export + Physical Print | STL export, 3D-printed scale model photographed as v1 capstone | Not started |

The "before" state is what ships first. The redesign is v2+.

---

## License

MIT — see [LICENSE](LICENSE). One license covering the whole repo, brand assets included.

---

*The Bench is a Probe in the [Signal Path framework](https://davidnunez.com). Aubergine on cream.*
