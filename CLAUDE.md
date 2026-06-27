<!-- GSD:project-start source:PROJECT.md -->
## Project

**The Bench**

The Bench is a living, version-controlled model of my physical home office/studio — "space as code" — built in public as a **Probe** in my Signal Path framework. This repo is the *execution arm*: it models the lived-in space (furniture layout, parametric desk accessories / cable organizers / shelving, the electronics workbench, lighting + AV/streaming control) as a *running model of* the space, not a one-time renovation plan, and drives the physical redesign over successive milestones.

The defining inversion: the **public / meta / Signal-Path layer leads; the physical build hangs off it.** The ultimate deliverable is the redesigned physical Bench; the artifact *along the way* is the documented process — **before → "alive."** The deliberate over-formalization (lines of OpenSCAD just to place a desk) is the point and the hook, not a bug.

**Core Value:** A stranger encountering the public repo sees a real human turning his environment into a reproducible, expressive, lovingly over-engineered system — and **wants to follow along.** The repo + public artifact are the spine; the office is what they model.

*Prioritization rule when tradeoffs arise:* ship an expressive, public proof-of-work over perfecting private infrastructure. **Silence is the only failure mode.**

### Constraints

- **Tech stack**: OpenSCAD is the "space as code" engine — `brew install --cask openscad@snapshot` (**not yet installed**; the `@snapshot`/dev release is required — the bare `openscad` cask installs the deprecated 2021.01 build, which the **QuackWorks** organizer library will not run on). Plus **BOSL2** + the **QuackWorks** submodule (Gridfinity / openGrid / Underware / Neogrid). Optional `yamllint` + `check-jsonschema` for the manifest. Present: Node 22, git, python3.
- **Brand**: palette = warm cream `#f5efe2` + near-black `#1a1820` + terracotta `#ec6a43` + plum `#4a2a57` + magenta pop `#c63c82`; type = Archivo (display) · Newsreader (serif body) · IBM Plex Mono (labels). **Supersedes** the March copper + electric-blue scheme. **No AI imagery** — authentic WIP photography only.
- **Cadence**: at least **weekly** pulse-ready proof-of-work. Heaviness is a feature; *silence* is the failure mode.
- **Physicality**: real-world delays (3D-print times, shipping, paint drying, physically sorting cable bins) are *legitimate* scheduling inputs — but must **not** inflate into long marination/analysis gates. Bias to rapid, prolific proof-of-work. **Not a 3-year project.**
- **Scope guard**: a contained side-rehearsal — must not sprawl into or displace primary income work, nor "open all the channels" at once.
- **Board boundary**: strategy/identity/priorities are read-only from the Board; insights/artifacts flow *back* to the Board (as Pulses/Components).
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

## Recommended Stack
### Core Technologies
| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| OpenSCAD (snapshot) | 2026.06.12 | Primary modeling engine: room shell, furniture primitives, floor plan generation, STL export | The only scriptable, plain-text solid modeler in the 3D printing ecosystem. `.scad` files are fully git-diffable and version-controllable — this is the entire point of the project. Snapshot required (not stable 2021.01) for Manifold backend and QuackWorks compatibility. |
| BOSL2 | v2.0.745 (Jun 2026) | Advanced OpenSCAD shape library | Required dependency for QuackWorks (Underware, openGrid, Neogrid). Also provides attachment system, threads, precision geometry, and 2D shape primitives needed for furniture modeling beyond basic boxes. |
| Gridfinity Rebuilt (kennetek) | v2.0.0 (Sep 2025) | Parametric Gridfinity bins and baseplates | The canonical open-source OpenSCAD implementation of Gridfinity. Pure parametric: width, length, height, compartments, magnets, scoops are all parameters. Most widely used, most community add-ons target it. |
| QuackWorks (AndyLevesque) | `main` branch | Unified source for Underware, openGrid, Neogrid 2.0, Deskware, Multiconnect | Single repo containing 99.2% OpenSCAD for all four organizer systems the project requires. BOSL2 is its only external dependency. Requires OpenSCAD developer release. |
| doratracyer/floor_plan | `main` branch | SVG → 3D-printable doll-house floor plan conversion | OpenSCAD-based tool that consumes standardized SVGs (walls as line paths, doors/windows as rectangles) and emits STL. GPL-3.0, print-ready with parametric wall heights and door/window sizing. This is the doll-house print path. |
### Supporting Libraries and Tools
| Library / Tool | Version | Purpose | When to Use |
|----------------|---------|---------|-------------|
| yamllint | current pip | YAML syntax and style linting | In `make validate` and pre-commit; catches malformed YAML before schema check |
| check-jsonschema | current pip | Validate equipment manifest YAML against JSON Schema | After yamllint; enforces required fields, types, enum values in `equipment/` manifests |
| python3 (present) | 3.x (present) | Run yamllint and check-jsonschema; generate design-system tokens | Already installed; no new runtime required |
| Node 22 (present) | 22.x (present) | `npm run` wrappers over Make targets; potential future JSON generation from YAML manifest | Thin glue layer — keep logic in Makefile, use npm scripts only as discoverable shortcuts |
| git submodules | — | Pin BOSL2, Gridfinity Rebuilt, QuackWorks as versioned dependencies | All three libraries are pulled as submodules into `models/lib/`; locks revision per repo commit |
### Development Tools
| Tool | Purpose | Notes |
|------|---------|-------|
| GNU Make | Build pipeline: render PNGs, export STLs, validate YAML, clean artifacts | `make renders` triggers all OpenSCAD CLI calls; output is committed PNG/SVG. Single `Makefile` at repo root. |
| OpenSCAD CLI (`--camera`, `--projection o`, `--imgsize`) | Headless rendering of committed visual artifacts | Top-down floor plan: `--camera 0,0,0,0,0,0,5000 --projection o --autocenter --viewall`. Perspective: `--camera 0,-500,1500,45,0,0,3000 --projection p`. |
| OpenSCAD `projection(cut=false)` | Extract 2D floor plan from 3D room model | Wrapping the 3D shell in `projection()` and exporting SVG gives a diff-able flat floor plan without a separate 2D model. |
| `OPENSCADPATH` env variable | Library resolution without hardcoded paths | Set in Makefile: `export OPENSCADPATH=$(PWD)/models/lib` so `use <BOSL2/std.scad>` resolves regardless of machine |
| pre-commit (optional) | Run yamllint + check-jsonschema on every commit | Add as a lightweight guardrail; not required for v1 |
## Parametric Physical-Organization Ecosystem
### Gridfinity
### openGrid
### Underware
### Neogrid 2.0
## Doll-House Floor Plan Print Path
## Design System in OpenSCAD
## Installation
# OpenSCAD: use @snapshot cask, NOT bare openscad cask
# The bare cask installs 2021.01 (deprecated, disable date Sep 1 2026)
# @snapshot installs 2026.06.12 with Manifold backend
# After install: enable Manifold in Preferences > Advanced > Backend: Manifold
# This reduces render time from minutes to seconds on complex models
# Libraries as git submodules (run once after cloning)
# Update all submodules
# YAML validation (Python tools, python3 is present)
# Node is already present (22.x); no additional npm packages required for v1
## Recommended Project Structure
## Makefile Render Pipeline Pattern
# Top-down orthographic floor plan
# 2D SVG floor plan (projection of 3D model)
# Perspective view
# STL for doll-house print
# YAML validation
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
## Version Compatibility
| Component | Compatible With | Notes |
|-----------|-----------------|-------|
| QuackWorks main | OpenSCAD dev release (2026.x) ONLY | README explicitly states "the regular release will not work" — this means 2021.01 stable is insufficient |
| BOSL2 v2.0.745 | OpenSCAD 2021.01+ (2026.x dev preferred) | Requires function literals from 2021.01; works better with dev snapshots |
| Gridfinity Rebuilt v2.0.0 | OpenSCAD 2021.01+, dev snapshot preferred | Use dev snapshot for fast Manifold rendering; 2021.01 works but CGAL rendering is slow |
| doratracyer/floor_plan main | OpenSCAD (any version supporting `import()` for SVG) | Uses `import()` for SVG; available in 2021.01+. Dev snapshot renders faster. |
| check-jsonschema | python3 3.8+ | Pure Python; no version conflicts expected |
| yamllint | python3 3.8+ | Pure Python; no version conflicts expected |
## Stack Patterns by Variant
- Use Makefile targets with `openscad --camera ... --projection o` for floor plan and `--projection p` for perspective
- Commit renders to `renders/` directory — they are build artifacts but committing them makes "the repo always shows the current state" without requiring a build step to see it
- Camera parameters need tuning once per view; thereafter they are stable
- Before room dimensions are measured: create a placeholder model with estimated dimensions; the print demonstrates the toolchain, not the final room
- After measurement: update `params.scad` → re-run `make stl` → reprint
- Scale to fit printer bed: at 1:75 scale, a 3.6m × 4.2m room prints as 48mm × 56mm (very small, fits on any bed but hard to read); at 1:50 it's 72mm × 84mm (more legible); at 1:25 it's 144mm × 168mm (requires large bed or split into sections)
- Use web generators (Perplexing Labs for Gridfinity/openGrid, MakerWorld customizer for Underware/Neogrid) to generate test STLs quickly
- Once a custom design is needed (non-standard dimensions, brand-specific embossing), pull from QuackWorks submodule and write a custom `.scad` in `models/organizers/`
- Commit the `.scad` source and the generated `.stl` together so the repo is self-contained
- Start with a flat `equipment/inventory.yaml` organized by zone (desk-zone, maker-zone, wall-above-desk)
- Validate syntax and schema on commit via Makefile or pre-commit hook
- Schema should enforce at minimum: `id` (slug), `name`, `category`, `status` (owned|ordered|planned|retired), `location` (zone slug)
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
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
