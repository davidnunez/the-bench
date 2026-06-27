# Roadmap: The Bench — v1 "Before + Spine"

## Overview

The Bench is a living, version-controlled model of a physical home office/studio — "space as code" — built in public as a Signal Path Probe. The v1 "Before + Spine" milestone inverts the v0 failure mode (stalled at 4% behind a measurement gate): the public spine and first render ship before any tape measure is picked up; measurement is a single non-blocking refinement step in Phase 4; and every phase ends with a pulse-ready proof-of-work artifact committed to the repo. The arc: public presence with brand and ADRs → parametric room shell on estimated dims → first on-brand committed render → real measurement refines the model → three modes annotated + manifest validated → physical doll-house printed and photographed as the v1 capstone.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Public Spine + Design System + ADRs** - Live public repo with thesis, brand tokens, label template SVG, and load-bearing ADRs — zero dependency on OpenSCAD or measuring the room
- [ ] **Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline** - OpenSCAD installed and pinned, `params.scad` with estimated dims, room shell renderable, Makefile pipeline produces committed PNGs
- [ ] **Phase 3: Furniture Primitives + First On-Brand Render** - Furniture and zone modules complete the before-state model; first on-brand committed render ships before measurement
- [ ] **Phase 4: Measurement Refinement + As-Is Layout** - Room measured exactly once; estimated params replaced with real dims; model renders the actual before-state
- [ ] **Phase 5: Three Modes + Equipment Manifest** - Three modes annotated in model per zone; equipment manifest validated as structured data
- [ ] **Phase 6: Doll-House Export + Physical Print** - Room model exported to STL; doll-house 3D-printed and photographed as the v1 milestone capstone pulse

## Phase Details

### Phase 1: Public Spine + Design System + ADRs
**Goal**: The probe is live on GitHub with a complete spine (thesis, brand, identity, LICENSE), design tokens, a label template SVG, and load-bearing ADRs — with zero dependency on physical measurement or OpenSCAD
**Mode:** mvp
**Depends on**: Nothing (first phase)
**Requirements**: SPINE-01, SPINE-03, SPINE-04, CODE-06, DSGN-01, DSGN-03
**Success Criteria** (what must be TRUE):
  1. A stranger landing on the GitHub repo immediately understands the before→alive thesis, the environment-as-provenance philosophy, the over-engineering-as-hook angle, and can follow a back-link to the governing Board Signal
  2. The repo carries an open LICENSE and public-facing metadata appropriate for a build-in-public project
  3. `design-system/tokens.yaml` encodes the full refreshed palette (cream `#f5efe2` / near-black `#1a1820` / terracotta `#ec6a43` / plum `#4a2a57` / magenta `#c63c82`) and type scale (Archivo / Newsreader / IBM Plex Mono)
  4. A printable label template SVG is committed, generated from the design tokens, demonstrating the design-system-to-physical pipeline before any `.scad` file is written
  5. `decisions/ADR-001` (include-vs-use with `$fn` convention) and `decisions/ADR-002` (doll-house print scale 1:25 vs 1:50) are committed, locking load-bearing OpenSCAD choices before a single `.scad` file is written
**Plans**: TBD
**UI hint**: yes

### Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline
**Goal**: OpenSCAD is installed and pinned to the snapshot cask, `params.scad` holds estimated room dimensions as the single source of truth, the room shell is renderable, and the Makefile pipeline produces committed PNGs via the F6/Manifold backend
**Mode:** mvp
**Depends on**: Phase 1
**Requirements**: CODE-01, CODE-02, CODE-03, CODE-05
**Success Criteria** (what must be TRUE):
  1. The setup command (`brew install --cask openscad@snapshot`) is documented and reproduces the exact pinned toolchain in one step; BOSL2 and QuackWorks submodules are pinned and resolvable via `OPENSCADPATH`
  2. `params.scad` is present at root with all dimensions explicitly marked `// ESTIMATED` and all `COLOR_*` constants wired from tokens.yaml; every other `.scad` file begins with `include <params.scad>` (never `use`)
  3. Running `make renders` produces valid top-plan and perspective PNGs of the room shell and commits them without any manual OpenSCAD GUI step
  4. The Makefile enforces F6 (Manifold) as the only render backend for committed artifacts — F5 preview is never used for output committed to the repo
**Plans**: TBD

### Phase 3: Furniture Primitives + First On-Brand Render
**Goal**: Furniture and zone modules bring the before-state model to life; all committed renders apply the brand palette via `COLOR_*` constants; the first on-brand render ships before the room is measured, satisfying the load-bearing inversion over v0
**Mode:** mvp
**Depends on**: Phase 2
**Requirements**: SPINE-02, CODE-04, DSGN-02
**Success Criteria** (what must be TRUE):
  1. The standing desk, Alex units, maker bench, and shelving are modeled as reusable parametric modules in `model/furniture/` and compose correctly into zone files
  2. Zone files assemble shell + furniture; at least two zone view PNGs are committed (top-down floor plan + isometric overview)
  3. All committed renders use `COLOR_*` constants from `params.scad` — the brand palette is visible in rendered output without any manual color override
  4. A stranger visiting the GitHub repo sees committed renders inline in README without taking any rendering step — the repo is visually alive before the room is measured
**Plans**: TBD

### Phase 4: Measurement Refinement + As-Is Layout
**Goal**: The room is physically measured exactly once; all `// ESTIMATED` markers in `params.scad` are replaced with real dimensions; the model renders the actual before-state with accurate geometry and furniture positions
**Mode:** mvp
**Depends on**: Phase 3
**Requirements**: BFOR-01, BFOR-02
**Success Criteria** (what must be TRUE):
  1. Every `// ESTIMATED` marker in `params.scad` has been replaced with a real measured value — no estimated dimension remains in the file
  2. Running `make renders` after measurement regenerates all PNGs; the git diff on render files is the observable visual proof that real measurements changed the model
  3. The room is modeled as-is: walls, door swing, window placement, and current furniture positions match the actual measured room
**Plans**: TBD

### Phase 5: Three Modes + Equipment Manifest
**Goal**: The three modes (deep-focus, creator-filming, electronics-maker) are annotated in the model per zone, and the equipment manifest captures all current items as validated, zone-tagged, mode-tagged structured data
**Mode:** mvp
**Depends on**: Phase 4
**Requirements**: BFOR-03, BFOR-04
**Success Criteria** (what must be TRUE):
  1. Each zone in the model carries a mode annotation — a human reading the `.scad` files can identify which mode(s) each zone serves without consulting external documentation
  2. Zone-specific renders (focus-desk, creator-filming, maker-bench) are committed as PNGs that make the mode differences between zones visible
  3. `inventory/manifest.yaml` lists all current equipment with zone and mode tags and passes `make validate` (yamllint + check-jsonschema) with zero errors
**Plans**: TBD

### Phase 6: Doll-House Export + Physical Print
**Goal**: The room model is exported to a printable STL via the OpenSCAD-native path, deriving directly from `params.scad`; the doll-house is 3D-printed at the scale locked in ADR-002; the physical object is photographed and committed as the v1 milestone capstone pulse
**Mode:** mvp
**Depends on**: Phase 5
**Requirements**: DOLL-01, DOLL-02
**Success Criteria** (what must be TRUE):
  1. `floor-plan.scad` derives the doll-house STL directly from `params.scad` via `linear_extrude` + `difference()` — one source of truth shared with the parametric room model, not a separate file
  2. The committed STL passes a non-manifold check in a slicer before printing — F6 (Manifold) is the enforced export path; F5 is never used for any committed STL
  3. The physical doll-house is 3D-printed at the scale locked in ADR-002, photographed with authentic WIP photography (no AI imagery), and the photo is committed under `pulses/001-doll-house/`
  4. A `v1` git tag is applied after the print photo commits — the milestone boundary is traceable in the repo history
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Public Spine + Design System + ADRs | 0/TBD | Not started | - |
| 2. Parametric Foundation — Toolchain + Room Shell + Pipeline | 0/TBD | Not started | - |
| 3. Furniture Primitives + First On-Brand Render | 0/TBD | Not started | - |
| 4. Measurement Refinement + As-Is Layout | 0/TBD | Not started | - |
| 5. Three Modes + Equipment Manifest | 0/TBD | Not started | - |
| 6. Doll-House Export + Physical Print | 0/TBD | Not started | - |
