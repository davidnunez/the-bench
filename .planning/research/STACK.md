# Stack Research

**Domain:** Physical space as version-controlled parametric code — "The Bench" home office/studio
**Researched:** 2026-06-27
**Confidence:** HIGH on core OpenSCAD toolchain and organizer ecosystem; MEDIUM on project structure conventions (no canonical standard exists, synthesized from best-practice sources)

---

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| OpenSCAD (snapshot) | 2026.06.12 | Primary modeling engine: room shell, furniture primitives, floor plan generation, STL export | The only scriptable, plain-text solid modeler in the 3D printing ecosystem. `.scad` files are fully git-diffable and version-controllable — this is the entire point of the project. Snapshot required (not stable 2021.01) for Manifold backend and QuackWorks compatibility. |
| BOSL2 | v2.0.745 (Jun 2026) | Advanced OpenSCAD shape library | Required dependency for QuackWorks (Underware, openGrid, Neogrid). Also provides attachment system, threads, precision geometry, and 2D shape primitives needed for furniture modeling beyond basic boxes. |
| Gridfinity Rebuilt (kennetek) | v2.0.0 (Sep 2025) | Parametric Gridfinity bins and baseplates | The canonical open-source OpenSCAD implementation of Gridfinity. Pure parametric: width, length, height, compartments, magnets, scoops are all parameters. Most widely used, most community add-ons target it. |
| QuackWorks (AndyLevesque) | `main` branch | Unified source for Underware, openGrid, Neogrid 2.0, Deskware, Multiconnect | Single repo containing 99.2% OpenSCAD for all four organizer systems the project requires. BOSL2 is its only external dependency. Requires OpenSCAD developer release. |
| doratracyer/floor_plan | `main` branch | SVG → 3D-printable doll-house floor plan conversion | OpenSCAD-based tool that consumes standardized SVGs (walls as line paths, doors/windows as rectangles) and emits STL. GPL-3.0, print-ready with parametric wall heights and door/window sizing. This is the doll-house print path. |

**Confidence:** HIGH — OpenSCAD snapshot version verified via Homebrew cask `openscad@snapshot` (formulae.brew.sh). BOSL2 v2.0.745 verified via GitHub releases. Gridfinity Rebuilt v2.0.0 verified via GitHub releases + newreleases.io. QuackWorks confirmed 99.2% OpenSCAD on GitHub. doratracyer/floor_plan confirmed GPL-3.0 on GitHub.

---

### Supporting Libraries and Tools

| Library / Tool | Version | Purpose | When to Use |
|----------------|---------|---------|-------------|
| yamllint | current pip | YAML syntax and style linting | In `make validate` and pre-commit; catches malformed YAML before schema check |
| check-jsonschema | current pip | Validate equipment manifest YAML against JSON Schema | After yamllint; enforces required fields, types, enum values in `equipment/` manifests |
| python3 (present) | 3.x (present) | Run yamllint and check-jsonschema; generate design-system tokens | Already installed; no new runtime required |
| Node 22 (present) | 22.x (present) | `npm run` wrappers over Make targets; potential future JSON generation from YAML manifest | Thin glue layer — keep logic in Makefile, use npm scripts only as discoverable shortcuts |
| git submodules | — | Pin BOSL2, Gridfinity Rebuilt, QuackWorks as versioned dependencies | All three libraries are pulled as submodules into `models/lib/`; locks revision per repo commit |

---

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| GNU Make | Build pipeline: render PNGs, export STLs, validate YAML, clean artifacts | `make renders` triggers all OpenSCAD CLI calls; output is committed PNG/SVG. Single `Makefile` at repo root. |
| OpenSCAD CLI (`--camera`, `--projection o`, `--imgsize`) | Headless rendering of committed visual artifacts | Top-down floor plan: `--camera 0,0,0,0,0,0,5000 --projection o --autocenter --viewall`. Perspective: `--camera 0,-500,1500,45,0,0,3000 --projection p`. |
| OpenSCAD `projection(cut=false)` | Extract 2D floor plan from 3D room model | Wrapping the 3D shell in `projection()` and exporting SVG gives a diff-able flat floor plan without a separate 2D model. |
| `OPENSCADPATH` env variable | Library resolution without hardcoded paths | Set in Makefile: `export OPENSCADPATH=$(PWD)/models/lib` so `use <BOSL2/std.scad>` resolves regardless of machine |
| pre-commit (optional) | Run yamllint + check-jsonschema on every commit | Add as a lightweight guardrail; not required for v1 |

---

## Parametric Physical-Organization Ecosystem

This is the central detail the project requires. Four systems, one codebase (QuackWorks), with distinct physical roles:

### Gridfinity
**What it is:** A modular grid system (42mm grid) for organizing small items on horizontal surfaces — desktop, drawer bottoms, shelves. The de-facto community standard.
**Toolchain:** `kennetek/gridfinity-rebuilt-openscad` (OpenSCAD, parametric). Add as git submodule. Web generator also available at gridfinity.perplexinglabs.com.
**Grid:** 42mm × 42mm base unit (Zack Freedman spec)
**Role in this project:** Desktop organization (pens, USB drives, small tools at the desk), maker bench bins (component types, resistor drawers), any horizontal surface at The Bench.
**Confidence:** HIGH

### openGrid
**What it is:** A wall and desk mounting framework using a 28mm grid. Clean, modern aesthetic suitable for living/studio spaces (not garage shelving). Designed to be Gridfinity-compatible via the 28mm/42mm math.
**Toolchain:** Source in `QuackWorks/openGrid/openGrid.scad`. Requires BOSL2. Web generator at gridfinity.perplexinglabs.com (openGrid tab). Also a separate GitHub org at `openGrid-3D`.
**Grid:** 28mm (7×7mm subgrid). Compatible with Gridfinity since 3×28mm = 84mm = 2×42mm.
**Role in this project:** Wall mounting above the maker bench (scissors, tape, rulers, small tools). SKADIS-alternative that is fully code-defined and parametric.
**Confidence:** HIGH — verified via opengrid.world and QuackWorks repo

### Underware
**What it is:** A snap-together cable channel system for under-desk cable management and wall cable runs. Version 2.0 is fully parametric OpenSCAD with 10,000+ channel size variations.
**Toolchain:** Source in `QuackWorks/Underware/`. Requires BOSL2. MakerWorld customizer available for no-install generation. CC-BY-NC-SA license.
**Role in this project:** Under-desk cable trunking (power brick hiding, monitor cable runs), wall cable channels. Completes the trio: Gridfinity = desktop, openGrid = wall, Underware = underneath.
**Confidence:** HIGH — verified via QuackWorks README and handsonkatie.com/underware

### Neogrid 2.0
**What it is:** A hybrid drawer organization system. 3D-printed connectors (X-junction, L, T, I pieces) + store-bought dividers (MDF/plywood/acrylic sheet). For large items that are impractical to contain in Gridfinity bins — clothing, tools, materials.
**Toolchain:** Source in `QuackWorks/NeoGrid/`. Requires BOSL2. Compatible with Gridfinity and openGrid for mixed-system drawers.
**Role in this project:** IKEA Alex drawer organization (the drawers in the existing desk setup). Fills the gap between "small components in Gridfinity bins" and "no organization at all for larger items."
**Confidence:** HIGH — verified via QuackWorks README and makerworld.com/en/models/1501061

**Critical note:** All four systems share BOSL2 as a dependency and all source from one repo (QuackWorks). A single git submodule pull gets the entire organizer ecosystem. The web generators (Perplexing Labs, MakerWorld customizers) allow no-install STL generation for testing before committing custom OpenSCAD files.

---

## Doll-House Floor Plan Print Path

The v1 milestone calls for a physical 3D-printed scale model of the room ("doll-house" floor plan). The path:

1. **SVG creation:** Draw room walls as SVG line paths using real dimensions in mm (1mm SVG = 1mm real via `viewBox`). Create separate SVG layers/documents for: exterior walls, interior walls, door openings (rectangles), window openings (rectangles).

2. **doratracyer/floor_plan.scad:** Import SVGs into `floor_plan.scad` via OpenSCAD's `import()`. Parametric wall height, wall thickness, door height, window sill height. Generates a fully printable doll-house model.

3. **Scale:** Print at 1:50 (1mm real = 0.02mm model → impractical) or more typically 1:75 or 1:100 on a 256mm print bed. At 1:100, a 4m room prints as 40mm — fine for context; at 1:50, 80mm per 4m — more legible. Choose scale based on bed size and desired detail.

4. **STL export:** `openscad -o stl/floor-plan.stl models/floor-plan/floor_plan.scad`

5. **Alternative path (OpenSCAD-native):** Instead of importing SVG, define the room geometry directly in OpenSCAD using `linear_extrude()` on a 2D room outline built with `polygon()` and boolean operations for door/window cutouts. This keeps everything in OpenSCAD and eliminates the SVG intermediate. Recommended for v1 since you're already defining the room parametrically; the SVG path adds a conversion step.

**Recommendation for v1:** Use the OpenSCAD-native path — `linear_extrude(height = wall_h_scaled)` applied to a `difference()` of the room perimeter polygon minus door/window rectangles. This re-uses `params.scad` directly and emits an STL from the same model. Pull in doratracyer/floor_plan as a reference/inspiration, not as a hard dependency, unless the SVG import workflow proves faster for iterating.

**Confidence:** HIGH for the doratracyer tool (verified on GitHub). MEDIUM for the OpenSCAD-native alternative (standard OpenSCAD workflow, not a packaged tool).

---

## Design System in OpenSCAD

Brand tokens (palette + type) must be usable both for renders and for physical signage/bin labels.

**Palette as OpenSCAD constants** (`design-system/palette.scad`):
```openscad
// The Bench — Brand Palette (2026)
bench_cream      = "#f5efe2";   // Background / base
bench_near_black = "#1a1820";   // Text / structure
bench_terracotta = "#ec6a43";   // Primary accent
bench_plum       = "#4a2a57";   // Secondary accent
bench_magenta    = "#c63c82";   // Pop accent
```

Include in render scripts via `include <../../design-system/palette.scad>`. Assign `color(bench_terracotta)` to furniture primitives, `color(bench_near_black)` to room shell. This makes renders visually branded rather than OpenSCAD's default grey.

**Palette as YAML tokens** (`design-system/tokens.yaml`): Parallel record for Node/Python consumers — generating physical label SVGs, future site glue, or print-layout PDFs.

**Type tokens** (`design-system/tokens.yaml`): Font names for labels (Archivo, Newsreader, IBM Plex Mono). Not usable in OpenSCAD renders directly (OpenSCAD's `text()` uses system fonts), but relevant for any Node-generated label artifacts.

---

## Installation

```bash
# OpenSCAD: use @snapshot cask, NOT bare openscad cask
# The bare cask installs 2021.01 (deprecated, disable date Sep 1 2026)
# @snapshot installs 2026.06.12 with Manifold backend
brew install --cask openscad@snapshot

# After install: enable Manifold in Preferences > Advanced > Backend: Manifold
# This reduces render time from minutes to seconds on complex models

# Libraries as git submodules (run once after cloning)
git submodule add https://github.com/BelfrySCAD/BOSL2.git models/lib/BOSL2
git submodule add https://github.com/kennetek/gridfinity-rebuilt-openscad.git models/lib/gridfinity-rebuilt
git submodule add https://github.com/AndyLevesque/QuackWorks.git models/lib/QuackWorks
git submodule add https://github.com/doratracyer/floor_plan.git models/lib/floor_plan

# Update all submodules
git submodule update --init --recursive

# YAML validation (Python tools, python3 is present)
pip install yamllint check-jsonschema

# Node is already present (22.x); no additional npm packages required for v1
```

---

## Recommended Project Structure

```
the-bench/
├── Makefile                          # Build pipeline: make renders, make stl, make validate
├── package.json                      # npm scripts wrapping make targets (optional discoverable layer)
├── models/
│   ├── room/
│   │   ├── params.scad               # Single source of truth: all dimensions (mm)
│   │   ├── shell.scad                # Room walls, floor, ceiling — include params.scad
│   │   ├── furniture/
│   │   │   ├── desk.scad
│   │   │   ├── chair.scad
│   │   │   └── ...
│   │   └── zones/
│   │       ├── deep-focus.scad       # Mode overlay: zone annotations
│   │       ├── creator.scad
│   │       └── maker.scad
│   ├── floor-plan/
│   │   └── floor_plan.scad           # Doll-house print model (room-shell derived)
│   ├── organizers/
│   │   ├── gridfinity/               # Custom Gridfinity bin designs
│   │   └── underware/                # Custom Underware channel configs
│   └── lib/                          # Git submodules
│       ├── BOSL2/
│       ├── gridfinity-rebuilt/
│       ├── QuackWorks/
│       └── floor_plan/               # doratracyer reference
├── renders/                          # Committed build artifacts (generated by `make renders`)
│   ├── floor-plan-top.png            # Top-down orthographic (2048×2048)
│   ├── floor-plan-top.svg            # 2D projection SVG (diff-friendly)
│   └── perspective.png               # 3D perspective view
├── stl/                              # Committed STL exports (generated by `make stl`)
│   └── floor-plan-print.stl
├── equipment/
│   ├── schema.yaml                   # JSON Schema for manifest validation
│   └── inventory.yaml                # Equipment manifest
├── design-system/
│   ├── palette.scad                  # Color constants for OpenSCAD renders
│   └── tokens.yaml                   # Brand tokens for Node/Python consumers
└── .planning/
```

---

## Makefile Render Pipeline Pattern

```makefile
OPENSCADPATH := $(PWD)/models/lib
export OPENSCADPATH

OPENSCAD := openscad
IMGSIZE   := 2048,2048

.PHONY: renders stl validate clean

renders: renders/floor-plan-top.png renders/floor-plan-top.svg renders/perspective.png

# Top-down orthographic floor plan
renders/floor-plan-top.png: models/room/shell.scad models/room/params.scad
	$(OPENSCAD) -o $@ \
	  --camera 0,0,0,0,0,0,10000 \
	  --projection o \
	  --imgsize $(IMGSIZE) \
	  --autocenter --viewall \
	  $<

# 2D SVG floor plan (projection of 3D model)
renders/floor-plan-top.svg: models/room/shell.scad models/room/params.scad
	$(OPENSCAD) -o $@ \
	  --projection o \
	  --autocenter --viewall \
	  $<

# Perspective view
renders/perspective.png: models/room/shell.scad models/room/params.scad
	$(OPENSCAD) -o $@ \
	  --camera 0,-2000,3000,45,0,0,8000 \
	  --projection p \
	  --imgsize 2048,1536 \
	  --autocenter --viewall \
	  $<

# STL for doll-house print
stl: stl/floor-plan-print.stl

stl/floor-plan-print.stl: models/floor-plan/floor_plan.scad models/room/params.scad
	$(OPENSCAD) -o $@ $<

# YAML validation
validate:
	yamllint equipment/inventory.yaml
	check-jsonschema --schemafile equipment/schema.yaml equipment/inventory.yaml

clean:
	rm -f renders/*.png renders/*.svg stl/*.stl
```

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| `brew install --cask openscad@snapshot` | `brew install --cask openscad` (2021.01) | Never for this project — QuackWorks requires dev release; 2021.01 cask is deprecated |
| Gridfinity Rebuilt (kennetek) | ostat/gridfinity_extended_openscad | If you need specific extended features not in kennetek; both are active but kennetek is more widely adopted |
| QuackWorks submodule (all organizer systems) | Individual repos per system | If only one system is needed and you want a smaller dependency footprint |
| OpenSCAD-native floor plan (`linear_extrude`) | doratracyer SVG import path | If you want to generate the doll-house model from a separate architectural drawing rather than sharing params.scad |
| Makefile + OpenSCAD CLI | GitHub Actions | Use GitHub Actions for CI validation of YAML manifests; keep renders local (no headless display needed) |
| yamllint + check-jsonschema | yamllint alone | yamllint catches syntax only; check-jsonschema enforces the manifest schema — both needed, complementary |
| YAML equipment manifest | SQLite | Only if relational queries become necessary (e.g., "all items under $100 in the maker zone"); overkill for v1 |

---

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| `brew install --cask openscad` (bare) | Installs deprecated 2021.01; disabled Sep 1 2026; incompatible with QuackWorks which requires dev release | `brew install --cask openscad@snapshot` (2026.06.12) |
| Fusion 360 for any Gridfinity work | Proprietary, binary files, no git workflow, subscription-gated exports, no parametric chain to text files | Gridfinity Rebuilt in OpenSCAD |
| FreeCAD for room modeling | FreeCAD's BIM workbench is excellent but its parametric model is GUI-driven and not the "over-engineering as legible artifact" the project wants; `.FCStd` files are binary | OpenSCAD `.scad` files — plain text, every parameter visible |
| SweetHome 3D | The old research recommended it for rapid layout, but it adds a separate tool whose output doesn't integrate into the OpenSCAD pipeline; XML diff is brittle | OpenSCAD all the way — keep the pipeline single-tool |
| Blender for renders | Photorealism is not the goal; OpenSCAD's default rendering (with color assignments) produces exactly the "over-engineered code artifact" aesthetic that is the project hook | OpenSCAD headless CLI rendering |
| JSCAD / OpenJSCAD | Different paradigm (JavaScript), different community, no direct interop with the OpenSCAD/Gridfinity/QuackWorks ecosystem | OpenSCAD — the community files are `.scad`, not `.js` |
| Tinkercad | No scripting, GUI-only, no git workflow, no parametric export chain | OpenSCAD |
| SketchUp | Binary `.skp` files, not diffable; free tier stripped significantly | OpenSCAD |
| Planner5D / Homestyler / Floorplanner.com | Cloud SaaS, no code export, no git integration, vendor lock-in | OpenSCAD + doratracyer floor_plan |
| SolidPython2 | Adds a Python→OpenSCAD compilation layer, increasing complexity without proportional benefit for this project; the over-engineering is OpenSCAD itself, not Python wrapper generation | Pure OpenSCAD with `params.scad` as the parameter surface |

---

## Version Compatibility

| Component | Compatible With | Notes |
|-----------|-----------------|-------|
| QuackWorks main | OpenSCAD dev release (2026.x) ONLY | README explicitly states "the regular release will not work" — this means 2021.01 stable is insufficient |
| BOSL2 v2.0.745 | OpenSCAD 2021.01+ (2026.x dev preferred) | Requires function literals from 2021.01; works better with dev snapshots |
| Gridfinity Rebuilt v2.0.0 | OpenSCAD 2021.01+, dev snapshot preferred | Use dev snapshot for fast Manifold rendering; 2021.01 works but CGAL rendering is slow |
| doratracyer/floor_plan main | OpenSCAD (any version supporting `import()` for SVG) | Uses `import()` for SVG; available in 2021.01+. Dev snapshot renders faster. |
| check-jsonschema | python3 3.8+ | Pure Python; no version conflicts expected |
| yamllint | python3 3.8+ | Pure Python; no version conflicts expected |

---

## Stack Patterns by Variant

**For rendering committed PNG artifacts on every model change:**
- Use Makefile targets with `openscad --camera ... --projection o` for floor plan and `--projection p` for perspective
- Commit renders to `renders/` directory — they are build artifacts but committing them makes "the repo always shows the current state" without requiring a build step to see it
- Camera parameters need tuning once per view; thereafter they are stable

**For the doll-house 3D-print (quickest path to v1 artifact):**
- Before room dimensions are measured: create a placeholder model with estimated dimensions; the print demonstrates the toolchain, not the final room
- After measurement: update `params.scad` → re-run `make stl` → reprint
- Scale to fit printer bed: at 1:75 scale, a 3.6m × 4.2m room prints as 48mm × 56mm (very small, fits on any bed but hard to read); at 1:50 it's 72mm × 84mm (more legible); at 1:25 it's 144mm × 168mm (requires large bed or split into sections)

**For integrating organizer systems without installing OpenSCAD locally for each print:**
- Use web generators (Perplexing Labs for Gridfinity/openGrid, MakerWorld customizer for Underware/Neogrid) to generate test STLs quickly
- Once a custom design is needed (non-standard dimensions, brand-specific embossing), pull from QuackWorks submodule and write a custom `.scad` in `models/organizers/`
- Commit the `.scad` source and the generated `.stl` together so the repo is self-contained

**For the equipment manifest:**
- Start with a flat `equipment/inventory.yaml` organized by zone (desk-zone, maker-zone, wall-above-desk)
- Validate syntax and schema on commit via Makefile or pre-commit hook
- Schema should enforce at minimum: `id` (slug), `name`, `category`, `status` (owned|ordered|planned|retired), `location` (zone slug)

---

## Sources

- Homebrew cask `openscad` (deprecated): https://formulae.brew.sh/cask/openscad — HIGH confidence (official); "disable date: September 1, 2026"
- Homebrew cask `openscad@snapshot` (2026.06.12): https://formulae.brew.sh/cask/openscad@snapshot — HIGH confidence (official)
- OpenSCAD CLI manual: https://files.openscad.org/documentation/manual/Using_OpenSCAD_in_a_command_line_environment.html — HIGH confidence (official)
- BOSL2 releases: https://github.com/BelfrySCAD/BOSL2/releases — HIGH confidence (GitHub releases, v2.0.745 Jun 21 2026)
- Gridfinity Rebuilt v2.0.0: https://github.com/kennetek/gridfinity-rebuilt-openscad — HIGH confidence (GitHub releases, Sep 1 2025)
- QuackWorks repo: https://github.com/AndyLevesque/QuackWorks — HIGH confidence (GitHub, "99.2% OpenSCAD")
- doratracyer/floor_plan: https://github.com/doratracyer/floor_plan — HIGH confidence (GitHub, GPL-3.0)
- openGrid world: https://www.opengrid.world/ — HIGH confidence (official project site, 28mm grid confirmed)
- Underware documentation: https://www.handsonkatie.com/underware — MEDIUM confidence (creator's site, version 2.0 confirmed)
- Neogrid overview: https://handsonkatie.com/neogrid-organise-your-big-items-with-this-free-and-open-source-system/ — MEDIUM confidence (creator's site)
- Underware MakerWorld (v2.0): https://makerworld.com/en/models/783010-underware-2-0-infinite-cable-management — MEDIUM confidence (community platform)
- Neogrid 2.0 MakerWorld: https://makerworld.com/en/models/1501061-neogrid-2-0-drawer-management-system — MEDIUM confidence (community platform)
- OpenSCAD project structure best practices: https://www.maskset.net/blog/2025/05/16/managing-openscad-projects/ — MEDIUM confidence (community blog, May 2025)
- Snapmaker organizer comparison (Gridfinity/openGrid/Multiboard/HSW): https://www.snapmaker.com/blog/3d-printed-organizers/ — MEDIUM confidence (editorial, ecosystem overview)

---

*Stack research for: The Bench — Physical Space as Code (v1 milestone)*
*Researched: 2026-06-27*
