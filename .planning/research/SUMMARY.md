# Project Research Summary

**Project:** The Bench — living version-controlled "space as code" model of a physical home office/studio
**Domain:** Parametric digital twin of a physical space, built in public as a Signal Path Probe
**Researched:** 2026-06-27
**Confidence:** HIGH

---

## Executive Summary

The Bench is a build-in-public probe in which a real home office/studio is modeled as a parametric, version-controlled OpenSCAD codebase — "space as code." The defining differentiator is not the furniture layout but the *philosophy*: environment-as-provenance, the thesis that a physical environment becomes part of the soul of the work produced within it. The repo, its renders, its commits, and its doll-house floor plan ARE the artifact, not documentation of a separate artifact. Research across all four domains converges on one load-bearing rule: **the public spine ships first, before any tape measure is picked up.** This inverts the order that killed v0, which buried "space as code / shareable content" at Phase 10 and stalled at 4% behind a measurement gate.

The recommended approach is a strict two-milestone split: v1 = public spine + parametric model of the room as-is + 3D-printed doll-house floor plan + first pulse; v2+ = physical redesign using the v1 model and manifest as inputs. The toolchain is lean and fully verified: `openscad@snapshot` (not the bare cask, which installs deprecated 2021.01) as the parametric engine; BOSL2 + QuackWorks as the single-repo organizer ecosystem (Gridfinity, openGrid, Underware, Neogrid 2.0); committed PNGs in `renders/` as the proof-of-work public surface. The organizer ecosystem (all four systems via QuackWorks) is a central v2 deliverable and must appear as concrete, sequenced phases — not a single "organize the office" bucket.

The primary risks are both from the v0 post-mortem: (1) the measurement gate stall, which is prevented by design — `params.scad` ships on day one with `ESTIMATED` values clearly marked, and the public spine has zero dependency on measured room dimensions; (2) planning capital inversion, prevented by ensuring every phase produces a pulse-ready artifact as its first or second deliverable, never as its last. A third risk unique to this toolchain is OpenSCAD technical debt: `use` vs `include` confusion, F5-instead-of-F6 STL exports, and high `$fn` during development all compound as the model grows. These must be locked in ADR-001 before a line of `.scad` is written.

---

## Key Findings

### Recommended Stack

The stack is OpenSCAD-centric and intentionally minimal. OpenSCAD snapshot (`brew install --cask openscad@snapshot`, v2026.06.12) is the only viable choice: the bare `openscad` cask installs deprecated 2021.01 (disabled September 1 2026) and is incompatible with QuackWorks which explicitly requires a developer release. The Manifold backend (enabled in Preferences after install) reduces render time from minutes to seconds on complex models — critical for the weekly-pulse cadence.

The organizer ecosystem is a single git submodule: `AndyLevesque/QuackWorks` (99.2% OpenSCAD) provides Underware 2.0, openGrid, Neogrid 2.0, and Deskware in one pull. `BelfrySCAD/BOSL2` (v2.0.745) is QuackWorks' only external dependency and provides the attachment system and precision geometry needed beyond basic boxes. `kennetek/gridfinity-rebuilt-openscad` (v2.0.0) is the canonical Gridfinity implementation. All three are pinned as git submodules in `models/lib/` and resolved via `OPENSCADPATH`. The `doratracyer/floor_plan` repo is the reference for the doll-house pipeline; the OpenSCAD-native path (`linear_extrude` on a `polygon()` room outline) is recommended for v1 over the SVG import path, as it re-uses `params.scad` directly.

Supporting tools are Python-only (`yamllint`, `check-jsonschema`) and already available (python3 is present). GNU Make is the build pipeline (`make renders`, `make stl`, `make validate`). Node 22 is present for npm script wrappers but carries no logic.

**Core technologies:**
- `openscad@snapshot` (2026.06.12): parametric room model, renders, STL export — the only scriptable, plain-text solid modeler with a git-diffable workflow
- BOSL2 (v2.0.745): required dependency for QuackWorks; attachment system and precision geometry for furniture beyond basic boxes
- QuackWorks (`main`): single source for all four organizer systems (Underware, openGrid, Neogrid 2.0, Deskware) — one submodule pull
- Gridfinity Rebuilt (v2.0.0, kennetek): canonical Gridfinity OpenSCAD implementation; most widely adopted, most community add-ons target it
- GNU Make + OpenSCAD CLI: headless render pipeline; `make renders` produces all committed PNGs
- `yamllint` + `check-jsonschema`: YAML syntax and schema validation for the equipment manifest

**Critical version note:** `openscad@snapshot` (not `openscad`) is mandatory. QuackWorks will not work on 2021.01 stable. This is the single highest-impact installation decision.

### Expected Features

**Must have (v1 — table stakes for probe credibility):**
- Public repo spine: README with thesis (before→alive; environment-as-provenance), identity, brand, back-link to governing Board Signal — ships before room is measured
- Parametric room model as-is: `params.scad` as single source of truth; `shell.scad`; furniture primitives; three modes (deep-focus / creator-filming / electronics-maker) as zone annotations
- One-command render pipeline: `make renders` → committed PNGs in `renders/`; model is live, not aspirational
- Equipment/inventory manifest: YAML, zone-tagged, mode-tagged, refreshed from the-bench-old
- Design system / brand tokens: `design-system/tokens.yaml` (palette + type); OpenSCAD `COLOR_*` constants in `params.scad`; palette = cream `#f5efe2` / near-black `#1a1820` / terracotta `#ec6a43` / plum `#4a2a57` / magenta `#c63c82`
- Doll-house 3D-printed scale floor plan: the tangible v1 artifact; OpenSCAD model → STL → printed; scale ADR required before modeling (1:25 vs 1:50 — see technical flags below)
- Pulse-ready mechanism: `pulses/` directory format; first entry = doll-house print photo
- ADR log: `decisions/ADR-001-openscad-include-strategy.md` committed before first `.scad` file

**Should have (v2 — organizer ecosystem, most-visible-first):**
- Gridfinity desk + drawer layer (42mm grid): custom bin models committed as `.scad`; layout planned from manifest; prototype-one-before-batch mandatory
- openGrid wall layer (28mm grid): mounted above maker bench; replaces ad-hoc pegboard; most visible physical change
- Underware cable management: under-desk + on-wall channels; PETG option for LED diffusion; critical for creator-filming mode (clean frame)
- Neogrid 2.0 drawer management: parametric connectors + cut-to-size panels for large items; fills gap between Gridfinity bins and unorganized drawers
- Physical bin label templates: SVG templates driven by brand tokens + IBM Plex Mono; the design-system-to-physical-world bridge
- Home Assistant mode scenes in git: `config/home-assistant/` YAML; Focus/Filming/Maker/Ambient scenes; mmWave presence sensor
- Creator-filming mode physical: three-point lighting, eye-level camera arm, curated background depth layers, OBS scene config

**Defer (v2+ only — not v1 scope):**
- Physical redesign execution (the actual buy/install/build of the redesigned room)
- Broadcasting/publishing pipeline (out of scope by design; repo emits pulse-ready artifacts only)
- Acoustic treatment (requires camera background coordination; defer to v2)
- Basement extension
- Dedicated DSLR upgrade

**Hard anti-features (never build in this repo):**
- AI-generated imagery (violates environment-as-provenance spine)
- RGB / gaming aesthetics
- SweetHome 3D, Fusion 360, Blender for rendering, Tinkercad, JSCAD — all excluded
- Waterfall "finish all planning before shipping" gate

### Architecture Approach

The architecture is a strict single-source-of-truth parametric model with five layers composing strictly downward: `params.scad` (dimensions + color constants, root-level) → `model/room/shell.scad` → `model/furniture/*.scad` → `model/zones/*.scad` → `views/*.scad` → `renders/*.png` (committed). The data layer (`inventory/manifest.yaml`, `design-system/tokens.yaml`) is independent of the model layer and feeds label generation, not OpenSCAD geometry. GNU Make orchestrates everything: `make renders`, `make validate`, `make labels`. The repo itself IS the public surface — no separate publishing pipeline.

**Major components:**
1. `params.scad` (root): single source of truth for ALL dimensions (with `// ESTIMATED` markers before measurement) and ALL `COLOR_*` constants from tokens.yaml; every `.scad` file begins with `include <params.scad>` using `include` not `use`
2. `model/` hierarchy: composes strictly downward; `shell.scad` has no knowledge of furniture; zones assemble shell + furniture + accessories; storage (`model/storage/`) is deferred to v2+
3. `views/` as render drivers: thin files that compose zones, set camera position via Makefile CLI args, and exist only to produce one PNG each; never imported by anything
4. `renders/` (committed, never gitignored): the proof-of-work public artifact; GitHub renders the PNGs inline in README.md; committing them is what makes the repo "alive" to a stranger
5. `design-system/tokens.yaml`: canonical brand palette; flows manually (v1) into `params.scad` COLOR_* constants AND into SVG label templates; `make sync-tokens` automates in v2+
6. `inventory/manifest.yaml`: structured equipment data, independent of `.scad` files; shares zone vocabulary with the model but does not import or export geometry
7. `decisions/`: ADR log; ADR-001 (include vs use) must be committed before first `.scad` file

**Key architectural pattern:** `include <params.scad>` for the parameter file (because `use` does not export variables — only modules/functions — causing silent `undef` failures); `use <model/furniture/X.scad>` from zone files (imports module definitions only, prevents geometry executing at origin).

### Critical Pitfalls

1. **Measurement gate stall** — The v0 failure mode, documented: stalled at 4% because "measure the room" blocked publishing the README. Prevention: `params.scad` ships day one with `ESTIMATED` values explicitly marked; the public repo goes live before any tape measure is picked up. Warning sign: any phase plan that lists "measure room" before "publish README."

2. **Planning capital inversion** — Spending all early energy on internal scaffolding (ADR templates, YAML schemas, directory conventions) before a stranger-visible artifact ships. Prevention: every phase produces a pulse-ready public deliverable as its first or second plan, never its last. Warning sign: three "setup" plans before the first shareable output.

3. **Cascading wait gates** — v0's roadmap chained: "2–4 week HA manual validation" → "2–4 weeks real Gridfinity usage patterns" → "presence automation only after manual scenes stable" = potential 6–8 week mandatory idle. Prevention: no wait gate exceeds two weeks; parallel deliverable required during any wait period. HA validation and Gridfinity baseplate modeling can run concurrently.

4. **OpenSCAD F5/F6 confusion** — Exporting STL from F5 preview produces broken geometry (non-manifold errors) that slicers silently accept and print badly. Prevention: F6 render pipeline only for all STL artifacts committed to repo; add this to `Makefile` as the enforced path. Never use File > Export for committed STLs.

5. **Gridfinity batch print before fit verification** — Printing a full drawer set of Gridfinity baseplates before verifying one prototype fit. IKEA Alex drawer inner usable dimensions are not the outer dimensions; rail clearance and tolerances can make the entire batch unusable. Prevention: prototype-one-before-batch is a mandatory plan in the storage phase; batch print is blocked until a prototype fit photo is committed.

6. **Scope sprawl** — Broadcasting operations, audio production, full-home renovation, and channel ops all look like legitimate project work. Prevention: PROJECT.md Out of Scope list is a hard boundary; scope recheck at every `/gsd:transition`.

---

## Implications for Roadmap

Research converges on a clear two-milestone, 11-phase structure. v1 = spine + parametric model + doll-house print (the "before"). v2+ = physical redesign using v1 as input, sequenced by the physical-dependency checklist.

### v1 Milestone: "Before" + Spine + Doll-House

---

### Phase 1: Public Spine (Zero Measurement Dependency)

**Rationale:** This is the load-bearing inversion over v0. The public artifact must exist before any physical task is required. Measurement does not gate this phase; nothing gates this phase. Ship it in the first session.

**Delivers:**
- `README.md` with thesis (before→alive; environment-as-provenance), brand identity, back-link to Board Signal, placeholder `img` tag for first render
- `.planning/PROJECT.md`, `ROADMAP.md`, `STATE.md` — substantive, not stubs
- `design-system/tokens.yaml` — canonical palette + type tokens (the visual identity for all downstream surfaces)
- `design-system/labels/label-template.svg` — a printable label template demonstrating design-system-to-physical pipeline immediately
- `Makefile` skeleton — `make validate`, `make renders` (no-op until Phase 2), `make labels` targets defined
- `decisions/ADR-001-openscad-include-strategy.md` — `include` vs `use` decision logged BEFORE any `.scad` is written
- `decisions/ADR-002-doll-house-print-scale.md` — 1:25 vs 1:50 scale calculated and decided BEFORE floor plan is modeled (see technical flags)

**Avoids:** Measurement gate stall (Pitfall 1); Planning capital inversion (Pitfall 2)

**Pulse artifact:** Live public repo on GitHub with thesis, brand tokens, label template, and ADR. Provable without measurements.

**Research flag:** Standard patterns — skip research phase. README and ADR writing require no additional research.

---

### Phase 2: Parametric Foundation (Estimated Dims OK)

**Rationale:** OpenSCAD installed here. `params.scad` ships with ESTIMATED dimensions clearly marked — the model runs, renders, and commits immediately. The first committed render is the first visual proof-of-work. Measurement is still non-blocking.

**Delivers:**
- `brew install --cask openscad@snapshot` (not bare cask) + Manifold backend enabled
- `params.scad` at root — all ESTIMATED dimensions marked `// ESTIMATED`, all `COLOR_*` constants from tokens.yaml
- `model/room/shell.scad` — room boundary with estimated dims
- `views/top-plan.scad` → `renders/top-plan.png` — FIRST COMMITTED RENDER; updates README.md img tag
- `model/furniture/standing-desk.scad`, `model/furniture/maker-bench-table.scad`
- `model/zones/focus-desk.scad`, `model/zones/maker-bench.scad`
- `views/iso-overview.scad` → `renders/iso-overview.png` — isometric "before" room in code
- Git submodules added: BOSL2, gridfinity-rebuilt, QuackWorks, floor_plan

**Uses from STACK.md:** `openscad@snapshot`; `OPENSCADPATH` env var; `include` vs `use` pattern from ADR-001; `$fn=12` during development

**Avoids:** `include`/`use` confusion (Architectural Anti-Pattern 4); dimensions outside `params.scad` (Architectural Anti-Pattern 2); high `$fn` during development (Performance Trap 1)

**Pulse artifact:** OpenSCAD floor plan + isometric render of the "before" room, committed and visible on GitHub.

**Research flag:** Standard patterns — skip research phase. OpenSCAD CLI patterns and submodule setup are well-documented in STACK.md.

---

### Phase 3: Measurement Refinement + Doll-House Print

**Rationale:** First and only measurement gate. It refines what already exists; it does not unlock the probe. Scale ADR must be committed before the floor plan model is built (1:25 = 144mm×168mm for a 3.6m×4.2m room, requires large bed or split; 1:50 = 72mm×84mm, recommended for most printers — but verify minimum wall thickness at 1.5mm before committing).

**Delivers:**
- Measured room: walls, outlets, windows, door swing → ESTIMATED values in `params.scad` replaced with real dimensions; `// ESTIMATED` markers removed
- `make renders` regeneration with accurate dims — git diff on PNGs is the visual proof of measurement
- `inventory/manifest.yaml` — equipment manifest for "before" room, zone-tagged, mode-tagged, refreshed from the-bench-old
- `make validate` passing (yamllint + check-jsonschema)
- `model/zones/creator-filming.scad` — camera sightlines with real dims
- `models/floor-plan/floor_plan.scad` — doll-house STL derived from room model (OpenSCAD-native path: `linear_extrude` on `difference()` of room perimeter polygon)
- `stl/floor-plan-print.stl` — F6 render, not F5; verify non-manifold clean in slicer before committing
- 3D print at ADR-002 scale; prototype print first to verify wall thickness ≥ 1.5mm
- `pulses/001-doll-house/` — photo of printed doll-house + brief description = first pulse artifact

**Avoids:** F5/F6 STL confusion (Technical Debt 2); scale failure at print time (Integration Gotcha 6); params.scad as-is snapshot lost when redesign begins (Integration Gotcha 2)

**Pulse artifact:** Physical 3D-printed scale model of the room + committed photo in `pulses/`. This is the most shareable v1 proof-of-work.

**Research flag:** Needs a quick check during planning on printer bed size vs. scale calculation. Use STACK.md's scale math (1:50 = 72mm×84mm for a ~3.6m×4.2m room) as the starting point.

---

### Phase 4: v1 Completion — Full Render Suite + Labels

**Rationale:** Fills out the "before" model with accessories and design-system bridge, closes the v1 loop, and leaves the repo in a state that communicates the full concept to a first-time visitor.

**Delivers:**
- `model/accessories/*.scad` — monitors, lighting rig, camera arm positioned in zones
- `views/focus-zone.scad`, `views/maker-zone.scad`, `views/filming-zone.scad` → committed PNGs
- `design-system/labels/generated/*.svg` — `make labels` from manifest + template (IBM Plex Mono, brand tokens)
- `CHANGELOG.md` v1.0 entry — as-is state documented
- `decisions/ADR-003-*` for any non-obvious v1 choices made during these phases
- `README.md` updated: all five render PNGs inline; full thesis; pulse log link
- v1 milestone tagged in git

**Avoids:** Design tokens siloed to digital layer only (Architectural Anti-Pattern 5); repo coherence gap (a stranger reading README still does not understand the project)

**Pulse artifact:** v1 complete. All five renders committed and inline in README. Equipment manifest. Brand label templates. Physical doll-house print. The probe has a face.

**Research flag:** Standard patterns — skip research phase.

---

### v2 Milestone: Physical Redesign

The physical-dependency checklist from ARCHITECTURE.md governs v2 sequencing. The order is non-negotiable: infra/power/cable before furniture moves; furniture to final positions before storage; storage baseline before custom inserts; HA manual scenes before sensor automation. The organizer phases are sequenced most-visible-first (openGrid wall > Gridfinity desk/drawer > Underware cable > Neogrid large storage) because the wall grid has the highest visual impact and is the fastest proof-of-work in the physical space.

---

### Phase 5: Physical Redesign Foundation

**Rationale:** Infra and furniture must move before any organizer system is deployed. Printing Gridfinity bins before the desk is in its final position is waste. This phase clears the physical dependency checklist items 1–3 and updates the OpenSCAD model with the redesigned layout.

**Delivers:**
- Infra/power/cable installed (outlets, cable runs) before furniture moves
- Furniture to final positions (standing desk, maker bench, shelving)
- `params.scad` updated for new layout; `make renders` regenerates all views
- `CHANGELOG.md` v2.0 entry
- `pulses/002-redesign-foundation/` — before/after photos committed

**Physical-dependency checklist:** items 1–3 (measure already done in Phase 3; install infra/power; move furniture)

**Avoids:** Marination trap — bias to installing and iterating, not observing for weeks (Pitfall 4)

**Research flag:** Needs research phase for power/circuit planning if the maker bench requires an isolated circuit (CBLE-07 from FEATURES.md). Otherwise standard patterns.

---

### Phase 6: Desk + Drawer Organization (Gridfinity)

**Rationale:** Gridfinity is the highest-density visible change to the desk zone and the most relatable build-in-public content. It requires knowing what is being stored (manifest, done in Phase 3) and the final desk position (Phase 5). Lock grid-system-per-zone in an ADR before printing.

**Delivers:**
- `decisions/ADR-004-gridfinity-zone-assignment.md` — lock which system per zone (Gridfinity for desk drawers/surface; openGrid for walls; no mixing per zone)
- Drawer inner usable dimensions measured (not outer; subtract 4–6mm for clearance; IKEA Alex 9-drawer depth 425mm vs 5-drawer 525mm noted)
- `models/organizers/gridfinity/desk-drawer-baseplate.scad` — custom baseplate for actual drawer dimensions
- FIRST: prototype single baseplate, print it, verify fit, commit fit-check photo → THEN batch print
- Full Gridfinity layout for desk daily-use zone and maker bench components zone
- `stl/gridfinity-*.stl` — all from F6 render pipeline, never F5

**Avoids:** Batch print before fit verification (Pitfall 5); grid system mixing (Technical Debt 4)

**Pulse artifact:** Gridfinity drawers installed + photo. Community-recognizable content.

**Research flag:** Standard patterns for kennetek Gridfinity Rebuilt. May need a quick check on QuackWorks Gridfinity integration if using QuackWorks for Gridfinity rather than kennetek directly.

---

### Phase 7: Wall Organization (openGrid)

**Rationale:** openGrid is the highest-visibility physical change (walls visible in filming background and maker bench zone). It is sequenced before Underware because Underware can snap onto openGrid boards — install order matters. Most-visible-first principle.

**Delivers:**
- `decisions/ADR-005-opengrid-zone-assignment.md` — openGrid for maker bench wall + desk wall
- `models/organizers/opengrid/*.scad` — custom tiles for scissors, rulers, tape, soldering accessories
- openGrid boards mounted; accessories snapped on
- `models/zones/maker-bench.scad` updated with openGrid overlay
- Re-render all affected views; commit PNGs

**Avoids:** Printing wrong tiles before zone assignment is locked (grid system ADR); Underware before openGrid (integration sequence error)

**Pulse artifact:** openGrid wall mounted above maker bench + photo. Camera background visibly improved.

**Research flag:** Standard patterns — QuackWorks openGrid source is well-documented.

---

### Phase 8: Cable Management (Underware)

**Rationale:** Underware snaps onto mounted openGrid boards (Phase 7 prerequisite) or runs standalone under the desk surface. It directly improves creator-filming mode (zero cables in frame) and deep-focus mode (no cable clutter). Transparent PETG enables LED strip diffusion as a bonus.

**Delivers:**
- `models/organizers/underware/*.scad` — channel configurations for under-desk and wall cable runs
- Underware channels printed (PLA standard; PETG if LED diffusion wanted) and installed
- All cables routed off the floor and out of camera frame
- `models/zones/creator-filming.scad` updated to reflect clean cable state
- Re-render filming-zone view

**Avoids:** Underware before openGrid (sequence dependency); HA cable config stored in UI rather than git

**Pulse artifact:** Before/after desk-cable-management photos. "Zero cables in frame" = filming-mode demo.

**Research flag:** Standard patterns — QuackWorks Underware source documented. License note: Underware is CC-BY-NC-SA; note in ADR.

---

### Phase 9: Large Storage (Neogrid 2.0)

**Rationale:** Neogrid addresses deep drawers with large items — tools, materials, filament — where Gridfinity bins are too small a unit. Sequenced last in the organizer ecosystem because it requires knowing the final drawer contents after the desk + openGrid + Underware phases have stabilized usage patterns.

**Delivers:**
- `models/organizers/neogrid/*.scad` — connector layouts (X-junction, L, T, I pieces) for actual drawer dimensions
- Connectors printed (FDM); panels cut to size (MDF/plywood/acrylic — not printed)
- Large-item drawers organized
- Manifest updated with relocated items

**Avoids:** Printing Neogrid connectors for wrong drawer dimensions (measure inner usable, subtract clearance)

**Pulse artifact:** Deep drawer organization photo — before/after.

**Research flag:** Standard patterns — QuackWorks Neogrid 2.0 source documented.

---

### Phase 10: Home Automation + HA in Git

**Rationale:** HA config ships after manual usage is proven (lights and plugs physically installed first) to avoid automating an unvalidated baseline. The mandatory wait period (manual scenes before sensor automation) is timeboxed to two weeks maximum, not 2–4 weeks. Parallel work during the wait: any Phase 9 items not yet complete.

**Delivers:**
- `config/home-assistant/` — YAML for all mode scenes committed to repo (never "configured in the UI")
- Focus scene (warm 3000K, minimal distraction), Filming scene (balanced color temp, bias lighting dimmable), Maker scene (bright, high CRI, all equipment plugs on), Ambient scene
- mmWave presence sensor (HA config committed; ESPHome only for sensors unavailable commercially)
- `make validate` updated to lint HA YAML
- One-tap mode switching demonstrated

**Avoids:** HA config only in UI (Technical Debt 6); cascading wait gate — two-week max on manual validation before adding automation (Pitfall 3)

**Pulse artifact:** HA mode-switching demo video or GIF committed to pulses/.

**Research flag:** May need research phase for mmWave sensor ESPHome config specifics.

---

### Phase 11: Creator Filming Mode

**Rationale:** The physical filming setup (three-point lighting, eye-level camera, curated background) is the capstone of the space redesign. It depends on: cable management complete (clean frame), openGrid wall installed (visible background), HA lighting scenes available (one-tap mode switch). This is the phase that produces the first video shot in the redesigned Bench.

**Delivers:**
- Key light (45° placement), fill light, hair/separation light installed
- Eye-level camera on arm (FILM-01)
- Boom-mounted microphone
- Curated background depth layers (near desk surface / mid shelving / far wall)
- OBS scene list committed as data in repo
- Bias lighting behind monitor (dimmable warm, not RGB)
- `models/zones/creator-filming.scad` final — camera sightlines accurate with real installed positions
- First video produced in redesigned space

**Avoids:** Green screen (anti-feature); RGB/gaming aesthetics (anti-feature); resin printer in office (anti-feature — FDM only)

**Pulse artifact:** First piece of content produced in the redesigned Bench. The before→alive arc completes.

**Research flag:** Standard patterns for three-point lighting. OBS scene config is well-documented.

---

### Phase Ordering Rationale

- **Spine before everything:** The public probe's credibility requires a live public README before any physical task. No exception.
- **Estimated dims before measured dims:** `params.scad` with `ESTIMATED` values ships before the tape measure comes out; measurement refines, never gates.
- **Equipment manifest before organizer phases:** You cannot plan a Gridfinity layout without knowing what you're storing. Manifest (Phase 3) is a hard prerequisite for Phases 6–9.
- **openGrid before Underware:** Underware snaps onto openGrid boards; install order is structural.
- **Most-visible organizer first:** openGrid (wall, visible in background) before Gridfinity (desk, partially hidden in drawers) before Underware (under-desk, invisible) before Neogrid (deep drawers). This maximizes visual proof-of-work per phase.
- **HA manual before sensor automation:** Not a 2–4 week gate — a timeboxed two-week maximum. Parallel work must be identified for the wait period.
- **Physical redesign (v2) after "before" is modeled (v1):** v1 model becomes the ground-truth baseline for measuring what changed. Tag the v1 commit before any v2 physical changes.

### Research Flags

**Needs research phase during planning:**
- **Phase 5 (Physical Redesign Foundation):** If the maker bench requires an isolated power circuit (CBLE-07), electrical planning research is warranted before committing to a layout.
- **Phase 10 (Home Automation):** mmWave presence sensor ESPHome config specifics; which sensor models are confirmed compatible with HA in 2026.

**Standard patterns (skip research phase):**
- **Phase 1 (Public Spine):** README writing, ADR format, brand tokens — no research needed.
- **Phase 2 (Parametric Foundation):** OpenSCAD CLI patterns documented in STACK.md + ARCHITECTURE.md; submodule setup is standard git.
- **Phase 3 (Measurement + Doll-House):** Scale math provided in STACK.md; printer bed size vs. scale is a quick calculation.
- **Phase 6 (Gridfinity):** kennetek Gridfinity Rebuilt is well-documented; web generator available for pre-print testing.
- **Phase 7 (openGrid):** QuackWorks openGrid source documented; opengrid.world has specs.
- **Phase 8 (Underware):** QuackWorks Underware source documented; MakerWorld customizer available.
- **Phase 9 (Neogrid):** QuackWorks Neogrid 2.0 documented.
- **Phase 11 (Creator Filming):** Three-point lighting and OBS setup are well-documented domains.

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | OpenSCAD snapshot version verified via official Homebrew formulae. BOSL2 v2.0.745 verified via GitHub releases. Gridfinity Rebuilt v2.0.0 verified. QuackWorks confirmed 99.2% OpenSCAD. doratracyer/floor_plan confirmed GPL-3.0. Version incompatibility between QuackWorks and 2021.01 is documented in QuackWorks README. |
| Features | HIGH | Primary source is PROJECT.md (owner-stated requirements and anti-patterns). Organizer ecosystem features verified via official creator sites (handsonkatie.com). Doll-house pipeline verified via GitHub. |
| Architecture | HIGH | OpenSCAD `include` vs `use` semantics verified via official OpenSCAD User Manual wikibook. Render pipeline patterns verified via Cal Bryant's documented approach. Committed-artifacts rationale is project-specific and grounded in build-in-public principles. |
| Pitfalls | HIGH | Grounded in documented v0 post-mortem (STATE.md shows 4% completion, measurement gate blocker). Technical pitfalls (F5/F6, $fn, Gridfinity print tolerances) verified via official OpenSCAD issues and community Printables models with documented dimension failures. |

**Overall confidence:** HIGH

### Gaps to Address

- **Doll-house print scale:** STACK.md provides the scale math but the ADR must be decided before modeling. Key calculation: minimum 1.5mm FDM wall thickness works back to a minimum scale. For a typical room with 200mm thick walls at 1:50, model wall = 4mm (fine). For 1:25, model wall = 8mm (also fine but larger print). For 1:100, model wall = 2mm (borderline — verify against printer's minimum reliable wall). Resolve in ADR-002 during Phase 1.

- **IKEA Alex exact inner usable dimensions:** Gridfinity baseplate fit depends on accurate inner usable dimensions minus rail clearance. The Printables community has documented that IKEA Alex dimensions vary between manufacturing runs. Plan to measure the actual drawers during Phase 3 / Phase 6, not rely on published specs.

- **QuackWorks license for Underware:** Underware is CC-BY-NC-SA. If any Bench artifacts are sold or used commercially, this requires acknowledgment. Log in an ADR during Phase 8.

- **HA Git sync method:** The ARCHITECTURE.md notes `config/home-assistant/` as the target for committed HA YAML. The sync method (HA Git Exporter add-on vs SSH copy vs manual export) is not resolved. Resolve during Phase 10 research.

- **`$fn` convention across the model:** PITFALLS.md and ARCHITECTURE.md both flag global-high `$fn` as a performance trap. The convention (`$fn=12` in development, `$fn=64` for final F6 renders) should be locked in `params.scad` and ADR-001 during Phase 2, not discovered after the model has 20+ objects.

---

## Sources

### Primary (HIGH confidence)

- `/Users/davidnunez/src/the-bench/.planning/PROJECT.md` — owner-stated scope, constraints, anti-patterns, brand
- `/Users/davidnunez/src/the-bench-old/.planning/STATE.md` — v0 post-mortem; 4% completion; measurement gate blocker
- `/Users/davidnunez/src/the-bench-old/.planning/ROADMAP.md` — v0 cascading wait gates; Phase 10 waterfall
- https://formulae.brew.sh/cask/openscad@snapshot — OpenSCAD snapshot cask v2026.06.12 (official Homebrew)
- https://formulae.brew.sh/cask/openscad — deprecated 2021.01 cask; disable date September 1 2026 (official Homebrew)
- https://github.com/BelfrySCAD/BOSL2/releases — BOSL2 v2.0.745 June 2026 (GitHub releases)
- https://github.com/kennetek/gridfinity-rebuilt-openscad — Gridfinity Rebuilt v2.0.0 September 2025 (GitHub)
- https://github.com/AndyLevesque/QuackWorks — QuackWorks "99.2% OpenSCAD"; dev-release requirement (GitHub)
- https://github.com/doratracyer/floor_plan — doll-house floor plan pipeline, GPL-3.0 (GitHub)
- https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement — `include` vs `use` semantics (official OpenSCAD manual)
- https://files.openscad.org/documentation/manual/Using_OpenSCAD_in_a_command_line_environment.html — OpenSCAD CLI (official)

### Secondary (MEDIUM confidence)

- https://www.handsonkatie.com/home-organisation — Gridfinity/openGrid/Underware/Neogrid ecosystem overview (official creator site)
- https://www.handsonkatie.com/opengrid — openGrid cross-system compatibility (official creator site)
- https://www.handsonkatie.com/underware — Underware 2.0 cable channels, LED diffuser (official creator site)
- https://www.opengrid.world/ — openGrid 28mm grid spec, Gridfinity compatibility (official project site)
- https://calbryant.uk/blog/pushing-openscad-to-the-max-with-discipline-and-imagemagick/ — render pipeline and view-file pattern (community, verified approach)
- https://www.printables.com/model/987829-gridfinity-baseplate-for-ikea-alex-measurements-fi — IKEA Alex dimension variation and misfit problems (community, real-world evidence)
- https://bigrep.com/posts/designing-wall-thickness-for-3d-printing/ — FDM minimum wall thickness 0.8mm supported, 1.2mm reliable, 1.5mm recommended
- https://github.com/openscad/openscad/issues/6301 — F5 vs F6 geometry divergence (official GitHub issue)
- https://makerblock.com/2025/04/openscad-render-times/ — $fn and render() performance impact (community, measured examples)
- https://makerworld.com/en/models/783010-underware-2-0-infinite-cable-management — Underware 2.0 MakerWorld (community platform)
- https://makerworld.com/en/models/1501061-neogrid-2-0-drawer-management-system — Neogrid 2.0 MakerWorld (community platform)
- https://www.maskset.net/blog/2025/05/16/managing-openscad-projects/ — OpenSCAD project structure best practices (community blog, May 2025)

---

*Research completed: 2026-06-27*
*Ready for roadmap: yes*
