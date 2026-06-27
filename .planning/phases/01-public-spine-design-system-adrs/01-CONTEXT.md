# Phase 1: Public Spine + Design System + ADRs - Context

**Gathered:** 2026-06-27
**Status:** Ready for planning

<domain>
## Phase Boundary

Stand up the **public spine** of the probe — a live GitHub repo a stranger can land on and understand — with **zero dependency on OpenSCAD or measuring the room**. Concretely, Phase 1 ships:
- A README framing the probe (thesis + orientation), in David's voice
- An open LICENSE + public-facing metadata
- `design-system/tokens.yaml` — the semantic brand-token system, materialized in-repo
- A printable label SVG **generated** from those tokens (the design-system → physical bridge)
- Four load-bearing ADRs locked before any `.scad` file is written
- The phase's own pulse-ready proof-of-work (the live repo itself)

Requirements in scope: **SPINE-01, SPINE-03, SPINE-04, CODE-06, DSGN-01, DSGN-03.**

Out of scope (later phases): any OpenSCAD model, room shell, renders, measurement, equipment manifest, the actual doll-house print. New capabilities belong to their own phases.
</domain>

<decisions>
## Implementation Decisions

### README & spine (SPINE-01)
- **D-01:** README is a **genuine, conventional GitHub README** — title + tight thesis up top, then what-it-is / repo structure / how-it-works / examples / status / license + back-link. Standard bones; orientation over theater.
- **D-02:** A real **thesis/manifesto section** sits near the top — before→alive · environment-as-provenance · the over-engineering is deliberate — kept tight (a section, not a billboard).
- **D-03:** Written in **David's voice** per `branding-brief.md`: first-person, "curious veteran," lead-with-the-made-thing, plain/vivid/specific, em-dashes, "not X — but Y," house caps (Signal/Probe/Pulse/The Bench), wit that earns its place. Banned: guru-fluff (unlock/leverage/"fast-paced world"), confessional pre-frames, purple prose, credential-leading. Conventional structure, unconventional soul — a casual visitor should feel something unusual is happening *and* that it respects standards.
- **D-04:** **Audience model:** optimize for whoever finds the repo *later*, when it's more rendered — not a day-one stranger watching commits. "It exists at all" is the proof-of-work. (This retires the "how do we feel alive with no render yet" constraint — it's moot.)
- **D-05:** **Board back-link:** link to davidnunez.com's "The Bench" presence and name the Signal → Probe → Pulse framing in-repo. The governing Signal itself lives in a private vault, so the public back-link points at the public site, not the vault note.

### License (SPINE-04)
- **D-06:** **MIT, whole repo.** One LICENSE file — maximally generous and friction-free, including brand assets and future WIP photography. On-brand for "be a useful example, invite don't pitch." Chosen over a dual MIT+CC-BY split and over reserving brand/photos.

### Design system & semantic tokens (DSGN-01)
- **D-07:** `design-system/tokens.yaml` encodes the **semantic** layer (color = meaning), not a flat palette. It is a **pinned, in-repo snapshot** of the Board's brand system, materialized so the public repo is self-contained. Provenance cited (see canonical refs).
- **D-08:** The canonical color system is the **eight-label Signal Path type system** (from the live `/about/#signal-path` + `board-structure.md`). Exact values to materialize:

  | Type | Bg hex | On (fg) hex | Meaning |
  |------|--------|-------------|---------|
  | signal    | `#c63c82` | `#fbeaf2` | a curiosity/spark worth tracking |
  | probe     | `#4a2a57` | `#f1eaf4` | hands-on exploration — "where the depth lives" |
  | pulse     | `#e59a7d` | `#3a1306` | *ephemeral* quick share (soft coral) |
  | broadcast | `#ec6a43` | `#3a1306` | *durable*, built-to-travel share (persimmon) |
  | module    | `#d7a53a` | `#3a2a06` | reusable operational system |
  | cadence   | `#8a5410` | `#fbf2de` | recurring review rhythm |
  | component | `#15807c` | `#e6f2f1` | distilled reusable insight |
  | schematic | `#2e7d52` | `#e9f4ee` | speculative outline composing components |

  **Base:** paper `#f5efe2` · ink `#1a1820` · surface `#ede7d5`.
  **Roles:** accent = persimmon `#ec6a43` · structure = aubergine `#4a2a57`.
  **Type stack:** Archivo (display) · Newsreader (serif body) · IBM Plex Mono (labels/tags/meta).
- **D-09:** **Key nuance — pulse vs broadcast split:** pulse = soft coral `#e59a7d` (ephemeral/fragile); broadcast = bold persimmon `#ec6a43` (durable/built-to-travel). They are sibling *sharing* forms split on intent. Do not collapse them.
- **D-10:** **Places carry no distinct ink:** Bench / Rack / Board are *places where the path evolves*, not path stages → they carry **paper/cream**, no type color (per David's call).
- **D-11:** `cobalt #2f5da8` and `indigo #5b53b0` are defined-but-**unbound** inks (cobalt was formerly broadcast; freed in this rework). Record as available/reserved, not assigned.
- **D-12:** Token set is the **full** system (all 8 types + base + roles), not a velocity-layer subset. The original "Bench five" (cream/near-black/terracotta/plum/magenta) is a strict subset of this.
- **D-13:** **The Bench's own identity = a Probe → aubergine on cream.** The repo is a Probe in the Signal Path framework; weekly proof-of-work artifacts are Pulses (soft coral); anything built-to-travel is a broadcast (persimmon).

### Label generator (DSGN-03)
- **D-14:** `make labels` is a **real generator** — a small script (Node or Python) reads `tokens.yaml` and emits SVG. Not hand-authored, not a stub. The design-system → physical pipeline genuinely runs (on-theme: the over-engineering is visible and honest).
- **D-15:** First `make labels` output = **the `the-bench` wordmark** (aubergine on cream — the repo's probe identity) **+ an eight-label ink-legend card** (each tag as a dot/swatch with its content-type meaning, IBM Plex Mono, echoing the dot-in-square mark). The legend is the printed instantiation of the meaning-system itself.
- **D-16:** **No bin label yet** — the connection is too thin in Phase 1 (no bins exist). It arrives in v2 when Gridfinity bins exist; the generator will already be there to produce it.
- **D-17:** **Zone/mode coloring is deferred to Phase 5.** The three room modes (deep-focus / creator-filming / electronics-maker) are a *different axis* from the Signal Path types; reconciling modes ↔ activities ↔ inks is its own piece of thinking. Until then, never color a mode label with a type ink (would collide with its locked meaning).

### ADRs (CODE-06) — four ADRs, locked before any `.scad`
- **D-18:** **ADR-001 — OpenSCAD `include` vs `use` + `$fn` convention.** `include <params.scad>` for the parameter file (because `use` won't export variables → silent `undef`); `use <…>` for furniture/module files (definitions only, no geometry at origin); `$fn` low (≈12) during dev, raised only for committed renders/exports. Pre-decided by research; write to that spec.
- **D-19:** **ADR-002 — doll-house print scale = 1:25.** Locked now (success criterion requires it). Rationale: Bambu Lab A1 (256×256 bed) fits the whole 1:25 footprint (~144×168mm for a ~3.6×4.2m room) and any single wall (~168mm) easily; at 1:25 walls are ~3mm — thick enough for printed joinery (see ADR-003). Exact joint feature-size verification is a Phase 6 checkpoint. AMS enables printing walls in meaning-bound brand inks (ties to ADR-004).
- **D-20:** **ADR-003 — modular doll-house: floor base + swappable walls via printed joinery.** The doll-house decomposes into a floor/base + individual swappable walls joined by *printed* connectors (dovetail-or-similar), so it can be iterated (reprint one wall to add shelving mounts) — the printed model becomes a living, version-controlled physical object. **Phase-1 footprint:** capture the architecture + the scale/feature-size constraint now; this directs Phase 2 to build `shell.scad` as **composable wall modules from the start** (cheap now, costly to retrofit). The joint *mechanism* (dovetail vs. other) is deferred to Phase 6.
- **D-21:** **ADR-004 — semantic color integrity (+ reflect-don't-invent + Board boundary).** Brand inks always carry their Signal Path type meaning and are never reused decoratively to mean something else (governs every render, label, and future lighting scene). The Bench repo **reflects** the Board's color semantics, never **invents** them (CLAUDE.md Board boundary: identity is read-only from the Board; insights/artifacts flow back as Pulses/Components). Gaps are marked "pending — owned by the Board"; any proposed new color routes back to the Board, not canonized here. `tokens.yaml` is a pinned snapshot that re-syncs when the Board changes (manual in v1; `make sync-tokens` is a v2 idea).

### Phase pulse (SPINE-03)
- **D-22:** The Phase 1 pulse-ready proof-of-work **is the live public repo itself** — spine + tokens + first generated label (wordmark + ink legend) + the four ADRs. Logged in-repo; broadcasting it is out-of-repo (A4/A5).

### Claude's Discretion
- Exact `tokens.yaml` YAML schema shape (nesting, key names) — encode the semantic structure above faithfully; planner/executor choose the concrete shape.
- Generator language (Node vs Python) and exact SVG layout of the wordmark + legend card.
- README section ordering details and exact ADR file formatting (use a lightweight standard ADR template).
- Repo metadata specifics (GitHub description, topics, social-preview) beyond "appropriate for a build-in-public project."
</decisions>

<specifics>
## Specific Ideas

- The Bench *is a Probe* → aubergine ("where the depth lives") is its identity color by definition, not preference. Wordmark = aubergine on cream.
- The five original "Bench" colors turned out to be exactly paper + ink + part of the Signal Path velocity layer — the system was already coherent, just unnamed.
- The brand is a **moving target** (the source-of-truth color system was dramatically reworked mid-discussion: pulse/broadcast split, schematic+cadence added). `tokens.yaml` is therefore explicitly a *pinned snapshot with provenance*, re-synced on change.
- An honest "TBD — owned upstream by the Board" marker for uncolored terms is itself on-brand (over-engineering as legible artifact).
</specifics>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.** Note: exact hex values are **materialized into `design-system/tokens.yaml`** during this phase, so the public repo is self-contained; the external sources below are *provenance* and may change.

### Brand color semantics (authoritative — color = meaning)
- Live page `http://localhost:2368/about/#signal-path` — **the eight-label Signal Path type system + exact colors** (authoritative; moving target). Colors resolve via `--ink-{type}` / `--ink-{type}-on` in the Ghost theme's built CSS (`/assets/built/index.css`). The values captured in D-08 are the current snapshot.
- `/Users/davidnunez/Ideaverse/.claude/rules/board-structure.md` — Signal Path vocabulary (Signal/Probe/Pulse/Module/Component/Schematic/Cadence/Trace) + the Board / Bench / Rack **place** definitions + the **Board boundary** (identity read-only from the Board).
- `/Users/davidnunez/Ideaverse/Works/Signal Path Framework.md` — framework semantics (Signal→Probe→Pulse→Module; Component→Schematic knowledge layer; Cadence rhythms).

### Voice, mark, type stack (NOT color assignments — those are superseded)
- `/Users/davidnunez/src/davidnunez.com.ghost/docs/branding-brief.md` — voice & personality ("curious veteran"; voice do/don't), the dot-in-square mark system (square=constant · dot position=how-public · dot color=content-type), and the type stack (Archivo / Newsreader / IBM Plex Mono). **Its essay/artifact/experiment ink labels are two revisions stale — do not use for color meaning.**
- `/Users/davidnunez/Ideaverse/AI/Context/davidnunez-rebrand-about.html` — supporting voice exemplars (about-page draft). Note: its inline tag colors are an *older* version; the live page (above) supersedes.

### Doll-house structure (Phase 6 reference, captured now)
- `https://github.com/doratracyer/floor_plan` — SVG → 3D-printable doll-house floor-plan structure lessons; informs the floor-base + swappable-walls decomposition (ADR-003).

### In-repo / project
- `CLAUDE.md` (repo root) — stack constraints, brand constraints, **Board boundary**, OpenSCAD `@snapshot` requirement.
- `.planning/research/{STACK,ARCHITECTURE,FEATURES,PITFALLS,SUMMARY}.md` — toolchain + architecture + pitfalls (research already done; `make labels`/`make validate`/`make renders` skeleton, include-vs-use, scale math).
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **No application code exists yet** — repo currently holds only `CLAUDE.md` + `.planning/`. The "reusable assets" for this phase are the research docs and the locked brand/decision system, not existing code.
- `.planning/research/STACK.md` already specifies the `design-system/` layout and Makefile targets (`make validate`, `make renders` no-op until Phase 2, `make labels`).

### Established Patterns
- **Board boundary (CLAUDE.md):** strategy/identity/brand is read-only from the Board; artifacts flow back as Pulses/Components. Directly governs ADR-004 and `tokens.yaml`.
- **Single-source-of-truth ethos:** `tokens.yaml` → (manually in v1) `params.scad` COLOR_* + SVG labels; `make sync-tokens` is a v2 automation idea.
- **Pulse cadence:** every phase ends with a committed, pulse-ready proof-of-work.

### Integration Points
- `design-system/tokens.yaml` is the contract consumed by **both** the label generator (this phase) and Phase 2's `params.scad` COLOR_* constants.
- ADR-003 (modular walls) is an **upstream constraint on Phase 2's `shell.scad`** — it must be built as composable wall modules.
- ADR-001 (include/use) constrains every `.scad` file written from Phase 2 onward.
</code_context>

<deferred>
## Deferred Ideas

- **Dynamic, color-shifting space (v2 — lighting/AUTO).** Lighting (and someday robotic reconfiguration, e.g. the camera tucks away for admin work) makes the *room itself* the living dot-in-square: the active Signal Path mode (signal / probe / pulse / broadcast…) becomes the lighting scene; "how public" tracks filming-on/off. David's framing: "a joyful and meaningful design playground." The highest-energy idea in the project — log richly; surface at the v2 lighting milestone (AUTO-01/02/03).
- **Livestreaming the Bench (v2 — FILM).** "Watch me work live" for co-working / body-doubling. Surfaces with FILM-01/02.
- **Mode ↔ Signal-Path-activity ↔ ink reconciliation (Phase 5).** The three room modes (deep-focus/creator-filming/electronics-maker) and the eight Signal Path types are different axes; reconcile when annotating modes in Phase 5. Only then assign any mode→color mapping.
- **Color proposals for uncolored terms (a future Pulse).** Schematic/Cadence now have colors, but Bench/Rack/Board are intentionally cream. Any future need for a place-color or new ink is proposed *back to the Board* as a Pulse/Component, never canonized in this repo.
- **`make sync-tokens` automation (v2).** Auto-sync `tokens.yaml` → `params.scad` COLOR_* once the model exists and the brand keeps moving.
- **Bin-label template (v2).** Generated by the same `make labels` pipeline once Gridfinity bins exist.

---

*Phase: 01-public-spine-design-system-adrs*
*Context gathered: 2026-06-27*
</deferred>
