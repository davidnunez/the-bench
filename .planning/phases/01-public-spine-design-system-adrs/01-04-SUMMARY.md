---
phase: 01-public-spine-design-system-adrs
plan: 04
subsystem: docs
tags: [github, build-in-public, pulses, metadata, make, validation]

requires:
  - phase: 01-public-spine-design-system-adrs/01-03
    provides: four ADRs (ADR-001..004) committed and ready to reference in pulse

provides:
  - Live public GitHub repo (https://github.com/davidnunez/the-bench) with build-in-public metadata
  - PULSES.md at repo root: Pulse 001 entry for Phase-1 public-spine pulse (D-22)
  - Phase-1 phase gate green: make validate && make labels both exit 0
affects:
  - Phase 2 (can now link to live repo; PULSES.md establishes pulse-logging pattern)
  - All future phases (repo is now public; everything committed is publicly visible)

tech-stack:
  added: []
  patterns:
    - "PULSES.md at repo root: one entry per phase pulse; entry references artifacts by relative path"
    - "gh repo create --public --source=. --remote=origin --push for initial publish"
    - "gh repo edit for description, homepage, topics (all metadata set via CLI, no GUI)"

key-files:
  created:
    - PULSES.md
  modified:
    - scripts/generate-labels.py
    - scripts/test_generate_labels.py
    - design-system/labels/the-bench-labels.svg
    - Makefile

key-decisions:
  - "Repo published public on GitHub as davidnunez/the-bench (authorized by user at orchestrator checkpoint)"
  - "GitHub About: description, davidnunez.com homepage, 8 topics set via gh CLI"
  - "PULSES.md at repo root (not pulses/ subdirectory): flat, one entry per phase, discoverable"
  - "Phase-1 pulse = the live public repo itself (D-22): spine + tokens + SVG + 4 ADRs"
  - "Task 3 (human-verify) left PENDING — checkpoint payload returned to orchestrator; not self-approved"

patterns-established:
  - "Pulse logging: PULSES.md entry per phase; references artifacts by relative path; note that broadcasting is out-of-repo"
  - "Phase gate: make validate && make labels before marking any phase complete"

requirements-completed: [SPINE-01, SPINE-03, SPINE-04]

duration: 2min
completed: 2026-06-27
---

# Phase 1 Plan 4: Publish Repo Public + PULSES.md Summary

**Live public repo at github.com/davidnunez/the-bench with build-in-public metadata; Phase-1 pulse logged in PULSES.md; phase gate green — human verification PENDING**

## Performance

- **Duration:** ~2 min (Tasks 1-2 only; Task 3 is checkpoint:human-verify, not self-approved)
- **Started:** 2026-06-27T17:46:29Z
- **Completed (tasks 1-2):** 2026-06-27T17:48:27Z
- **Tasks:** 2 of 3 completed (Task 3 is human-verify checkpoint — PENDING)
- **Files modified:** 1 (PULSES.md created)

## Accomplishments

- Published the repo as https://github.com/davidnunez/the-bench — public, with the full Wave-1 commit history
- Set GitHub About metadata: description ("Physical home office/studio modeled as version-controlled code. Space as code — built in public."), homepage (https://davidnunez.com), 8 topics (openscad, 3d-printing, gridfinity, space-as-code, build-in-public, home-office, parametric-design, design-system)
- Created PULSES.md at repo root with Pulse 001 entry documenting the Phase-1 probe pulse (D-22): README spine + tokens + SVG + 4 ADRs
- Phase gate `make validate && make labels` both exit 0 (green)

## Task Commits

1. **Task 1: Publish repo public + set metadata** — `538a937` (push via `gh repo create --public`; metadata set via `gh repo edit`; no new in-repo file)
2. **Task 2: PULSES.md + phase gate** — `dee8b19` (docs: PULSES.md with Pulse 001 entry)
3. **Task 3: Human verify live repo** — PENDING (checkpoint:human-verify, blocking gate; not self-approved)

**Post-checkpoint fixes:**
- `d58d98b` (fix: XML-escape SVG text + fail build on malformed SVG — see Deviations below)
- `1f821ba` (fix: wrap swatch descriptions to card width + overflow guard — see Deviations below)

## Files Created/Modified

- `PULSES.md` — In-repo pulse log; Pulse 001 entry for Phase-1 public-spine pulse; references README, tokens.yaml, the-bench-labels.svg, ADR-001..004

## Decisions Made

- GitHub About metadata set via `gh repo edit` CLI (no GUI needed, fully scripted)
- PULSES.md at repo root (flat file, not a subdirectory) per RESEARCH Open Questions resolution
- Phase-1 pulse IS the live repo itself (D-22): not a separate publish artifact

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Generated SVG was not well-formed XML (bare `&` broke browser parsing)**
- **Found during:** Task 3 human-verify (surfaced by the human reviewer opening the SVG in a browser)
- **Issue:** The label generator emitted the Google Fonts `@import url(...)` with bare `&` characters separating the `family=` params. SVG is XML, so a bare `&` is an illegal entity reference — the browser failed with `EntityRef: expecting ';'` at line 7, and the SVG would not render. The phase gate never checked the generated SVG was well-formed XML, so the regression went undetected.
- **Fix:**
  - Added a general `xesc()` XML-escape helper (`xml.sax.saxutils.escape`) applied to all emitted text/attribute content, so the font URL's `&` (and any future `&`/`<`/`>` in token values) escapes to `&amp;` etc. The XML parser unescapes `&amp;`→`&` before the CSS URL is used, so fonts still load.
  - Added a regression guard: the generator parses the written SVG back with `xml.dom.minidom` and hard-fails (non-zero exit) if it is not well-formed. Surfaced the same check in the `make labels` target.
  - Added tests T9 (well-formed XML) + T10 (no bare `&` in `@import`) to lock it in.
- **Files modified:** scripts/generate-labels.py, scripts/test_generate_labels.py, design-system/labels/the-bench-labels.svg (regenerated), Makefile
- **Verification:** `make validate && make labels` green; SVG parses via both `xml.dom.minidom` and `xml.etree.ElementTree`; line 7 now shows `&amp;`; 14/14 tests pass; guard confirmed to hard-fail on a deliberately malformed SVG.
- **Committed in:** `d58d98b`

**2. [Rule 1 - Bug] Swatch description text overflowed the card and clipped**
- **Found during:** Task 3 human-verify (second visual defect surfaced by the reviewer)
- **Issue:** Each swatch `meaning` was emitted as a single non-wrapping `<text>` line with no fit-to-width. Longer meanings ran past the card's right edge and clipped — visible on probe ("...where the dep[th]"), broadcast ("...(persimm[on])"), and schematic ("...composing compo[nent]"). At IBM Plex Mono 10px the monospace advance is 0.6em = 6px/char, so the ~198px inner width holds ~33 chars; probe (44), broadcast (42), schematic (40), signal (35), and pulse (34) all exceeded it.
- **Fix:**
  - Word-wrap each meaning to the card inner width. `chars_per_line` is **derived** from the monospace metric (`inner_width / (0.6 * font_size)` = 198/6 = 33), not a hardcoded number. Wrapped lines emit as `<tspan x="10" dy="...">` children of the meaning `<text>`; breaks are word-boundary only (longest word "built-to-travel"=15 fits).
  - Bumped `SWATCH_H` 58→64 so two 10px lines clear the bottom edge; `SVG_H` is now computed from the actual row count (canvas 480×428) so it always fits. 2-column grid, colors, and spacing otherwise unchanged.
  - Added structural overflow guard `assert_swatch_fits()` (mirrors the XML guard): hard-fails the build if any line exceeds the inner width or the block exceeds card height. Added test **T11** enforcing the same on both axes.
- **Files modified:** scripts/generate-labels.py, scripts/test_generate_labels.py, design-system/labels/the-bench-labels.svg (regenerated)
- **Verification:** All 8 meanings now wrap within 33 chars / ≤2 lines (probe→["hands-on exploration — where the","depth lives"], broadcast→["durable, built-to-travel share","(persimmon)"], schematic→["speculative outline composing","components"]); `make validate && make labels` green; XML guard still passes; 15/15 tests pass; overflow guard confirmed to trip on an over-wide line (240px > 198px).
- **Committed in:** `1f821ba`

---

**Total deviations:** 2 auto-fixed (2 Rule 1 bugs, both caught at the human-verify gate)
**Impact on plan:** Both fixes were required for correctness — the label SVG is a core Phase-1 deliverable and must render legibly. Each fix also closed a validation hole (malformed XML and text overflow are now hard build failures with regression tests), so neither can silently regress. No scope creep. Task 3 remains PENDING for re-verification.

## Checkpoint: Task 3 PENDING

**Type:** checkpoint:human-verify (gate="blocking")
**What to verify:**

1. Open https://github.com/davidnunez/the-bench — confirm About panel shows description, 8 topics, davidnunez.com link
2. Read README.md on GitHub — confirm before→alive thesis, Board back-link, David's voice (not guru-fluff)
3. Open `design-system/labels/the-bench-labels.svg` in browser — confirm wordmark (aubergine on cream) + 8 ink-legend swatches with meanings (SVG now parses as valid XML — bare-`&` fixed in `d58d98b`; descriptions now wrap inside the cards with no clipping — fixed in `1f821ba`)
4. Confirm `decisions/` lists ADR-001..004 and PULSES.md has Pulse 001 entry

**Resume signal:** Type "approved" or describe what to fix.

## Issues Encountered

None.

## Threat Surface Scan

No new security surface introduced. The repo publish (T-01-04-I) was mitigated: all tracked files verified to contain only intended-public artifacts before `gh repo create --public`.

## Known Stubs

None — PULSES.md is complete; Pulse 001 references live artifacts.

## Next Phase Readiness

- Repo is live and public; Phase 2 can link to it
- PULSES.md establishes the pulse-logging pattern for all future phases
- Phase gate (make validate && make labels) is green
- Blocked on: human approval of Task 3 (checkpoint:human-verify)

## Self-Check

- [x] PULSES.md created at /Users/davidnunez/src/the-bench/PULSES.md
- [x] Commit dee8b19 exists in git log (Task 2)
- [x] Commit d58d98b exists in git log (SVG XML-escape fix)
- [x] Commit 1f821ba exists in git log (swatch description wrap fix)
- [x] Repo is public at https://github.com/davidnunez/the-bench
- [x] make validate && make labels both green
- [x] SVG parses as well-formed XML (xml.dom.minidom + ElementTree)
- [x] No swatch description overflows its card (T11 + generator guard)

## Self-Check: PASSED

---
*Phase: 01-public-spine-design-system-adrs*
*Plan 04 tasks 1-2 complete; Task 3 (human-verify) pending*
*Completed: 2026-06-27*
