# Requirements: The Bench

**Defined:** 2026-06-27
**Core Value:** A stranger encountering the public repo sees a real human turning his environment into a reproducible, expressive, lovingly over-engineered system — and wants to follow along.

> **Milestone scope (v1 = "Before + Spine").** v1 stands up the public spine, models the room **as-is**, and ships the doll-house print + first pulse. The actual physical redesign and the organizer-ecosystem install are **v2+** (tracked below, not in this roadmap). Guiding inversion: the public/meta spine leads and **never waits on room measurement**; silence is the only failure mode; ship-on-a-beat over marination.

## User Stories

- **As a stranger on the internet**, I want to land on the repo and immediately get what this is and why it's interesting (before→alive; environment-as-provenance; the over-engineering IS the art), so that I want to follow along.
- **As the builder (David)**, I want the public spine + first render to ship *before* I measure the room, so that the project can't stall behind a measurement gate like v0 did.
- **As the builder**, I want every phase to end with a committed, shareable proof-of-work artifact, so that I always have something to pulse on a weekly beat without a publishing pipeline.
- **As the builder**, I want the room modeled as-is in parametric code with the three modes annotated, so that the "before" state is captured as a reproducible artifact.
- **As a maker audience**, I want a physical doll-house print of the floor plan, so that "space as code" becomes a holdable object I can see and share.

## v1 Requirements

Requirements for the initial release (the "Before + Spine" milestone). Each maps to a roadmap phase.

### Spine (Public Artifact)

- [ ] **SPINE-01**: Public README frames the probe — the before→alive thesis, environment-as-provenance, "over-engineering is the hook," the identity one-liner, and a back-link to the governing Board Signal
- [ ] **SPINE-02**: The repo ships its first public proof-of-work (a committed render) **before** the room is measured
- [ ] **SPINE-03**: A pulse-ready proof-of-work artifact is produced and logged in-repo at the end of every phase (broadcasting itself stays out of repo)
- [ ] **SPINE-04**: Repo carries an appropriate open LICENSE and public-facing metadata for a build-in-public project

### Design System

- [ ] **DSGN-01**: In-repo design tokens encode the refreshed palette (cream `#f5efe2` / near-black `#1a1820` / terracotta `#ec6a43` / plum `#4a2a57` / magenta `#c63c82`) and type (Archivo / Newsreader / IBM Plex Mono)
- [ ] **DSGN-02**: Renders apply the brand palette so even early/boring renders are on-brand and shareable
- [ ] **DSGN-03**: Brand tokens drive printable physical signage / bin-label templates (SVG) from the same source of truth

### Space-as-Code Foundation

- [ ] **CODE-01**: OpenSCAD toolchain installed and pinned — `openscad@snapshot` + BOSL2 + the QuackWorks submodule — reproducible via a documented one-command setup
- [ ] **CODE-02**: `params.scad` is the single source of truth for room dimensions, seeded with **estimated** values that do not block the build (`include`, never `use`)
- [ ] **CODE-03**: Parametric room shell (walls, door, window, outlets) is modeled from `params.scad`
- [ ] **CODE-04**: Furniture & zone primitives (standing desk, Alex units, maker bench, shelving) are modeled as reusable modules
- [ ] **CODE-05**: A one-command render pipeline (Makefile) produces committed top-down floor-plan + perspective PNGs via the F6 (Manifold) backend
- [ ] **CODE-06**: Architecture Decision Records lock the load-bearing early choices — `include`-vs-`use`, and the doll-house print scale (e.g. 1:25 vs 1:50)

### Before-State Model

- [ ] **BFOR-01**: The room is measured and the estimated `params.scad` values are replaced with real measurements (the single, non-blocking measurement refinement)
- [ ] **BFOR-02**: The room is modeled **as-is** with the current furniture layout
- [ ] **BFOR-03**: The three modes (deep-focus / creator-filming / electronics-maker) are annotated in the model per zone
- [ ] **BFOR-04**: An equipment/inventory manifest (YAML) captures current items as structured data, validated (yamllint + schema)

### Doll-House Artifact

- [ ] **DOLL-01**: A scale doll-house floor plan is exported to a printable STL from the room model (F6, validated geometry, scale locked by ADR)
- [ ] **DOLL-02**: The doll-house is physically 3D-printed and photographed (authentic WIP, no AI imagery) as the v1 milestone pulse

## v2 Requirements

Deferred to future milestones (the actual physical redesign + organizer ecosystem). Tracked, not in the current roadmap. The harvested **physical-dependency checklist** applies here: measure → infra/power/cable → furniture → storage baseline → organization → HA manual-before-sensors. Discipline: each ships on a beat; **no long "live-in-it" marination gates.**

### Physical Foundation

- **PHYS-01**: Power, lighting fixtures, and cable routing installed in final positions before furniture moves
- **PHYS-02**: Furniture moved to final positions; ergonomics configured
- **PHYS-03**: Storage baseline — every item has a defined, labeled home (clutter eliminated)

### Organization Ecosystem (Gridfinity / openGrid / Underware / Neogrid)

- **ORG-01**: Grid-system-per-zone locked in an ADR (avoid mixing incompatible 42mm/28mm systems)
- **ORG-02**: Gridfinity baseplates + bins for desk surface and drawers (prototype-one-before-batch)
- **ORG-03**: openGrid wall panel above the maker bench (most-visible change; precedes Underware)
- **ORG-04**: Underware under-desk cable management snapping onto openGrid (zero cables in filming frame)
- **ORG-05**: Neogrid for large/deep-drawer storage

### Lighting, AV & Automation

- **AUTO-01**: Lighting scenes for the three modes, switchable by one tap
- **AUTO-02**: Home Assistant config committed to the repo (YAML, never UI-only)
- **AUTO-03**: Presence/automation added only after manual scenes prove stable (short validation, not weeks of marination)

### Creator / Filming Mode

- **FILM-01**: Filming rig operational (camera, mic, lighting, OBS scenes); on-camera environment reads intentional for YouTube and Zoom
- **FILM-02**: First video produced *in* the redesigned space (capstone pulse)

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Broadcasting / publishing the pulses (newsletter, YouTube ops, social posting) | The repo *emits* pulse-ready artifacts; broadcasting is the A4/A5 job outside this repo |
| Rendering the model into davidnunez.com / the Ghost site | Public surface is the GitHub repo; not required for the probe |
| Full Signal-Path machinery in-repo | Carry only identity + brand + a back-link to the Board |
| Re-deriving strategy / identity / priorities | Those live in the Board (system of record) |
| AI-generated imagery | Brand requires authentic WIP photography only |
| RGB / gaming aesthetics, chrome, glossy plastic | Off-brand (workshop-warm, real materials, restraint) |
| Long "live-in-it-for-weeks" marination gates before optimizing | Explicit anti-pattern; bias to rapid proof-of-work |
| Full-home renovation · structural changes (walls/plumbing/panel) · hiring a designer | Out of bounds; the hands-on process is the point |
| Audio / music production | Not part of this probe |
| Carrying the old 10-phase waterfall / GSD state / `params.scad` stub | Start fresh; harvest documents only |

## Definition of Done (v1)

v1 is shippable when:
1. The public repo is live with the README spine and an open LICENSE — and it shipped **before** the room was measured.
2. A committed render exists on GitHub (on-brand, generated by the Makefile pipeline) — the artifact is visible without any publishing step.
3. The room is modeled as-is from real measurements, three modes annotated, manifest validated.
4. The doll-house floor plan is printed, photographed, and posted as the v1 milestone pulse.
5. Every phase left behind a logged, pulse-ready proof-of-work artifact (cadence held; no silent phase).

## Traceability

Which phases cover which requirements. Updated after roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| SPINE-01 | Phase 1: Public Spine + Design System + ADRs | Pending |
| SPINE-02 | Phase 3: Furniture Primitives + First On-Brand Render | Pending |
| SPINE-03 | Phase 1: Public Spine + Design System + ADRs | Pending |
| SPINE-04 | Phase 1: Public Spine + Design System + ADRs | Pending |
| DSGN-01 | Phase 1: Public Spine + Design System + ADRs | Pending |
| DSGN-02 | Phase 3: Furniture Primitives + First On-Brand Render | Pending |
| DSGN-03 | Phase 1: Public Spine + Design System + ADRs | Pending |
| CODE-01 | Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline | Pending |
| CODE-02 | Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline | Pending |
| CODE-03 | Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline | Pending |
| CODE-04 | Phase 3: Furniture Primitives + First On-Brand Render | Pending |
| CODE-05 | Phase 2: Parametric Foundation — Toolchain + Room Shell + Pipeline | Pending |
| CODE-06 | Phase 1: Public Spine + Design System + ADRs | Pending |
| BFOR-01 | Phase 4: Measurement Refinement + As-Is Layout | Pending |
| BFOR-02 | Phase 4: Measurement Refinement + As-Is Layout | Pending |
| BFOR-03 | Phase 5: Three Modes + Equipment Manifest | Pending |
| BFOR-04 | Phase 5: Three Modes + Equipment Manifest | Pending |
| DOLL-01 | Phase 6: Doll-House Export + Physical Print | Pending |
| DOLL-02 | Phase 6: Doll-House Export + Physical Print | Pending |

**Coverage:**
- v1 requirements: 19 total
- Mapped to phases: 19 ✓
- Unmapped: 0 ✓

---
*Requirements defined: 2026-06-27*
*Last updated: 2026-06-27 — traceability populated after roadmap creation*
