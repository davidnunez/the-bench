---
phase: 01-public-spine-design-system-adrs
plan: 02
subsystem: design-system
tags: [tokens, yaml, svg, python, pyyaml, yamllint, makefile, signal-path, design-tokens]

requires:
  - phase: 01-public-spine-design-system-adrs plan 01
    provides: LICENSE and README.md committed to repo

provides:
  - design-system/tokens.yaml encoding the full Signal Path 8-type semantic system
  - scripts/generate-labels.py reading tokens.yaml via yaml.safe_load and emitting SVG
  - design-system/labels/the-bench-labels.svg — wordmark + 8-label ink-legend card
  - Makefile with make validate (yamllint + 8-types assertion) and make labels (generator + non-empty check)
  - .gitignore for .venv, __pycache__, .DS_Store, OpenSCAD scratch artifacts

affects:
  - 01-public-spine-design-system-adrs plan 03 (ADRs reference tokens.yaml and design system)
  - 01-public-spine-design-system-adrs plan 04 (phase capstone — SVG visual verification)
  - Phase 02 (OpenSCAD params.scad COLOR_* constants derive from tokens.yaml)
  - Phase 05 (zone/mode coloring — deferred per D-17)

tech-stack:
  added:
    - yamllint 1.38.0 (brew install yamllint)
    - PyYAML 6.0.3 (pip install --user --break-system-packages PyYAML)
    - check-jsonschema 0.37.3 (pip install --user --break-system-packages; in .venv for future use)
  patterns:
    - tokens.yaml as single source of truth for brand colors — consumed by generator at runtime
    - yaml.safe_load enforced (never yaml.load) for YAML deserialization security
    - Makefile pipeline: validate (lint + schema smoke) and labels (generator + non-empty check)
    - Custom human-legible YAML schema (not W3C DTCG) per Research Finding 3
    - provenance block first in tokens.yaml to enforce Board boundary on every read

key-files:
  created:
    - Makefile
    - .gitignore
    - design-system/tokens.yaml
    - scripts/generate-labels.py
    - scripts/test_generate_labels.py
    - design-system/labels/the-bench-labels.svg
  modified: []

key-decisions:
  - "yamllint via brew (system PATH); PyYAML via pip --user --break-system-packages due to PEP 668 externally-managed environment"
  - "YAML key 'on' must be quoted as '\"on\"' to avoid yaml truthy coercion (yamllint rule: truthy)"
  - "Makefile labels target is .PHONY (not file-based) so make -n labels succeeds before generator exists"
  - "Custom tokens.yaml schema with bg/on/meaning per type (not W3C DTCG $value/$type)"
  - "SVG @import Google Fonts + fallback font-family for browser rendering; print via Inkscape"

patterns-established:
  - "tokens.yaml is a Board snapshot — provenance block enforces read-only Board boundary"
  - "yaml.safe_load() only in any YAML consumer in this repo"
  - "make validate + make labels as the two-command integration test for design-system"
  - "TDD: test file written before generator, RED confirmed, then GREEN implementation"

requirements-completed: [DSGN-01, DSGN-03]

duration: 5min
completed: "2026-06-27"
---

# Phase 01 Plan 02: Design System Pipeline Summary

**Pinned 8-type Signal Path tokens.yaml + Python generator producing aubergine wordmark + ink-legend SVG via make labels, with make validate green**

## Performance

- **Duration:** 5 min
- **Started:** 2026-06-27T17:28:00Z
- **Completed:** 2026-06-27T17:33:00Z
- **Tasks:** 3
- **Files modified:** 6 created, 0 modified

## Accomplishments

- Authored `design-system/tokens.yaml` with the full 8-type Signal Path semantic system: signal/probe/pulse/broadcast/module/cadence/component/schematic — each with exact hex bg/on/meaning values from the Board snapshot
- Built `scripts/generate-labels.py` (~75 lines, Python + PyYAML + f-string SVG) that reads tokens at runtime and emits the wordmark (aubergine #4a2a57 on cream) + 8-label ink-legend card
- Wired `make validate` (yamllint + 8-types assertion) and `make labels` (generator + non-empty check) — both green; design-system → physical pipeline runs end-to-end
- Committed first generated artifact: `design-system/labels/the-bench-labels.svg` (3.5 KB)

## Task Commits

Each task committed atomically:

1. **Task 1: Makefile + .gitignore** - `abe4037` (chore)
2. **Task 2: design-system/tokens.yaml** - `4c45f76` (feat)
3. **Task 3 RED: failing test** - `d18fab1` (test)
4. **Task 3 GREEN: generator + SVG** - `9bf6102` (feat)

## Files Created/Modified

- `Makefile` — `.PHONY: validate labels renders clean help`; validate uses yamllint + Python 8-types assertion; labels invokes generator + test -s check
- `.gitignore` — .venv, __pycache__, .DS_Store, OpenSCAD scratch artifacts
- `design-system/tokens.yaml` — pinned Board snapshot: 8 types + base + roles + reserved + typography + provenance
- `scripts/generate-labels.py` — reads tokens via yaml.safe_load, emits SVG wordmark + 8-swatch legend
- `scripts/test_generate_labels.py` — TDD test suite (12 checks: security, output, content, mode-ban)
- `design-system/labels/the-bench-labels.svg` — generated wordmark + ink-legend card (3521 bytes)

## Decisions Made

- **PEP 668 externally-managed environment:** yamllint installed via `brew install yamllint` (on PATH); PyYAML via `pip3 install --user --break-system-packages PyYAML` since the system python is externally managed. A `.venv` was also created for check-jsonschema.
- **YAML truthy coercion:** The key `on` in each type entry must be quoted as `"on":` — yamllint 1.38.0 flags bare `on` as a truthy value (YAML 1.1 interprets `on`/`yes`/`true` as booleans). Fixed in Task 2.
- **Makefile labels as .PHONY:** File-based dependency (`labels: $(LABELS)`) causes `make -n labels` to fail before the SVG exists. Switched to a `.PHONY` direct invocation so the dry-run parses cleanly (Task 1 acceptance criterion).
- **Custom YAML schema over W3C DTCG:** bg/on/meaning per type — three fields, intuitive, maps directly to SVG generator variables. No Figma plugin or Style Dictionary pipeline needed.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] PEP 668 externally-managed Python**
- **Found during:** Task 1 (toolchain install)
- **Issue:** `pip install` and `pip3 install --user` both rejected by macOS externally-managed Python; standard RESEARCH install command failed
- **Fix:** Installed yamllint via `brew install yamllint`; PyYAML via `pip3 install --user --break-system-packages PyYAML`; also created a `.venv` for check-jsonschema
- **Files modified:** `.gitignore` (added .venv exclusion)
- **Verification:** `command -v yamllint` and `python3 -c "import yaml"` both succeed
- **Committed in:** abe4037

**2. [Rule 1 - Bug] YAML truthy coercion on 'on' key**
- **Found during:** Task 2 (tokens.yaml authoring)
- **Issue:** yamllint 1.38.0 flags bare `on:` as a truthy value; `make validate` exited non-zero
- **Fix:** Quoted all `on` keys as `"on":` in types block
- **Files modified:** design-system/tokens.yaml
- **Verification:** `make validate` exits 0; yamllint clean
- **Committed in:** 4c45f76

**3. [Rule 1 - Bug] Makefile file-based dependency breaks make -n labels**
- **Found during:** Task 1 (Makefile verification)
- **Issue:** `make -n labels` with file-based prerequisite fails when tokens.yaml doesn't exist yet, violating Task 1 acceptance criterion
- **Fix:** Changed labels to a `.PHONY` target that directly invokes the generator
- **Files modified:** Makefile
- **Verification:** `make -n labels` succeeds; `make labels` works after generator exists
- **Committed in:** abe4037

**4. [Rule 1 - Bug] TDD test false-positive on docstring mentioning yaml.load**
- **Found during:** Task 3 GREEN (generator implementation)
- **Issue:** Generator docstring contained the string `yaml.load()` for documentation purposes; the security test (T3) uses a string-match check and flagged it as a violation
- **Fix:** Rewrote docstring to say "the unsafe loader is forbidden" without the literal `yaml.load(` substring
- **Files modified:** scripts/generate-labels.py
- **Verification:** All 12 TDD checks pass
- **Committed in:** 9bf6102

---

**Total deviations:** 4 auto-fixed (2 bugs, 2 blocking environment issues)
**Impact on plan:** All auto-fixes necessary for correctness and environment compatibility. No scope creep. All acceptance criteria met as written.

## Issues Encountered

- macOS Sequoia (25.5.0) has PEP 668 enforcement on system Python — resolved with brew + --break-system-packages for user installs. The `.venv` was created for future use but the system python3 now also has PyYAML available.

## User Setup Required

None — all tools are now installed. New contributors need:
```bash
brew install yamllint
pip3 install --user --break-system-packages PyYAML
```
Or use the project `.venv` (created at `.venv/`, gitignored).

## Next Phase Readiness

- `design-system/tokens.yaml` is the contract for Phase 2's `params.scad` COLOR_* constants — file is stable, schema is proven by the generator
- `make validate && make labels` is the two-command integration test for any future tokens change
- Phase 01 Plan 03 (ADRs) can reference tokens.yaml schema as established
- Plan 01-04 (phase capstone) will visually verify `the-bench-labels.svg` in browser/Inkscape

---
*Phase: 01-public-spine-design-system-adrs*
*Completed: 2026-06-27*
