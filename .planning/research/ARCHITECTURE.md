# Architecture Research

**Domain:** Space-as-code / parametric digital twin of a physical home office
**Researched:** 2026-06-27
**Confidence:** HIGH (OpenSCAD patterns), MEDIUM (design-token-to-signage pipeline), HIGH (build order rationale from project context)

## Standard Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  PUBLIC SPINE (leads everything; no measurement dependency)          │
│  README.md · .planning/ · design-system/tokens.yaml · Makefile       │
├─────────────────────────────────────────────────────────────────────┤
│  PARAMETRIC MODEL (composes strictly downward)                       │
│                                                                      │
│  params.scad ──────────────────────────────────────────────────┐    │
│       │ (include)                                              │    │
│  model/room/shell.scad                                         │    │
│       │ (include)              ↑ all files include params.scad │    │
│  model/zones/*.scad                                            │    │
│       │ (include)                                              │    │
│  model/furniture/*.scad ◄──────────────────────────────────────┘    │
│       │ (include)                                                    │
│  model/accessories/*.scad                                            │
│       │ (include)                                                    │
│  model/storage/*.scad   (Gridfinity inserts, v2+)                    │
├─────────────────────────────────────────────────────────────────────┤
│  RENDER DRIVERS  (views/ compose model, set camera, emit PNGs)       │
│                                                                      │
│  views/top-plan.scad → renders/top-plan.png      (orthographic)      │
│  views/iso-overview.scad → renders/iso-overview.png                 │
│  views/focus-zone.scad → renders/focus-zone.png  (perspective)       │
│  views/maker-zone.scad → renders/maker-zone.png                     │
│  views/filming-zone.scad → renders/filming-zone.png                 │
├─────────────────────────────────────────────────────────────────────┤
│  DATA LAYER (independent of model; drives manifest + signage)        │
│                                                                      │
│  inventory/manifest.yaml ──► design-system/labels/  (SVG templates) │
│  design-system/tokens.yaml ──► params.scad (color constants)         │
│                           ──► design-system/labels/ (CSS vars)       │
└─────────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Key Rule |
|-----------|----------------|----------|
| `params.scad` | Single source of truth for ALL dimensions (with PLACEHOLDER markers when unmeasured) AND all color constants translated from tokens.yaml | Every other .scad file starts with `include <../../params.scad>`. Never define a dimension anywhere else. |
| `model/room/shell.scad` | Room boundary: walls, floor outline, window openings, door swings. Nothing inside the room. | Depends only on params.scad |
| `model/zones/*.scad` | Compose shell + furniture into spatial zones (focus-desk, maker-bench, creator-filming). One file per zone. | Depends on shell.scad + furniture/*.scad |
| `model/furniture/*.scad` | Individual furniture items as modules: standing desk, maker bench table, shelving, chair. | Depends only on params.scad |
| `model/accessories/*.scad` | Items placed on or near furniture: monitors, keyboard, lighting rig, camera arm. | Depends on furniture modules + params.scad |
| `model/storage/*.scad` | Gridfinity baseplates and custom bin inserts. Deferred to v2+ (build only after usage patterns known). | Depends on params.scad; optionally references furniture dims |
| `views/*.scad` | Render-driver files ONLY. Compose zones, set camera position/angle, set render color mode. No geometry of their own. | Imports zone files; never imported by anything else |
| `renders/` | Committed PNG outputs. NEVER gitignored. The proof-of-work artifact. | Written by Makefile via OpenSCAD CLI; humans never touch directly |
| `inventory/manifest.yaml` | Structured equipment list: every item with `status` (keep/discard/relocate), `zone`, `category`, `notes`. | Independent of .scad files; yamllint validated |
| `design-system/tokens.yaml` | Brand color palette + type tokens as the canonical source. Values flow INTO params.scad and label SVGs. | Never auto-synced in v1 (manual copy is fine); a `make sync-tokens` target can automate in v2+ |
| `design-system/labels/` | SVG label templates for bin labels and physical signage. Parameterized by shell variables from Makefile. | Driven by manifest.yaml category/zone fields |
| `Makefile` | Orchestrates: `make renders`, `make validate`, `make labels`. The one-command proof-of-work trigger. | Must work from repo root with only `openscad` and `yamllint` installed |
| `.planning/` | Meta spine: PROJECT.md, ROADMAP.md, STATE.md, research/. The public-facing identity and thesis framing. | Leads everything; has no dependencies |
| `decisions/` | Architecture Decision Records (ADRs). Log every non-obvious choice. | Reference from README |

## Recommended Project Structure

```
the-bench/
├── README.md                       # Public spine: thesis, identity, live renders inline
├── Makefile                        # make renders / make validate / make labels
├── params.scad                     # SINGLE SOURCE OF TRUTH (dimensions + color constants)
│
├── model/
│   ├── room/
│   │   └── shell.scad              # Walls, floor, windows, door swings
│   ├── zones/
│   │   ├── focus-desk.scad         # Deep-focus zone (desk + accessories)
│   │   ├── maker-bench.scad        # Electronics/maker zone
│   │   └── creator-filming.scad    # Camera sightlines + filming zone
│   ├── furniture/
│   │   ├── standing-desk.scad
│   │   ├── maker-bench-table.scad
│   │   ├── shelving.scad
│   │   └── chair.scad
│   ├── accessories/
│   │   ├── monitors.scad
│   │   ├── lighting-rig.scad
│   │   └── camera-arm.scad
│   └── storage/                    # v2+ only
│       ├── gridfinity-baseplate.scad
│       └── gridfinity-bins.scad
│
├── views/                          # Render-driver files (compose + camera only)
│   ├── top-plan.scad               # Orthographic floor plan
│   ├── iso-overview.scad           # Isometric full-room overview
│   ├── focus-zone.scad             # Perspective: desk detail
│   ├── maker-zone.scad             # Perspective: bench detail
│   └── filming-zone.scad           # Perspective: camera sightlines
│
├── renders/                        # COMMITTED PNGs — the public proof-of-work
│   ├── top-plan.png
│   ├── iso-overview.png
│   ├── focus-zone.png
│   ├── maker-zone.png
│   └── filming-zone.png
│
├── inventory/
│   └── manifest.yaml               # Equipment: every item, status, zone
│
├── design-system/
│   ├── tokens.yaml                 # Canonical brand tokens (colors + type)
│   └── labels/
│       ├── label-template.svg      # Parameterized bin/zone label template
│       └── generated/              # Output of make labels (gitignored or committed)
│
├── config/
│   └── home-assistant/             # HA YAML config (v2+)
│
├── decisions/
│   ├── ADR-TEMPLATE.md
│   └── ADR-001-openscad-include-strategy.md
│
└── .planning/
    ├── PROJECT.md
    ├── ROADMAP.md
    ├── STATE.md
    └── research/
```

### Structure Rationale

- **`params.scad` at root (not inside `model/`):** Every file at any depth needs it. Root placement keeps `include` paths shorter and signals it is the single source of truth for the whole repo.
- **`model/` hierarchy:** Composes strictly downward. room/shell has no knowledge of furniture; zones assemble them. This means changing a furniture dimension only requires changing params.scad, and the shell never needs to know.
- **`views/` as render drivers, separate from `model/`:** This is the Cal Bryant pattern. Model files are reusable libraries. View files are disposable assembly scripts that exist only to produce one PNG. Keeping them separate means the model stays clean of camera/render concerns.
- **`renders/` committed, never gitignored:** The PNG is the proof-of-work artifact. It must be in the repo to be visible on GitHub without any publishing pipeline. Every model change MUST produce a new committed render — this is what makes the repo "alive."
- **`design-system/` independent of `model/`:** Tokens define brand identity. They flow INTO params.scad (color constants) and INTO label SVGs (CSS variables). They do NOT import anything from model/. This keeps design identity decoupled from geometry.
- **`inventory/manifest.yaml` independent of `.scad` files:** The equipment manifest is structured data. It feeds label generation and is human-readable on GitHub. It does not need to know OpenSCAD exists.

## Architectural Patterns

### Pattern 1: Single Include Root with `include`, Not `use`

**What:** Every `.scad` file begins with `include <../../params.scad>` (relative depth varies). `include` (not `use`) is required because `use` imports only modules/functions — NOT global variables — and params.scad is all variables.

**When to use:** Always, for params.scad. For module libraries (furniture, accessories), use `use` from zone files to import only the module definitions without re-executing any top-level geometry.

**Trade-offs:** `include` means all of params.scad's variable assignments execute in the including file's scope. This is the intended behavior and the only way to share dimension constants. Risk: name collisions if a child file redefines a params variable. Prevention: all params.scad names are UPPER_SNAKE_CASE and documented as reserved.

**Example:**
```openscad
// In model/zones/focus-desk.scad
include <../../params.scad>          // Gets ROOM_W, ROOM_D, COLOR_CREAM, etc.
use <../furniture/standing-desk.scad> // Gets standing_desk() module only
use <../furniture/shelving.scad>

// Compose this zone
module focus_desk_zone() {
  standing_desk(
    width = DESK_W,
    depth = DESK_D,
    height = DESK_H_SIT
  );
  // ...
}
focus_desk_zone();
```

### Pattern 2: PLACEHOLDER Dimensions for Measurement-Independent Start

**What:** params.scad defines all dimensions on day one, but unmeasured values are assigned a clearly-marked placeholder and documented inline. The model runs, renders, and commits immediately with estimated values.

**When to use:** v1 — before the room is measured. Enables the entire model and render pipeline to exist as proof-of-work before any tape measure is involved.

**Trade-offs:** Renders are "wrong" in absolute dimensions but correct in structure, composition, and relative proportions. This is acceptable and is explicitly the v1 state ("before, estimated"). Measurement refines the model; it does not gate it.

**Example:**
```openscad
// params.scad
// ============================================================
// ROOM DIMENSIONS
// NOTE: Values marked [ESTIMATED] are placeholders.
//       Run 'make measured' after filling in real values.
// ============================================================

ROOM_W  = 3500;  // mm [ESTIMATED — measure wall-to-wall]
ROOM_D  = 4200;  // mm [ESTIMATED — measure wall-to-wall]
ROOM_H  = 2440;  // mm [ESTIMATED — standard 8ft ceiling]

// Measured (fill after measuring):
// ROOM_W = ???;
// ROOM_D = ???;

// ============================================================
// BRAND COLORS (from design-system/tokens.yaml)
// ============================================================
COLOR_CREAM     = "#f5efe2";
COLOR_NEARBLACK = "#1a1820";
COLOR_TERRACOTTA= "#ec6a43";
COLOR_PLUM      = "#4a2a57";
COLOR_MAGENTA   = "#c63c82";

// ============================================================
// UNIT: all dimensions in millimeters
// ============================================================
$fn = 32;  // curve resolution
```

### Pattern 3: View Files as Render Drivers

**What:** Files in `views/` are not reusable libraries. Each one imports the composed zone model, sets a camera position, and exists only to produce one specific PNG via the Makefile.

**When to use:** Every committed render is backed by exactly one view file. Adding a new render angle means adding a new view file — the model is never modified to accommodate a render.

**Trade-offs:** Slight duplication of import statements across view files. This is acceptable: view files are thin and disposable.

**Example:**
```openscad
// views/top-plan.scad
include <../params.scad>
use <../model/room/shell.scad>
use <../model/zones/focus-desk.scad>
use <../model/zones/maker-bench.scad>
use <../model/zones/creator-filming.scad>

// Compose full room for top-down render
room_shell();
focus_desk_zone();
maker_bench_zone();
creator_filming_zone();

// Camera is set via Makefile CLI args — no camera() call needed here
```

```makefile
# Makefile
OPENSCAD = openscad
RENDERS  = renders

renders/top-plan.png: views/top-plan.scad params.scad model/**/*.scad
    $(OPENSCAD) -o $@ \
      --camera=0,0,5000,0,0,0 \
      --projection=ortho \
      --imgsize=2400,2400 \
      $<

renders/iso-overview.png: views/iso-overview.scad params.scad model/**/*.scad
    $(OPENSCAD) -o $@ \
      --camera=1000,1000,2000,45,0,45 \
      --imgsize=2400,1800 \
      $<

renders: renders/top-plan.png renders/iso-overview.png \
         renders/focus-zone.png renders/maker-zone.png renders/filming-zone.png

validate:
    yamllint inventory/manifest.yaml

.PHONY: renders validate labels
```

### Pattern 4: Design Tokens Flow from tokens.yaml to Two Surfaces

**What:** `design-system/tokens.yaml` is the canonical source for brand colors and type. It flows downstream to two surfaces: (1) `params.scad` color constants, (2) SVG label templates. In v1, this is a manual sync — copy hex values. In v2+, a `make sync-tokens` script reads tokens.yaml and writes the OpenSCAD color constants block.

**When to use:** Whenever a brand color is used in a render or on a label. Never hardcode hex values in model/ or views/ files — always reference the named constant from params.scad.

**Trade-offs:** Manual sync in v1 can drift. Mitigation: comment every color constant in params.scad with its token name so drift is immediately visible.

```yaml
# design-system/tokens.yaml
color:
  cream:      { value: "#f5efe2", role: background }
  nearblack:  { value: "#1a1820", role: text-primary }
  terracotta: { value: "#ec6a43", role: accent-warm }
  plum:       { value: "#4a2a57", role: accent-cool }
  magenta:    { value: "#c63c82", role: pop }

type:
  display: { family: "Archivo", weight: 700 }
  body:    { family: "Newsreader", weight: 400 }
  label:   { family: "IBM Plex Mono", weight: 400 }
```

## Data Flow

### Model → Render Pipeline

```
params.scad  (dimensions + color constants)
    │
    ├──► model/room/shell.scad   (include)
    │         │
    │    model/furniture/*.scad  (use from zones)
    │         │
    │    model/zones/*.scad      (include shell + use furniture)
    │         │
    │    views/*.scad            (compose zones; camera via Makefile CLI)
    │         │
    │    [Makefile: openscad -o renders/X.png --camera=... views/X.scad]
    │         │
    └──────► renders/*.png       (COMMITTED — visible on GitHub)
```

### Design Tokens → Physical Signage

```
design-system/tokens.yaml
    │
    ├──► params.scad             (COLOR_* constants — manual sync v1)
    │         └──► renders/*.png (OpenSCAD uses colors in model visualization)
    │
    └──► design-system/labels/label-template.svg
              │  (CSS variables filled from tokens.yaml)
              │
         [Makefile: make labels — substitutes manifest.yaml values into template]
              │
         design-system/labels/generated/
              └──► zone-labels.svg, bin-labels.svg  (print-ready SVG)
```

### Manifest → Labels

```
inventory/manifest.yaml
    │ (fields: name, zone, category, status)
    │
[Makefile: make labels — for each item in manifest, render label SVG]
    │
design-system/labels/generated/
    └──► [zone]-[category]-label.svg
```

### Key Data Flows

1. **Dimension change:** Edit `params.scad` → `make renders` → all affected PNGs regenerate → commit the changed PNGs.
2. **Measurement refinement:** Fill in real dims in `params.scad` (replacing ESTIMATED values) → `make renders` → commit. The git diff on the PNG is the visual proof of the measurement update.
3. **Brand color update:** Edit `tokens.yaml` → manually update COLOR_* in `params.scad` → `make renders` + `make labels` → commit.
4. **New equipment:** Add item to `manifest.yaml` → `make validate` → optionally `make labels` → commit.
5. **New furniture:** Create `model/furniture/new-item.scad` → add `use` in affected zones → `make renders` → commit.

## Suggested Build Order

This order honors the inversion: public spine leads; measurement is a non-blocking refinement.

### Tier 0: Public Spine (no measurement, no OpenSCAD required)

These can be built immediately and committed as the first pulses. Nothing in this tier depends on room dimensions.

1. `README.md` — public hook: thesis ("environment as provenance"), identity, "before" photos, placeholder for first render (img tag that will be filled by Tier 2)
2. `.planning/` — already started; ensure PROJECT.md, ROADMAP.md, STATE.md exist and are substantive
3. `design-system/tokens.yaml` — canonical brand palette; defines the visual identity for all downstream surfaces
4. `design-system/labels/label-template.svg` — a printable label template using brand tokens; demonstrates the design-system-to-physical pipeline immediately
5. `Makefile` skeleton — `make validate`, `make renders` (no-op until Tier 1), `make labels` targets defined even if empty
6. `decisions/ADR-001-openscad-include-strategy.md` — log the `include` vs `use` decision before writing a line of SCAD

**Pulse artifact from Tier 0:** `README.md` live on GitHub with thesis, brand tokens, label template, and ADR. Provable without measurements.

### Tier 1: Parametric Primitives (estimated dims OK — no measurement gate)

OpenSCAD is installed here. Dimensions are ESTIMATED but params.scad is the single source of truth from the start.

7. `params.scad` — all ESTIMATED dimensions clearly marked + COLOR_* constants from tokens.yaml
8. `model/room/shell.scad` — room boundary with ESTIMATED dims; `make renders` produces a first (imprecise) floor plan PNG
9. `views/top-plan.scad` + `renders/top-plan.png` — committed floor plan PNG; FIRST RENDER ARTIFACT; updates README.md img tag
10. `model/furniture/standing-desk.scad` — parametric desk module
11. `model/furniture/maker-bench-table.scad` — parametric bench module
12. `model/zones/focus-desk.scad` + `model/zones/maker-bench.scad` — first zone compositions
13. `views/iso-overview.scad` + `renders/iso-overview.png` — isometric render; "before" room in code

**Pulse artifact from Tier 1:** OpenSCAD floor plan + isometric render of the "before" room, committed and visible on GitHub. The parametric code exists. Still no accurate measurements needed.

### Tier 2: Measurement Refinement (first and ONLY measurement gate)

This is where room measurement matters. It refines what already exists; it does not unlock the first pulse.

14. Measure the room (walls, outlets, windows, door swing)
15. Update ESTIMATED values in `params.scad` with real dimensions; remove ESTIMATED markers
16. `make renders` — all views regenerate with accurate dims; git diff shows the delta
17. `inventory/manifest.yaml` — equipment manifest for the "before" room (harvested from the-bench-old)
18. `make validate` — manifest validated
19. Three-mode zone files refined: `views/filming-zone.scad`, `views/maker-zone.scad` — camera sightlines modeled with real dims

**Pulse artifact from Tier 2:** Accurate parametric model of the "before" room. Doll-house 3D print is now unlocked (export STL from top-plan view, slice, print).

### Tier 3: Accessories, Signage, Storage (v1 completion)

20. `model/accessories/*.scad` — monitors, lighting rig, camera arm positioned in zones
21. `design-system/labels/generated/*.svg` — `make labels` from manifest + template
22. `renders/` — full render suite committed; README updated with all five views

**Pulse artifact from Tier 3:** v1 complete. Full parametric "before" room. All renders committed. Equipment manifest. Brand label templates. README is the public artifact.

### Tier 4: Physical Redesign (v2+ — governed by physical-dependency checklist)

The following physical-dependency checklist from the prior roadmap is PRESERVED as the sequencing logic for the physical build (v2+). It is NOT a v1 gate and does NOT block any Tier 0-3 work.

```
PHYSICAL DEPENDENCY CHECKLIST (v2+ only):
[ ] 1. Measure room accurately                        ← already done in Tier 2
[ ] 2. Install infra/power/cable BEFORE furniture moves
[ ] 3. Move furniture to final positions
[ ] 4. Establish storage BASELINE before custom inserts
[ ] 5. Deploy Gridfinity AFTER real usage patterns known (not before)
[ ] 6. Deploy HA MANUAL SCENES before adding sensor automation
[ ] 7. Add presence/sensor automation only after manual scenes proven stable
```

This checklist governs the PHYSICAL BUILD ORDER when the Bench is redesigned. The parametric model evolves in parallel: each physical change is modeled in the repo, rendered, and committed as a proof-of-work pulse.

## Anti-Patterns

### Anti-Pattern 1: Measurement as a First-Phase Gate

**What people do:** Write `params.scad` as an empty stub with comments saying "fill in after measuring." Block all modeling and all rendering until real measurements exist.

**Why it's wrong:** This is exactly what killed `the-bench-old`. The measurement gate transforms a creative project into a chore queue. Nothing is shippable until a single physical task is complete, and physical tasks have unpredictable timing.

**Do this instead:** Write `params.scad` on day one with ESTIMATED dimensions, clearly marked. Build and render immediately. Treat measurement as a refinement that improves the model — not a gate that enables it. The git diff when you replace ESTIMATED values IS the proof-of-work for the measurement session.

### Anti-Pattern 2: Dimensions Defined Outside params.scad

**What people do:** Hardcode a furniture dimension inside `furniture/standing-desk.scad` because "it's a specific property of the desk." Then the zone file that needs to position things relative to the desk cannot find the dimension.

**Why it's wrong:** Creates unit drift — two files with a slightly different notion of desk width. Break composition — the room shell cannot know if the desk fits without importing the furniture file. Makes `make renders` non-reproducible if values are changed in multiple places.

**Do this instead:** ALL dimensions live in `params.scad`. `DESK_W`, `DESK_D`, `DESK_H_SIT`, `DESK_H_STAND` are in params.scad and the desk module accepts them as parameters with defaults pointing to those constants. This means: change one number, re-render, get correct output everywhere.

### Anti-Pattern 3: Gitignoring Renders

**What people do:** Add `renders/*.png` to `.gitignore` because "generated files shouldn't be in the repo."

**Why it's wrong:** The PNG IS the proof-of-work artifact. It must be in the repo for GitHub to display it in README.md. Without committed renders, the repo looks empty to a stranger. There is no publishing pipeline in this project — the repo IS the public surface.

**Do this instead:** Commit renders explicitly. The Makefile regenerates them from source; the committed state is the last-rendered snapshot. A CI check can verify renders are current (diff not empty) but this is optional.

### Anti-Pattern 4: Mixing `include` and `use` Without Intent

**What people do:** Use `use` for params.scad (expecting variables to be available) or `include` for furniture modules (causing their geometry to execute in the zone context).

**Why it's wrong:**
- `use <params.scad>` — variables are NOT exported; dimensions are undefined; model silently uses `undef`.
- `include <furniture/standing-desk.scad>` — the desk geometry executes at origin in whatever file included it, producing a floating desk.

**Do this instead:** `include <params.scad>` everywhere (always). `use <model/furniture/standing-desk.scad>` from zones and views (imports the module definition only). This is the only safe combination.

### Anti-Pattern 5: Design Tokens Only in the Digital Layer

**What people do:** Define brand colors in tokens.yaml and use them in renders, but never produce physical signage or bin labels from the same source.

**Why it's wrong:** The design system's value is that it flows from the digital model to the physical room. Bin labels, zone markers, and physical signage that match the render colors are what makes the environment "designed" vs "assembled." This is core to the "environment as provenance" thesis.

**Do this instead:** `make labels` produces SVG label templates driven by the same token values used in renders. Print them. The visual language of the room matches the visual language of the repo.

### Anti-Pattern 6: Waterfall Zones (one layout file for the whole room)

**What people do:** Create a single `zones/layout-a.scad` that contains every furniture item, every accessory, the room shell, and camera setup. (This is what `the-bench-old` was moving toward.)

**Why it's wrong:** Cannot be composed. Cannot render individual zones. Cannot be edited without understanding the entire file. Breaks when furniture changes.

**Do this instead:** One file per zone, each composable independently. Views compose zones. Room shell is separate. This means you can render just the maker bench in isolation while redesigning it.

## Integration Points

### External Services / Tools

| Tool | Integration Pattern | Notes |
|------|---------------------|-------|
| OpenSCAD CLI | `openscad -o renders/X.png --camera=... views/X.scad` | Makefile target; called headlessly |
| yamllint | `yamllint inventory/manifest.yaml` | `make validate` target |
| ImageMagick (optional) | Post-process PNGs: 2x render + Lanczos downscale for anti-aliasing | Upgrade from default jagged OpenSCAD PNG output; add to Makefile if quality matters |
| Home Assistant | YAML config in `config/home-assistant/` committed to repo | v2+ only; HA Git Exporter or SSH sync |

### Internal Component Dependency Map

```
params.scad
  ↓ (include — all components)
model/room/shell.scad
  ↓ (use from zones)
model/furniture/*.scad ─────────────────────────────────────┐
  ↓ (use from zones)                                        │
model/accessories/*.scad                                    │
  ↓ (use from zones)                                        │
model/zones/focus-desk.scad ←──── shell + furniture + acc. ─┘
model/zones/maker-bench.scad ←─── shell + furniture + acc.
model/zones/creator-filming.scad ← shell + furniture + acc.
  ↓ (use from views)
views/*.scad ←─────────────────── compose zones + camera
  ↓ (Makefile: openscad -o)
renders/*.png ←──────────────────── committed PNG artifacts

design-system/tokens.yaml
  ↓ (manual sync / make sync-tokens)
params.scad (COLOR_* constants)
  ↓ (via renders)
renders/*.png (colored model)

design-system/tokens.yaml
  ↓ (CSS variables in template)
design-system/labels/label-template.svg
  ↑
inventory/manifest.yaml
  ↓ (Makefile: make labels)
design-system/labels/generated/*.svg (print-ready)
```

### Boundary: params.scad ↔ design-system/tokens.yaml

**Communication:** Manual sync in v1. Makefile `sync-tokens` target in v2+.
**Notes:** These are two representations of the same truth (brand colors). tokens.yaml is the canonical source; params.scad COLOR_* constants are derived. If they ever diverge, tokens.yaml wins.

### Boundary: manifest.yaml ↔ model/*.scad

**Communication:** None directly. The manifest lists equipment; the model positions it.
**Notes:** This is intentional decoupling. The manifest is structured data for humans and label generation. The model is geometry for renders and printing. They share zone vocabulary (same zone names used in both) but do not import each other.

## Sources

- OpenSCAD `include` vs `use` semantics: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement
- Cal Bryant's OpenSCAD project structure and render pipeline with ImageMagick: https://calbryant.uk/blog/pushing-openscad-to-the-max-with-discipline-and-imagemagick/
- OpenSCAD headless CLI rendering: https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment
- doratracyer/floor_plan (3D-printable floor plan generator reference): https://github.com/doratracyer/floor_plan
- Gridfinity Rebuilt OpenSCAD (composition pattern reference): https://github.com/kennetek/gridfinity-rebuilt-openscad
- Design tokens specification and YAML support: https://cobalt-ui.pages.dev/guides/tokens
- Keep build artifacts in the repository (rationale for committing PNGs): https://medium.com/@MrJamesFisher/keep-your-build-artifacts-in-the-repository-69ad3a6edf1f

---
*Architecture research for: The Bench — space-as-code parametric room model*
*Researched: 2026-06-27*
