# Phase 1: Public Spine + Design System + ADRs — Research

**Researched:** 2026-06-27
**Domain:** Docs/design-system/ADR scaffolding — no OpenSCAD, no room measurement
**Confidence:** HIGH on all five research domains; no low-confidence blockers

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- D-01 through D-05: README is a real GitHub README in David's voice; thesis section near top; Board back-link to davidnunez.com; audience = "finds it later"
- D-06: MIT license, whole repo, one LICENSE file
- D-07 through D-13: `design-system/tokens.yaml` encodes the full semantic brand system (8 types + base + roles + reserved/unbound + provenance). Not a flat palette.
- D-14 through D-17: `make labels` is a real generator (not a stub) emitting the `the-bench` wordmark + an eight-label ink-legend card. No bin label yet.
- D-18 through D-21: Four ADRs with pre-decided content. Write to the locked specs. No content discretion.
- D-22: Phase 1 pulse = the live public repo itself (spine + tokens + first generated label + four ADRs).

### Claude's Discretion

- Exact `tokens.yaml` YAML schema shape (nesting, key names)
- Generator language (Node vs Python) and exact SVG layout
- README section ordering details and exact ADR file formatting (use a lightweight standard ADR template)
- Repo metadata specifics (GitHub description, topics, social-preview) beyond "appropriate for a build-in-public project"

### Deferred Ideas (OUT OF SCOPE)

- Dynamic lighting / color-shifting space (v2 — AUTO)
- Livestreaming (v2 — FILM)
- Mode ↔ Signal-Path ink reconciliation (Phase 5)
- Color proposals for uncolored terms (future Pulse back to Board)
- `make sync-tokens` automation (v2)
- Bin-label template (v2 — no bins yet)
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| SPINE-01 | Public README: before→alive thesis, environment-as-provenance, over-engineering hook, identity one-liner, Board back-link | D-01 through D-05 locked; README section structure documented in Architecture Patterns below |
| SPINE-03 | Pulse-ready proof-of-work artifact logged in-repo at phase end | The live repo itself (spine + tokens + label + ADRs) is the artifact; logging = commit a `pulses/` or in-README entry |
| SPINE-04 | Appropriate open LICENSE + public-facing metadata | MIT text verified from choosealicense.com; metadata specifics in Standard Stack below |
| CODE-06 | Four load-bearing ADRs before any `.scad` | Content pre-decided in D-18–D-21; template format researched below — Nygard format recommended |
| DSGN-01 | In-repo design tokens encode the full semantic brand system | Full token schema with 8 types + base + roles + reserved + typography + provenance researched below |
| DSGN-03 | Brand tokens drive printable physical label SVG from same source of truth | Generator approach researched: Python + PyYAML + string-templated SVG; font strategy documented |
</phase_requirements>

---

## Summary

Phase 1 is a docs/design-system/ADR phase with zero OpenSCAD or measurement dependencies. All five research questions are in the "how" domain — the what is fully locked in CONTEXT.md.

The five how-questions resolved clearly: (1) Michael Nygard's five-section ADR format is the right container — simple, canonical, fast to write; (2) the label generator should be a small Python script (40–80 lines) using PyYAML + Python f-strings for SVG, keeping it in the same runtime as the validation toolchain; (3) `tokens.yaml` should use a custom human-legible schema organized by semantic role rather than W3C DTCG's JSON-first `$value`/`$type` convention; (4) the MIT license has a single canonical text with `Copyright (c) 2026 David Nunez`; GitHub public repo metadata is well-understood and enumerated below; (5) yamllint on `tokens.yaml` is worth wiring in Phase 1; a JSON Schema for tokens.yaml is deferred.

**Primary recommendation:** Ship in this order — LICENSE → README → `design-system/tokens.yaml` → generator script → `make labels` output → four ADRs → commit as pulse. Every deliverable stands alone as a public artifact; nothing in this phase waits on a predecessor to be useful.

---

## Architectural Responsibility Map

This phase has no runtime tiers (no API, no browser app, no database). Everything is committed file artifacts and build-pipeline scripts.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| README / prose | Repo artifact | — | Plain markdown; authored once, read on GitHub |
| LICENSE | Repo artifact | — | Static file; no tooling dependency |
| `design-system/tokens.yaml` | Repo artifact (data) | Consumed by generator | Source of truth; hand-authored, yamllint-validated |
| Label generator script | Build pipeline | — | `scripts/generate-labels.py`; invoked by Makefile |
| Generated label SVG | Build artifact (committed) | — | Committed to `design-system/labels/` so it's visible without running `make labels` |
| `decisions/ADR-00X-*.md` | Repo artifact | — | Human-authored; no tooling dependency |
| `Makefile` targets | Build pipeline | — | `make labels`, `make validate` wired in this phase |

---

## Standard Stack

### Core (Phase 1 — no new runtimes)

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| Python 3.x (present) | 3.14.6 (verified) | Label generator runtime; YAML parsing | Already installed; same runtime as yamllint/check-jsonschema |
| PyYAML | 6.0.3 (latest on PyPI) | Parse `tokens.yaml` in generator | Flagship Python YAML library; [OK] via slopcheck; pip-installable alongside yamllint |
| yamllint | current pip | Lint `tokens.yaml` syntax | Already in stack; wiring to tokens.yaml adds zero new dep |
| check-jsonschema | current pip | Schema validation (equipment manifest; tokens schema deferred) | Already in stack |
| GNU Make | system | `make validate`, `make labels` targets | Already in project architecture |
| git | system | Commit all Phase 1 artifacts as single pulse | Already in project |

### Not Needed in Phase 1

| Skipped | Why |
|---------|-----|
| SVG library (svgwrite, svg.py, drawsvg) | SVG for this generator is 60–100 lines of static structure with 8 rect+text groups; hand-templating with Python f-strings is more readable and has no extra dep |
| Node `yaml` or `js-yaml` (npm) | Python + PyYAML keeps the toolchain consistent; no npm package needed |
| JSON Schema for tokens.yaml | Deferred — yamllint catches syntax; a `tokens-schema.yaml` is a Phase 2+ task once the file is consumed by the generator and the structure is proven |
| Templating library (Jinja2, Mako) | Overkill for one 80-line SVG generator; Python f-strings are sufficient and more readable as a repo artifact |

**Installation (Phase 1 only):**
```bash
pip install PyYAML yamllint check-jsonschema
```

**Version verification (confirmed 2026-06-27):**
```bash
pip3 index versions PyYAML   # → 6.0.3 (latest)
pip3 index versions yamllint # → current
```

---

## Package Legitimacy Audit

Phase 1 installs only Python packages. npm packages `js-yaml` and `yaml` are noted here for completeness (considered and not recommended for this phase).

| Package | Registry | Age | Downloads | Source Repo | slopcheck | Disposition |
|---------|----------|-----|-----------|-------------|-----------|-------------|
| PyYAML | PyPI | Since 2001 | Very high | github.com/yaml/pyyaml | [OK] | Approved |
| yamllint | PyPI | Established | High | github.com/adrienverge/yamllint | [OK] | Approved |
| check-jsonschema | PyPI | Established | High | github.com/python-jsonschema/check-jsonschema | [OK] | Approved |
| js-yaml | npm | Created 2011-11-02 | Very high | github.com/nodeca/js-yaml | Not checked (npm) — verified via `npm view` age + no postinstall | Not used |
| yaml | npm | Created 2011-04-15 | Very high | eemeli.org/yaml | Not checked (npm) — verified via `npm view` age + no postinstall | Not used |

**Note on slopcheck scope:** slopcheck defaults to PyPI. npm packages were verified manually via `npm view {pkg} time.created` (both packages are 12+ years old) and confirmed to have no `postinstall` scripts. Neither is recommended for this phase.

**Packages removed due to [SLOP] verdict:** none  
**Packages flagged [SUS]:** none

---

## Architecture Patterns

### System Architecture Diagram

```
Board (private — read-only source of brand truth)
    │
    │ manual snapshot
    ▼
design-system/tokens.yaml          ← hand-authored, Board-provenance cited
    │                                 yamllint validates syntax
    │ python scripts/generate-labels.py
    ▼
design-system/labels/the-bench-labels.svg   ← committed artifact (wordmark + ink legend)
    │
    │ make labels
    ▼
Committed to repo → visible on GitHub immediately

README.md          ← public thesis; links to ADRs and design-system/
LICENSE            ← MIT 2026 David Nunez
decisions/ADR-001..004.md  ← load-bearing architectural choices

All artifacts: committed, no build step required to VIEW;
`make labels` re-generates the SVG from tokens.yaml on demand.
```

### Recommended Project Structure (Phase 1 scope only)

```
the-bench/
├── README.md                           # Public spine
├── LICENSE                             # MIT 2026 David Nunez
├── Makefile                            # make validate, make labels (make renders is a no-op stub until Phase 2)
├── design-system/
│   ├── tokens.yaml                     # Semantic brand tokens (canonical)
│   └── labels/
│       └── the-bench-labels.svg        # Generated artifact (committed)
├── scripts/
│   └── generate-labels.py              # Label generator (~60-80 lines, Python + PyYAML)
└── decisions/
    ├── ADR-001-openscad-include-vs-use.md
    ├── ADR-002-dollhouse-print-scale.md
    ├── ADR-003-modular-dollhouse-walls.md
    └── ADR-004-semantic-color-integrity.md
```

Note: `pulses/` or in-README pulse log for SPINE-03 can be a lightweight `PULSES.md` at root or a section in README. Keeping it in-repo as a committed artifact satisfies D-22 without creating a complex publishing pipeline.

---

## Research Finding 1: ADR Template Format

**Recommendation: Michael Nygard's five-section format.** [VERIFIED: github.com/joelparkerhenderson/architecture-decision-record]

### Canonical Template

```markdown
# ADR-XXX: [Title]

**Status:** [Proposed | Accepted | Superseded by ADR-YYY | Deprecated]

## Context

[The situation and forces at play — what problem are we navigating, what
constraints apply. Not the solution.]

## Decision

[What we are doing. Active voice.]

## Consequences

[What becomes easier and what becomes harder because of this decision.
Both positive and negative.]
```

**File naming:** `decisions/ADR-001-openscad-include-vs-use.md` (zero-padded number, kebab-case slug). Numbering is monotonically increasing; superseded ADRs update `Status:` and add a `Superseded by:` line; old file is not deleted.

### Why Nygard over MADR

MADR (Markdown Architectural Decision Records) adds: Context and Problem Statement, Decision Drivers, Considered Options, Confirmation, Pros and Cons of the Options, More Information. This is valuable when a team is comparing live alternatives.

For this project: all four ADRs have pre-decided content (D-18–D-21). The Nygard format captures the decision + rationale concisely, which serves the "legible public artifact" ethos better than a formal multi-option comparison table. The over-engineering here is in the toolchain, not in the ADR meta-format.

**Canonical source:** Michael Nygard's 2011 blog post "Documenting Architecture Decisions." The `adr.github.io` site lists seven templates; Nygard's remains the most widely adopted and the one cited in most tooling (adr-tools, etc.). [CITED: adr.github.io/adr-templates/]

### Four ADR Files — Exact Spec (from CONTEXT.md D-18–D-21)

| File | Decision | Key Rationale to Capture |
|------|----------|--------------------------|
| `ADR-001-openscad-include-vs-use.md` | `include <params.scad>` for variables; `use <...>` for modules; `$fn=12` during dev | `use` does not export variables — silent `undef` is the failure mode |
| `ADR-002-dollhouse-print-scale.md` | 1:25 scale, locked | Bambu Lab A1 bed (256×256mm) fits 144×168mm footprint; walls are ~3mm at 1:25 — printable |
| `ADR-003-modular-dollhouse-walls.md` | Floor base + swappable walls via printed joinery; joint mechanism deferred to Phase 6 | Composable wall modules from the start in `shell.scad` — cheap now, costly to retrofit |
| `ADR-004-semantic-color-integrity.md` | Brand inks carry their Signal Path type meaning always; no decorative reuse; Board boundary | `tokens.yaml` is a pinned snapshot that re-syncs when the Board changes |

---

## Research Finding 2: Label Generator Implementation

**Recommendation: Python + PyYAML + Python f-string SVG templates.**

### Rationale

The generator is ~60–80 lines of Python. The SVG structure is:
- A fixed outer `<svg>` with viewBox and style block
- One group for the wordmark: a `<rect>` (aubergine) + `<text>` (cream, Archivo)
- Eight groups for the ink-legend card: one per type, each a `<rect>` (type bg) + `<text>` (type on/fg, IBM Plex Mono) + `<text>` (meaning label, IBM Plex Mono, smaller)

Total SVG elements: ~30. This is not complex enough to justify an SVG library.

**Why Python over Node:**
- Python is already the validation runtime (`yamllint`, `check-jsonschema`)
- Adding `pip install PyYAML` is consistent with the existing Python toolchain setup
- The generator script lives alongside the validation scripts; same language = lower cognitive overhead
- Node would require adding `npm install yaml` to the project's package.json, pulling in the first npm dep for a project that currently has zero

**Generator structure:**
```python
# scripts/generate-labels.py
import yaml, sys, pathlib

def load_tokens(path):
    with open(path) as f:
        return yaml.safe_load(f)

def build_svg(tokens):
    types = tokens['types']
    base = tokens['base']
    roles = tokens['roles']
    typography = tokens['typography']
    # --- palette constants from tokens ---
    aubergine = roles['structure']['hex']   # probe identity = The Bench
    cream     = base['paper']['hex']
    ink       = base['ink']['hex']
    # --- SVG generation (f-strings) ---
    ...

tokens = load_tokens('design-system/tokens.yaml')
svg = build_svg(tokens)
out = pathlib.Path('design-system/labels/the-bench-labels.svg')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(svg)
print(f"Generated: {out}")
```

### Font Strategy in SVG

SVG `<text>` stores font-family as a reference, not embedded data. Three options:

| Strategy | Print Fidelity | Complexity | Recommendation |
|----------|---------------|------------|----------------|
| `font-family: 'IBM Plex Mono', 'Courier New', monospace` (fallback only) | Degrades to Courier New if font not installed | None | Use as baseline fallback |
| `@import` Google Fonts in SVG `<style>` | Correct in browser; degrades without internet | ~1 line | Add as primary |
| Embed base64 font data URI | True font everywhere | High — font files are 50–300KB per variant | Overkill for Phase 1 |
| Convert text to paths (Inkscape CLI) | Perfect, truly embedded | Requires Inkscape + extra step | Deferred |

**Recommended approach:** Include a `<style>` block with Google Fonts `@import` for browser rendering, plus `font-family` fallbacks for offline/print use. Add a comment in the generated SVG: "For print-ready PDF with embedded fonts, open in Inkscape > File > Save a Copy as PDF."

```svg
<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo:wght@700&family=IBM+Plex+Mono&display=swap');
  .wordmark-text { font-family: 'Archivo', system-ui, sans-serif; font-weight: 700; }
  .label-type    { font-family: 'IBM Plex Mono', 'Courier New', monospace; }
  .label-meaning { font-family: 'IBM Plex Mono', 'Courier New', monospace; }
</style>
```

**Why this works for this project:** The committed SVG will be viewed on GitHub (browser renders Google Fonts fine) and shared as a proof-of-work artifact. For the first physical print, the user opens in Inkscape with the fonts installed. The SVG-to-print pipeline does not need to be zero-click in Phase 1.

### Makefile Target

```makefile
labels: design-system/labels/the-bench-labels.svg

design-system/labels/the-bench-labels.svg: design-system/tokens.yaml scripts/generate-labels.py
	python3 scripts/generate-labels.py

validate:
	yamllint design-system/tokens.yaml

.PHONY: labels validate
```

---

## Research Finding 3: tokens.yaml Semantic Schema

**Recommendation: Custom human-legible YAML, not W3C DTCG format.**

### Why Not W3C DTCG

The W3C Design Tokens Community Group (DTCG) specification (first stable version: October 2025 — 2025.10) mandates JSON with `$value`, `$type`, `$description` keys. YAML support is community-convention, not spec. DTCG is optimized for toolchain interoperability (Figma plugins, Style Dictionary, CSS pipelines). [CITED: designtokens.org/tr/drafts/format/]

This project's token file is a pinned snapshot for: (1) the label generator and (2) manual sync into `params.scad`. No Figma plugin, no Style Dictionary pipeline, no CSS pipeline. The "legible artifact" ethos is better served by a schema a first-time reader understands in 30 seconds.

### Recommended `tokens.yaml` Shape

```yaml
# design-system/tokens.yaml
#
# Pinned snapshot of the Signal Path brand system.
# Source of truth: Board (private vault + live Ghost site).
# This repo REFLECTS the Board's color semantics — never INVENTS them.
# Propose new colors back to the Board as a Pulse/Component.
# Re-sync when Board brand changes (manual in v1; make sync-tokens in v2).

provenance:
  source: "https://davidnunez.com/about/#signal-path"
  snapshot_date: "2026-06-27"
  board_doc: "board-structure.md (private vault)"
  note: >
    Colors are owned upstream by the Board. This file is a pinned snapshot.
    TBD entries are gaps pending a Board decision — do not fill them here.

# ── Signal Path type system ────────────────────────────────────────────────
# Each type: bg (background ink), on (foreground/text on that bg), meaning
types:
  signal:
    bg: "#c63c82"
    on: "#fbeaf2"
    meaning: "a curiosity or spark worth tracking"
  probe:
    bg: "#4a2a57"
    on: "#f1eaf4"
    meaning: "hands-on exploration — where the depth lives"
  pulse:
    bg: "#e59a7d"
    on: "#3a1306"
    meaning: "ephemeral quick share (soft coral)"
  broadcast:
    bg: "#ec6a43"
    on: "#3a1306"
    meaning: "durable, built-to-travel share (persimmon)"
  module:
    bg: "#d7a53a"
    on: "#3a2a06"
    meaning: "reusable operational system"
  cadence:
    bg: "#8a5410"
    on: "#fbf2de"
    meaning: "recurring review rhythm"
  component:
    bg: "#15807c"
    on: "#e6f2f1"
    meaning: "distilled reusable insight"
  schematic:
    bg: "#2e7d52"
    on: "#e9f4ee"
    meaning: "speculative outline composing components"

# ── Base palette ───────────────────────────────────────────────────────────
base:
  paper:
    hex: "#f5efe2"
    role: "background / page"
  ink:
    hex: "#1a1820"
    role: "text / structure"
  surface:
    hex: "#ede7d5"
    role: "card background / slight contrast from paper"

# ── Named roles ────────────────────────────────────────────────────────────
roles:
  accent:
    hex: "#ec6a43"
    name: "persimmon"
    note: "Primary accent; also the broadcast type color."
  structure:
    hex: "#4a2a57"
    name: "aubergine"
    note: >
      Secondary accent; also the probe type color.
      The Bench is a Probe → aubergine on cream is its identity ink.

# ── Reserved / unbound inks ────────────────────────────────────────────────
# Defined but not assigned to any type. Available for future Board decisions.
reserved:
  cobalt:
    hex: "#2f5da8"
    status: "unbound"
    note: "Formerly broadcast ink; freed in 2026 brand rework."
  indigo:
    hex: "#5b53b0"
    status: "unbound"
    note: "Available for future assignment."

# ── Typography ─────────────────────────────────────────────────────────────
typography:
  display:
    family: "Archivo"
    weight: 700
    role: "headings, wordmark, large type"
  body:
    family: "Newsreader"
    weight: 400
    role: "prose, body copy"
  label:
    family: "IBM Plex Mono"
    weight: 400
    role: "tags, labels, metadata, code, bin labels"
```

### Schema Rationale

- **`provenance:` block first** — enforces the Board boundary on every read; cannot be missed
- **`types:` uses `bg`/`on`/`meaning`** — three fields per type, intuitive, maps directly to SVG generator variables
- **`base:` / `roles:` / `reserved:` separation** — matches the semantic model exactly (D-08 through D-13)
- **No `$value` / `$type` keys** — DTCG convention is tool-chain-targeted; this file's consumers are one Python script and one human reading it on GitHub
- **No flat palette** — the original "Bench five" (cream/near-black/terracotta/plum/magenta) is derivable from `base:` + `roles:` + `types.signal.bg` etc.; no need to duplicate

---

## Research Finding 4: MIT LICENSE + GitHub Repo Metadata

### MIT License

**Canonical text** from choosealicense.com (OSI-approved): [CITED: choosealicense.com/licenses/mit/]

```
MIT License

Copyright (c) 2026 David Nunez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Year:** Use `2026` (current year). No year range needed for a new repo.
**Holder:** `David Nunez` — first name + last name, no comma, no "Inc." (this is a personal project).

### GitHub Repository Metadata

These fields live in the repo's "About" sidebar on GitHub (Settings > General > Social Preview / Description / Topics / Website).

| Field | Recommended Value | Notes |
|-------|-------------------|-------|
| Description | "Physical home office/studio modeled as version-controlled code. Space as code — built in public." | Under 120 chars; uses "space as code"; avoids jargon |
| Website | `https://davidnunez.com` | Back-links to the Board's public presence per D-05 |
| Topics | `openscad`, `3d-printing`, `gridfinity`, `space-as-code`, `build-in-public`, `home-office`, `parametric-design`, `design-system` | 8 topics; mix discoverability (openscad, 3d-printing) + identity (build-in-public, space-as-code) |
| Social preview image | Defer to Phase 3 | No render exists yet; set after first committed render in Phase 3 |
| Include in GitHub search | Yes | Build-in-public requires discoverability |

**GitHub CLI commands (planner reference):**
```bash
# Set description and topics after repo is created
gh repo edit --description "Physical home office/studio modeled as version-controlled code. Space as code — built in public."
gh repo edit --add-topic openscad --add-topic 3d-printing --add-topic gridfinity \
  --add-topic space-as-code --add-topic build-in-public --add-topic home-office \
  --add-topic parametric-design --add-topic design-system
gh repo edit --homepage "https://davidnunez.com"
```

---

## Research Finding 5: Validation Tooling Scope

### What to Wire in Phase 1

| Check | Command | In Phase 1? | Rationale |
|-------|---------|-------------|-----------|
| `tokens.yaml` YAML syntax | `yamllint design-system/tokens.yaml` | YES | Catches malformed YAML immediately; zero new deps |
| `tokens.yaml` structure/schema | check-jsonschema with custom schema | NO — deferred | Writing a JSON Schema for the token schema is non-trivial; not worth the investment until Phase 2 when the file is consumed by the generator |
| Generator runs cleanly | `python3 scripts/generate-labels.py && test -s design-system/labels/the-bench-labels.svg` | YES (as `make labels` exit code) | The `-s` flag confirms the output is non-empty; catches silent failures |
| ADR files exist | Smoke check in planner / human verification | YES (manual) | No automated tooling needed; four files are either there or not |

**Minimal `make validate` in Phase 1:**
```makefile
validate:
	yamllint design-system/tokens.yaml
	@echo "tokens.yaml syntax: OK"
```

**Deferred:**
- JSON Schema for `tokens.yaml` (Phase 2 or later, after the schema is stable)
- yamllint for `equipment/inventory.yaml` (Phase 5, when the equipment manifest exists)

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| YAML parsing | Manual regex/split parser | PyYAML | YAML has edge cases (indentation, anchors, multi-line strings, bool coercion) that a hand-parser misses; PyYAML is 20+ years of correctness |
| ADR template | Custom bespoke format | Nygard 5-section template | Nygard is the community standard; tooling (adr-tools) and readers expect it |
| SVG font embedding | Base64-encode + embed fonts | `@import` Google Fonts + fallbacks | Font embedding adds 50–300KB per variant; for a committed artifact viewed on GitHub and shared as a proof-of-work, the @import approach is correct for Phase 1 |
| MIT license text | Custom license language | choosealicense.com canonical text verbatim | Any deviation from canonical text creates ambiguity and may void OSI-compatibility |

---

## Common Pitfalls

### Pitfall 1: Pulse-as-last-step Ordering
**What goes wrong:** README, tokens, ADRs are written in sequence; the repo goes live only after all four ADRs are committed. If anything in the middle stalls, no public artifact exists.
**How to avoid:** Commit and push after EACH deliverable. `git push` after README + LICENSE = pulse-ready repo. Generator + tokens = second pulse. ADRs = third. Nothing waits on everything else.

### Pitfall 2: Tokens Schema Drift
**What goes wrong:** The generator script hardcodes keys (`tokens['color']['cream']`) that don't match the actual tokens.yaml structure (`tokens['base']['paper']['hex']`). Silent `None` reference errors produce empty SVG or wrong colors.
**How to avoid:** Write the schema first; write the generator to exactly match the schema; run `make labels` as the integration test immediately after both are written.

### Pitfall 3: Invented Colors
**What goes wrong:** A color is needed and no Board value exists, so a value is invented in `tokens.yaml`. This violates D-21 (ADR-004) and the Board boundary in CLAUDE.md.
**How to avoid:** The `provenance:` block explicitly names the Board as source. Any gap gets a `"TBD — pending Board decision"` value, not an invented hex. The ADR-004 consequences section reinforces this.

### Pitfall 4: ADR Content Drift
**What goes wrong:** While writing ADR-003 (modular walls), the joint mechanism details are fleshed out, accidentally re-opening a deferred decision (the joint *mechanism* is explicitly deferred to Phase 6 per D-20).
**How to avoid:** Each ADR should state the *deferred* elements explicitly in Consequences: "Joint mechanism (dovetail vs. other) deferred to Phase 6." This is a feature of Nygard's Consequences section — it captures what is explicitly NOT decided.

### Pitfall 5: Social Preview as a Phase 1 Blocker
**What goes wrong:** The plan includes "set GitHub social preview image" in Phase 1. There is no render yet. This creates a blocking dependency on Phase 3.
**How to avoid:** GitHub social preview is deferred to Phase 3. The repo is public and navigable without it; a placeholder GitHub-generated card is sufficient.

---

## Code Examples

### Minimal label generator (structural pattern)

```python
# scripts/generate-labels.py
# Reads design-system/tokens.yaml → writes design-system/labels/the-bench-labels.svg
# Dependencies: PyYAML (pip install PyYAML)

import yaml
import pathlib

TOKENS_PATH = pathlib.Path("design-system/tokens.yaml")
OUTPUT_PATH = pathlib.Path("design-system/labels/the-bench-labels.svg")

def load_tokens():
    with open(TOKENS_PATH) as f:
        return yaml.safe_load(f)

def type_swatch(name, type_data, x, y, w=200, h=60):
    bg = type_data['bg']
    fg = type_data['on']
    meaning = type_data['meaning']
    return f'''  <g transform="translate({x},{y})">
    <rect width="{w}" height="{h}" fill="{bg}" rx="4"/>
    <text x="12" y="22" class="label-type" fill="{fg}">{name}</text>
    <text x="12" y="42" class="label-meaning" fill="{fg}">{meaning}</text>
  </g>'''

def build_svg(tokens):
    types = tokens['types']
    roles = tokens['roles']
    base = tokens['base']

    aubergine = roles['structure']['hex']
    cream     = base['paper']['hex']

    swatches = []
    for i, (name, data) in enumerate(types.items()):
        row, col = divmod(i, 2)
        swatches.append(type_swatch(name, data, x=col * 220 + 20, y=row * 80 + 160))

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated by scripts/generate-labels.py from design-system/tokens.yaml -->
<!-- For print-ready PDF: open in Inkscape with fonts installed > Save as PDF -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 560" width="480" height="560">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo:wght@700&family=IBM+Plex+Mono&display=swap');
    .wordmark  {{ font-family: 'Archivo', system-ui, sans-serif; font-weight: 700; font-size: 32px; }}
    .label-type    {{ font-family: 'IBM Plex Mono', 'Courier New', monospace; font-size: 14px; font-weight: 700; }}
    .label-meaning {{ font-family: 'IBM Plex Mono', 'Courier New', monospace; font-size: 10px; }}
  </style>
  <!-- Wordmark: The Bench — probe identity (aubergine on cream) -->
  <rect x="0" y="0" width="480" height="120" fill="{aubergine}"/>
  <text x="40" y="76" class="wordmark" fill="{cream}">the-bench</text>
  <!-- Ink legend: 8-type Signal Path system -->
{chr(10).join(swatches)}
</svg>'''

def main():
    tokens = load_tokens()
    svg = build_svg(tokens)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(svg, encoding='utf-8')
    print(f"Generated: {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
```

### Nygard ADR template (exact format)

```markdown
# ADR-001: OpenSCAD `include` vs `use` + `$fn` Convention

**Status:** Accepted

## Context

[The problem this decision addresses...]

## Decision

[What we are doing, in active voice...]

## Consequences

[What becomes easier and what becomes harder because of this decision...]
```

---

## State of the Art

| Area | Current Practice | Notes |
|------|-----------------|-------|
| ADR format | Nygard 5-section (2011) remains canonical | MADR offers more structure; overkill for pre-decided ADRs |
| Design tokens | W3C DTCG 2025.10 (stable) uses JSON `$value`/`$type` | YAML is human convention, not spec; DTCG is toolchain-optimized, not artifact-legibility-optimized |
| YAML parsing Python | PyYAML 6.0.3 (latest, 2024) | Stable; use `yaml.safe_load()` not `yaml.load()` (prevents arbitrary code execution) |
| MIT license | Unchanged canonical text; year = current year | No substantive changes to the license text |

**Deprecated / outdated:**
- `yaml.load()` without Loader argument: removed safe default in PyYAML 5.1+; always use `yaml.safe_load()`
- `npm install -g adr-tools`: the adr-tools CLI is useful for teams automating ADR numbering; not needed for a 4-ADR solo project where hand-numbering is fine

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | `pip install PyYAML` succeeds on Python 3.14.6 (PyPI shows 6.0.3 as latest) | Standard Stack | PyYAML may need a version pin if 3.14 has a C extension build failure; fallback is `pip install PyYAML==6.0.3` |
| A2 | Google Fonts `@import` in SVG renders correctly on GitHub's Markdown SVG renderer | Code Examples | GitHub may sandbox SVG and block external font requests; in that case the committed SVG falls back to system fonts in the GitHub preview, which is acceptable |

**If table were empty:** All claims in this research were verified or cited. The two assumptions above are low-risk edge cases, not blockers.

---

## Open Questions (RESOLVED)

1. **Pulse logging mechanism (SPINE-03)**
   - What we know: D-22 says "logged in-repo"
   - What's unclear: Whether a `PULSES.md` file, a `pulses/` directory with one file per pulse, or a section in README is preferred
   - Recommendation: Start with a `PULSES.md` at repo root (flat, no subdirectory overhead) with one entry per phase pulse. Simple, discoverable, on-brand for a legible artifact.
   - **RESOLVED:** `PULSES.md` at repo root — one entry per phase pulse. Locked in plan 01-04/Task 2.

2. **`decisions/` directory name**
   - What we know: Both ARCHITECTURE.md research and CONTEXT.md use `decisions/` for ADR files
   - What's unclear: Some projects use `adr/`, `doc/adr/`, or `docs/decisions/`
   - Recommendation: Use `decisions/` (already in the architecture research); keeps it adjacent to the project vocab (ADR = architectural *decision* record)
   - **RESOLVED:** `decisions/` (per ARCHITECTURE.md and CONTEXT.md). Used consistently across plan 01-03.

---

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3 | Label generator | Yes | 3.14.6 | — |
| Node 22 | npm scripts in Makefile (optional) | Yes | 22.23.0 | — |
| git | All commits | Yes | system | — |
| PyYAML | Generator YAML parsing | Not yet installed | 6.0.3 on PyPI | `pip install PyYAML` is the install step |
| yamllint | `make validate` | Not yet installed | current | `pip install yamllint` |
| check-jsonschema | `make validate` (equipment; tokens deferred) | Not yet installed | current | `pip install check-jsonschema` |
| Inkscape (optional) | Print-ready PDF with embedded fonts | Unknown | — | Generate SVG; user opens in Inkscape; not a Phase 1 gate |

**Missing with no fallback:** None — all Phase 1 work is Python + git + hand-authored files.

**Missing with fallback (pip install):** PyYAML, yamllint, check-jsonschema — standard pip install; no blockers.

---

## Validation Architecture

> `nyquist_validation: true` is set in `.planning/config.json`.

Phase 1 deliverables are primarily committed text artifacts. The appropriate validation is proportional: file-existence checks, YAML syntax, and generator smoke test. No unit test framework needed.

### Test Approach

| Req ID | Behavior | Test Type | Automated Command | Exists? |
|--------|----------|-----------|-------------------|---------|
| DSGN-01 | `tokens.yaml` parses without error | Lint | `yamllint design-system/tokens.yaml` | No — Wave 0: add to Makefile |
| DSGN-01 | `tokens.yaml` contains all 8 type keys | Smoke | `python3 -c "import yaml; t=yaml.safe_load(open('design-system/tokens.yaml')); assert len(t['types'])==8, 'missing types'"` | No — Wave 0: add as `make validate` step |
| DSGN-03 | Generator produces non-empty SVG | Smoke | `python3 scripts/generate-labels.py && test -s design-system/labels/the-bench-labels.svg` | No — Wave 0: part of `make labels` |
| SPINE-04 | LICENSE file contains "MIT License" | Smoke | `grep -q 'MIT License' LICENSE` | No — human check acceptable |
| CODE-06 | All 4 ADR files exist | Smoke | `ls decisions/ADR-00{1,2,3,4}-*.md` | No — human check acceptable |

### Wave 0 Gaps

- [ ] `make validate` target: add yamllint on `tokens.yaml` + 8-types assertion
- [ ] `make labels` target: invoke generator + `-s` check on output file
- [ ] `Makefile` must declare `.PHONY: validate labels`

### Sampling Rate

- Per task: run `make validate` after any change to `tokens.yaml`; run `make labels` after any change to generator or tokens
- Per phase gate: `make validate && make labels` both green before marking Phase 1 complete

---

## Security Domain

> `security_enforcement` not set in config — treating as enabled per instructions.

Phase 1 has no runtime components, no user inputs, no network services, and no authentication. ASVS categories do not apply.

| ASVS Category | Applies | Note |
|---------------|---------|------|
| V2 Authentication | No | No auth in this phase |
| V3 Session Management | No | No sessions |
| V4 Access Control | No | No access control |
| V5 Input Validation | Minimal | Generator reads local YAML file; `yaml.safe_load()` prevents arbitrary object deserialization |
| V6 Cryptography | No | No crypto |

**Only security action:** Use `yaml.safe_load()` (not `yaml.load()`) in the generator — prevents arbitrary Python object instantiation from a maliciously crafted YAML file. This is a two-word fix in the generator script.

---

## Sources

### Primary (HIGH confidence)

- [choosealicense.com/licenses/mit/](https://choosealicense.com/licenses/mit/) — canonical MIT license text, verified
- [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md) — Nygard ADR template, section headers verified
- [adr.github.io/adr-templates/](https://adr.github.io/adr-templates/) — ADR template catalogue; confirms Nygard as foundational
- [designtokens.org/tr/drafts/format/](https://www.designtokens.org/tr/drafts/format/) — W3C DTCG spec (2025.10 stable); confirms JSON-first approach and `$value`/`$type` convention
- PyPI registry — `PyYAML 6.0.3`, `yamllint`, `check-jsonschema`: all [OK] via slopcheck 0.6.1
- npm registry — `js-yaml 5.2.0` (created 2011-11-02, no postinstall), `yaml 2.9.0` (created 2011-04-15, no postinstall): legitimate but not used in Phase 1
- Runtime versions: `node 22.23.0`, `python3 3.14.6` — verified locally

### Secondary (MEDIUM confidence)

- [MDN: Using fonts in SVG](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Using_fonts) — confirms `@font-face`/`@import` approach for SVG text; confirms text-to-paths as the true print-safe option
- [svgmaker.io: SVG Text & Fonts](https://svgmaker.io/blogs/svg-text-fonts-complete-guide-to-typography-in-svg) — confirms font-reference vs. embedding trade-offs
- [W3C community/design-tokens](https://www.w3.org/community/design-tokens/) — confirms DTCG is JSON-primary, YAML is community convention

---

## Metadata

**Confidence breakdown:**
- ADR template format: HIGH — canonical source verified
- Label generator approach: HIGH — runtime versions verified, PyYAML slopcheck [OK], SVG font strategy grounded in MDN docs
- tokens.yaml schema: HIGH — design derived directly from locked CONTEXT.md D-08 through D-13; DTCG comparison verified
- MIT license: HIGH — canonical text from choosealicense.com (OSI)
- GitHub metadata: MEDIUM — GitHub's About section fields are well-known; specific topic values are [ASSUMED] recommendations

**Research date:** 2026-06-27
**Valid until:** 2026-09-27 (90 days; stable domain — ADR format and MIT license do not change)

---

*Phase: 01-public-spine-design-system-adrs*
*Research completed: 2026-06-27*
