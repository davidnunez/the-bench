---
phase: 01-public-spine-design-system-adrs
plan: 3
subsystem: docs
tags: [openscad, adr, architecture, decisions, dollhouse, design-system, color-semantics]

# Dependency graph
requires: []
provides:
  - "Four load-bearing ADRs in decisions/ before any .scad file"
  - "ADR-001: include <params.scad> for variables, use <...> for modules, $fn~12 dev convention"
  - "ADR-002: doll-house print scale locked at 1:25 (Bambu Lab A1 256mm bed fits ~144x168mm footprint)"
  - "ADR-003: floor-base + swappable-wall architecture; directs shell.scad to composable wall modules; joint mechanism deferred to Phase 6"
  - "ADR-004: semantic color integrity (reflect-don't-invent) + Board boundary; tokens.yaml as pinned snapshot"
affects:
  - 02-openscad-room-shell
  - phase-2-shell-scad
  - phase-6-dollhouse-print
  - all phases using openscad

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Nygard five-section ADR format (Context / Decision / Consequences)"
    - "decisions/ directory for architecture decision records"
    - "include <params.scad> for variables, use <...> for modules"
    - "$fn=12 during development, $fn=64 for committed renders/STL exports"
    - "1:25 doll-house print scale with SCALE=1/25 in params.scad"
    - "floor-base + swappable-wall composable module architecture"
    - "Reflect-don't-invent color rule; TBD markers for Board gaps"

key-files:
  created:
    - decisions/ADR-001-openscad-include-vs-use.md
    - decisions/ADR-002-dollhouse-print-scale.md
    - decisions/ADR-003-modular-dollhouse-walls.md
    - decisions/ADR-004-semantic-color-integrity.md
  modified: []

key-decisions:
  - "include <params.scad> for variables (use silently produces undef); use <...> for modules only"
  - "Doll-house print scale = 1:25; full room footprint ~144x168mm fits Bambu A1 256mm bed"
  - "Doll-house decomposes into floor base + swappable wall panels; shell.scad must be composable from Phase 2"
  - "Joint mechanism (dovetail vs. other) explicitly deferred to Phase 6"
  - "Brand inks carry Signal Path type meaning always — never decorative reuse"
  - "The Bench repo reflects Board color semantics, never invents them; gaps = TBD markers"
  - "tokens.yaml is a pinned snapshot; re-syncs manually in v1 when Board changes"

patterns-established:
  - "ADR format: Nygard five-section (Status / Context / Decision / Consequences)"
  - "OpenSCAD include convention: include for data files, use for module files"
  - "All phase-2+ .scad files must begin with include <../../params.scad>"
  - "Composable wall module stub pattern: connector_female=true parameter placeholder in Phase 2"
  - "Color integrity rule: type ink = type meaning, always; no decorative reuse"

requirements-completed: [CODE-06]

# Metrics
duration: 3min
completed: 2026-06-27
---

# Phase 1 Plan 3: ADRs Summary

**Four load-bearing architecture ADRs in Nygard format — include/use convention, 1:25 print scale, composable wall modules, and semantic color integrity — committed before any .scad file exists**

## Performance

- **Duration:** 3 min
- **Started:** 2026-06-27T17:36:44Z
- **Completed:** 2026-06-27T17:39:49Z
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments

- ADR-001 locks the OpenSCAD `include` vs `use` convention: `include <params.scad>` for variables (using `use` causes silent `undef` — the failure mode is explicitly named); `use <...>` for furniture/module files; `$fn~12` during development, raised only for committed renders/STL exports
- ADR-002 locks doll-house print scale at 1:25 — the Phase 1 success criterion; a 3.6×4.2m room prints as ~144×168mm, fitting the Bambu Lab A1's 256×256mm bed; walls are ~6mm at this scale, thick enough for printed joinery
- ADR-003 locks floor-base + swappable-wall architecture and directs Phase 2 to build `shell.scad` as composable wall modules from the start; the joint mechanism (dovetail vs. other) is explicitly deferred to Phase 6
- ADR-004 locks semantic color integrity: brand inks carry Signal Path type meaning without exception; the Bench reflects the Board's color semantics, never invents them; `tokens.yaml` is a pinned snapshot; gaps use `"TBD — pending Board decision"` markers

## Task Commits

Each task was committed atomically:

1. **Task 1: Write ADR-001 (include vs use + $fn) and ADR-002 (1:25 scale)** - `a6e9cdb` (docs)
2. **Task 2: Write ADR-003 (modular walls) and ADR-004 (semantic color integrity)** - `63ff0f7` (docs)

## Files Created/Modified

- `decisions/ADR-001-openscad-include-vs-use.md` — locks include/use convention and $fn; names the silent undef failure mode
- `decisions/ADR-002-dollhouse-print-scale.md` — locks 1:25 scale; Bambu A1 bed fit analysis; joint feature-size verification deferred to Phase 6
- `decisions/ADR-003-modular-dollhouse-walls.md` — floor-base + swappable-walls architecture; composable wall modules from Phase 2; joint mechanism deferred to Phase 6
- `decisions/ADR-004-semantic-color-integrity.md` — reflect-don't-invent rule; Board boundary; tokens.yaml as pinned snapshot; TBD markers for gaps

## Decisions Made

- **include vs use:** `include <params.scad>` is the only safe choice for a variable-sharing file. `use` silently produces `undef` for all variables — no error, just wrong geometry. This is a correctness requirement, not a style choice.
- **1:25 scale locked as Phase 1 success criterion:** The full room footprint at 1:25 fits the A1 bed with margin. Walls are 6mm — above FDM minimums and thick enough for joinery. Scale constant flows into `params.scad` as `SCALE = 1/25`.
- **Composable architecture deferred but not the decision itself:** The joint mechanism is Phase 6's job, but the architectural decision (floor-base + swappable walls) is Phase 1's, so Phase 2 does not accidentally build a monolithic shell that must be refactored.
- **TBD markers over invented values:** Any color gap in `tokens.yaml` must be explicitly marked `"TBD — pending Board decision"`, never filled with an invented hex. This is the Board boundary made concrete.

## Deviations from Plan

None — plan executed exactly as written. All four ADRs follow the locked decisions from D-18 through D-21 in CONTEXT.md without deviation.

## Issues Encountered

None. The `decisions/` directory did not exist yet and was created as part of task execution (expected — no prior plans created it). All four ADRs passed their automated verification checks on first write.

## Known Stubs

None — these are pure documentation files. No code stubs, no placeholder data.

## Threat Flags

None — this plan produces four static Markdown files. No runtime, no network, no auth, no user input surface.

## Next Phase Readiness

- CODE-06 satisfied: four load-bearing ADRs are committed under `decisions/` before any `.scad` file exists
- Phase 2 (`shell.scad`) is now constrained by ADR-001 (include/use) and ADR-003 (composable wall modules from the start)
- Phase 6 (doll-house print) has the explicit joint-mechanism decision scope it needs: `ADR-003.md#Consequences` states "Joint mechanism deferred to Phase 6"
- `tokens.yaml` is governed by ADR-004's reflect-don't-invent rule — any future color addition routes back to the Board

## Self-Check: PASSED

All four ADR files exist and passed Nygard-format verification:
- `decisions/ADR-001-openscad-include-vs-use.md` — contains `include`, `undef`, `$fn`, all three section headers
- `decisions/ADR-002-dollhouse-print-scale.md` — contains `1:25`, `A1`/`256`, all three section headers
- `decisions/ADR-003-modular-dollhouse-walls.md` — contains `swappable`/`composable`, `Phase 6`, all three section headers
- `decisions/ADR-004-semantic-color-integrity.md` — contains `Board`, `reflect`, `pinned snapshot`, all three section headers

Both task commits exist in git history:
- `a6e9cdb` — Task 1 (ADR-001 + ADR-002)
- `63ff0f7` — Task 2 (ADR-003 + ADR-004)

No `.scad` files exist in the repo — CODE-06 requirement satisfied.

---
*Phase: 01-public-spine-design-system-adrs*
*Completed: 2026-06-27*
