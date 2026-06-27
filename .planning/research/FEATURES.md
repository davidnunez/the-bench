# Feature Research

**Domain:** Living version-controlled physical workspace model — "space as code" + build-in-public probe
**Researched:** 2026-06-27
**Confidence:** HIGH (primary sources: PROJECT.md, REQUIREMENTS.md, aesthetic-brief.md; verified: Gridfinity/openGrid/Underware/Neogrid ecosystem via handsonkatie.com; doratracyer/floor_plan via GitHub)

---

## Feature Landscape

### Table Stakes (Must Have or the Probe Isn't Credible)

These are the features a stranger encountering the public repo expects to find. Missing any of them breaks the probe's core promise.

| Feature | Why Expected | Complexity | v1 or v2+ | Notes |
|---------|--------------|------------|------------|-------|
| Public repo spine | A "build-in-public" probe with no README/thesis is invisible — the spine IS the first artifact | LOW | v1 | README: thesis (before→alive; environment-as-provenance), identity, brand tone, back-link to governing Board Signal. Ships before room measurement. |
| Room dimensions + as-is layout (OpenSCAD model) | "Space as code" without a room model is empty rhetoric | MEDIUM | v1 | `room.scad` — measured walls, windows, doors, outlet positions. Furniture placed by name and coordinates. `params.scad` as single source of truth for all dimensions. |
| One-command render pipeline | Code that can't be executed is dead code; renders must be committable | MEDIUM | v1 | `make render` or equivalent → PNG outputs committed to `renders/`. OpenSCAD CLI invoked headlessly. Proves the model is live, not just aspirational. |
| Equipment / inventory manifest (structured data) | Without an inventory there is nothing to organize, model, or document | LOW | v1 | YAML file(s): name, location (zone), purpose, mode-tags, purchase_date, cost, link, warranty. Harvested and refreshed from the-bench-old. Zone-tagged and mode-tagged from the start. |
| Three modes represented in the model | The three-mode framing is the core value proposition of the space design | MEDIUM | v1 | Deep-focus · creator-filming · electronics-maker. Represented as zone annotations and color-coding in the OpenSCAD model — not three separate files. Mode tags also appear in the manifest. |
| Design system / brand tokens | Renders that look generic undermine the brand-loop claim (the room is a live brand asset) | MEDIUM | v1 | `design-system/tokens.yaml` (or similar): palette hex values, type choices (Archivo/Newsreader/IBM Plex Mono), OpenSCAD color constants. Two outputs: render styling AND physical bin label / signage templates. Current palette: cream `#f5efe2`, near-black `#1a1820`, terracotta `#ec6a43`, plum `#4a2a57`, magenta `#c63c82`. Supersedes old copper + electric-blue scheme. |
| ADR / decision log | Non-obvious choices (why this placement, why this product, why this version of the system) must be auditable | LOW | v1 | `decisions/ADR-NNN-*.md` format. Already established in the-bench-old; carry the practice, not the old decisions. |
| Version-controlled physical changelog | A "living model" must have a history of what changed and when | LOW | v1 start, ongoing | `CHANGELOG.md` — physical versions of the office (v1.0 = as-is documented; v1.1 = first physical change; etc.). Not just git commits — a human-readable history of physical state. |
| Pulse-ready proof-of-work mechanism | Silence is the only failure mode; the repo must *emit* shareable artifacts without a publishing pipeline | LOW | v1 | `pulses/` directory. Each phase boundary entry: rendered image + photo + brief description. Minimum weekly cadence. Format established in v1; populated every phase. Broadcasting happens outside the repo. |

---

### Differentiators (The Environment-as-Provenance Spine)

Features that make The Bench a probe worth following, not just another desk-setup repo.

| Feature | Value Proposition | Complexity | v1 or v2+ | Notes |
|---------|-------------------|------------|------------|-------|
| Environment-as-provenance framing | The genuinely original philosophical differentiator — the physical context of creation becomes part of the work's "soul" | LOW (craft, not code) | v1 | Lives in the README and in-repo framing. The Bench is the *example* of the thesis, not just a furniture-layout tool. Must not get buried as a detail. The deliberate over-engineering (lines of OpenSCAD just to place a desk) IS the point. |
| Doll-house 3D-printed scale floor plan | A physical artifact that literalizes "space as code" — the most shareable v1 proof-of-work | HIGH | v1 | Workflow: measured room → OpenSCAD room model → SVG export → doratracyer/floor_plan (or direct OpenSCAD) → STL → 3D print. Scale model of the as-is room with furniture and zones. A stranger holding it gets the concept instantly. Ships as a v1 milestone artifact. |
| Over-engineering-on-display as hook | The deliberate formalism (parametric primitives, design tokens, structured manifests, ADRs) is the content — not the enemy of shipping | LOW (philosophy, medium execution) | v1 | Every file and directory in the repo is a demonstration of the thesis. The repo structure IS the product. |
| Parametric desk accessories + cable management parts | Custom-designed, version-controlled physical objects that reinforce the "space as code" model | HIGH | v2 | OpenSCAD parts: cable clips, cord holders, monitor arm cable management, custom mount adapters. Committed alongside the room model. Each printed part has a corresponding SCad source in the repo. |
| Gridfinity organizational layer (desk + maker bench drawers) | The 42mm community standard for small-item drawer organization becomes a sub-system in the code model | HIGH | v2 | Gridfinity baseplates and custom bins modeled in OpenSCAD (CODE-04), version-controlled. Drawer dimensions → bin layout → printed parts. Desk daily-use items (STOR-04) + maker bench components (STOR-05). Community bins used where available; custom bins only where community doesn't have the right shape. |
| openGrid wall-mount layer (maker bench + desk wall) | Universal snap-fit grid for small vertical surface organization — scissors, rulers, soldering accessories, pens | HIGH | v2 | Printed tiles screwed to walls; accessories snap on. Compatible with Gridfinity and Underware. Modeled in OpenSCAD as zone overlays. Especially valuable above the maker bench (replacing ad-hoc pegboard). openGrid = CC-BY open source. |
| Neogrid drawer management for large items | Parametric connector-based system for deep drawers with larger items (tools, materials, filament supplies) | HIGH | v2 | Not fully printed (divider panels are cut from suitable material; only connectors are printed). Models the connector layout in OpenSCAD. Complementary to Gridfinity — used in drawers where Gridfinity bins are too small a unit. |
| Underware cable management (under-desk + wall) | Snap-together cable channels that route cleanly under the desk surface; compatible with openGrid | MEDIUM | v2 | Printed in PLA (standard) or transparent PETG (doubles as LED strip diffuser). Channels route every cable off the floor and hidden. Snaps onto openGrid boards. Version-controlled as an in-repo sub-system (CBLE-06). Directly improves creator-filming mode (clean desk in frame). |
| Lighting + AV/streaming control as code | Home Assistant YAML in-repo represents mode-aware scenes — not just physical wiring | MEDIUM | v2 | `automation/home-assistant/` — lighting scenes (Focus 3000K warm / Filming balanced / Maker CRI90+ / Ambient), smart plug configs, presence automation. Git-tracked. OBS scene list as data (camera positions, scene configs). Code-03, Lite-10, Auto-01–06. |
| Before→alive documentation mechanism | The structured documentation of the physical transformation is itself a content artifact | LOW | v1 starts it, v2+ populates it | Structured: `pulses/` for weekly artifacts, `CHANGELOG.md` for physical versions, `photos/` for authentic WIP photography (no AI imagery). Each phase boundary produces a pulse entry. The "before" state is documented at v1; "alive" is ongoing. |
| In-repo bin label + physical signage templates | The design system crosses the digital/physical boundary — the same brand tokens that color renders also print on bin labels and zone signage | MEDIUM | v2 | SVG templates using brand palette and IBM Plex Mono typeface. Printed labels for Gridfinity bins, openGrid accessories, zone signage. Connects the "living model" to the physical space in a visible way. |

---

### Anti-Features (Explicitly NOT Building)

Features to deliberately exclude — either because they compromise the probe, invert the priority, or are the failure mode of the old attempt.

| Anti-Feature | Why It Seems Attractive | Why Not | What to Do Instead |
|--------------|------------------------|---------|-------------------|
| Broadcasting / publishing pipeline | Seems like the natural output of a "build in public" project | Out of scope by design — the repo's obligation is to *emit* pulse-ready artifacts; broadcasting is A4/A5 (Public Explorer/Publisher) outside this repo. Building it here re-buries the deliverable. | `pulses/` directory emits shareable artifacts; broadcasting happens outside the repo. |
| RGB / gaming aesthetics | Cheap way to add visual interest to photos and renders | Conflicts directly with builder/explorer brand identity. Reads as gaming setup, not maker studio. Undermines on-camera look. | Bias lighting (dimmable, warm) behind monitor; warm practical lights as room fill. |
| AI-generated imagery | Fast way to produce renders and concept art | Violates the "environment-as-provenance" philosophical spine — if the space is authentic, its documentation must be authentic too. No AI renders. | Authentic WIP photography only. OpenSCAD renders for technical visualization. |
| Rendering the model to davidnunez.com | Natural extension — if the room is a brand asset, it should appear on the site | Not v1 scope. Publishing to the live site is handled outside this repo. Pursuing it inverts the priority (infra/plumbing over shipping artifacts). | GitHub repo IS the public surface for v1. Site integration is a future phase when the content is proven. |
| Full Signal Path machinery in-repo | The Bench is part of the Signal Path framework, so it feels right to bring it all in | The Board (Obsidian vault) is the system of record for strategy, identity, and priorities. Re-deriving them here creates drift and sprawl. | Identity + brand tokens + a back-link to the governing Board Signal. Strategy is read-only from the Board. |
| Waterfall "finish all planning before shipping" gate | Thorough planning feels responsible | The old v0 failure mode. It buried "space as code / shareable content" at Phase 10 and stalled at 4% behind a measurement gate. | Invert: public spine ships first. Room measurement enables the model but doesn't gate the probe. |
| "Live in it for weeks" marination before optimizing | Seems empirically sound — use the space before redesigning it | Explicit anti-pattern in PROJECT.md. Creates a long analysis gate that delays proof-of-work. The old repo's kill shot. | Rapid iteration. Measure, model, print, install, photograph, pulse. Don't wait for a marination period. |
| Physical redesign execution in v1 | The whole point is a redesigned office, so why not start building? | v1 = model the "before." Physical redesign is v2+. Trying to do both in v1 inflates scope and recreates the old waterfall. | v1 ships the model, the doll-house, the spine, the manifest. v2 uses those as inputs to the physical redesign. |
| Green screen backdrop | Easy way to control the filming background | Practical layered background is higher quality, zero-setup, no chroma spill, and shows the real space. | Curated physical background with depth layers (near/mid/far: desk surface → shelving → wall treatment). |
| Resin 3D printer in office | Better print quality for detail work | Fumes are hazardous in an enclosed space. FDM only in office; resin to basement if ever. | FDM (Bambu or Prusa) in office. Resin deferred to v2 basement extension if warranted. |
| Full audio production suite | Rack mount interface, multi-XLR, monitor speakers | Overkill for YouTube/Zoom. Adds significant complexity and cost with minimal return. | USB mic sufficient. Boom-mounted. Upgrade only when USB proves the limiting factor. |
| Custom ESPHome firmware everywhere | Maximum control over every smart device | Creates ongoing maintenance burden for devices that off-the-shelf smart plugs handle fine. | Off-the-shelf smart plugs and lights. Reserve ESPHome for sensors unavailable commercially (mmWave presence sensor is the exception). |
| Home lab server rack | Feels right alongside a maker bench | HA runs on a single RPi or mini PC. No server rack needed. Disproportionate to the scope. | Single-board HA host. Scale only if actual services demand it. |
| Acoustic treatment (v1) | Important for audio quality in creator-filming mode | Not a v1 constraint — the current space ships audible content. Acoustic panels require significant wall real estate that interacts with camera backgrounds. | Defer to v2. Plan panel placement to coordinate with camera background aesthetics. |
| Motorized window blinds | Smart home feel | High cost, minimal return vs. manual blinds. Doesn't improve any of the three modes meaningfully. | Manual blinds. Defer or skip entirely. |

---

## Feature Dependencies

```
[Public repo spine (README + thesis)]
    └──establishes credibility for──> [All pulse artifacts]
    └──must ship before──> [Room measurement gate]

[Room measurement]
    └──enables──> [OpenSCAD room model]
                      └──enables──> [One-command render pipeline]
                      └──enables──> [Three-mode zone representation]
                      └──enables──> [Doll-house floor plan print]
                                        └──requires──> [SVG export or OpenSCAD → STL pipeline]
                                        └──requires──> [3D printer available]

[Equipment / inventory manifest]
    └──enables──> [Zone-tagged inventory view]
    └──informs──> [Gridfinity layout planning (v2)]
    └──informs──> [Neogrid drawer sizing (v2)]

[Design system / brand tokens]
    └──enables──> [Consistent render styling]
    └──enables──> [Physical bin label templates (v2)]
    └──enables──> [Physical zone signage (v2)]

[One-command render pipeline]
    └──enables──> [Committed renders as pulse artifacts]
    └──enables──> [Parametric desk accessories (v2)]

[Gridfinity physical install (v2)]
    └──requires──> [Equipment manifest → know what to store]
    └──requires──> [OpenSCAD Gridfinity models (CODE-04)]
    └──requires──> [Maker bench installed (MAKE-01)]
    └──requires──> [Drawer dimensions measured]

[openGrid wall install (v2)]
    └──requires──> [Zone walls identified in room model]
    └──enables──> [Underware attachment to openGrid boards]
    └──enables──> [Small vertical-surface tool access at maker bench]

[Underware cable management (v2)]
    └──requires──> [openGrid boards OR direct desk-mount surface]
    └──enhances──> [Creator-filming mode (clean desk in frame)]
    └──enhances──> [Deep-focus mode (zero cable distraction)]
    └──enables──> [LED diffuser strips (transparent PETG channels, v2)]

[Home Assistant mode scenes (v2)]
    └──requires──> [Smart plugs on all equipment zones]
    └──requires──> [Smart bulbs with color temperature control]
    └──requires──> [HA config in git (CODE-03)]
    └──enables──> [One-tap mode switching (deep-focus/filming/maker/ambient)]

[Creator-filming mode (v2 physical)]
    └──requires──> [Key light + fill light + hair light]
    └──requires──> [Eye-level camera on arm]
    └──requires──> [Curated background depth layers]
    └──enhances──> [Underware cable management (clean frame)]

[Pulse-ready proof-of-work mechanism]
    └──requires──> [One-command render pipeline (for render artifacts)]
    └──requires──> [WIP photography (for photo artifacts)]
    └──feeds──> [CHANGELOG.md physical versions]
```

### Dependency Notes

- **Public spine must ship before room measurement gate:** The old v0 stalled because it put space-as-code at Phase 10. The spine ships immediately; room measurement is a dependency only for the model, not for the probe's public existence.
- **Doll-house requires room model, not the other way around:** Model the room first in OpenSCAD, then derive the doll-house STL. The doll-house is a rendered artifact of the model, not a precondition.
- **Design system is a v1 dependency for renders:** Without brand tokens, the renders are unstyled. Tokens are also the bridge to physical bin labels in v2.
- **Gridfinity/openGrid/Neogrid/Underware all require the manifest:** You cannot plan a Gridfinity layout without knowing what you're storing. Manifest → layout planning → OpenSCAD models → printing → install. Skip this order and you print the wrong bins.
- **Underware is post-openGrid (or standalone):** Underware snaps onto openGrid boards, so openGrid boards must be mounted first if using the integrated approach. Underware can also be standalone desk-mounted channels.
- **HA scenes require physical smart devices:** You cannot write mode-scene automation until the lights and plugs are physically installed and HA is running.

---

## MVP Definition

### v1: "Before" + Spine + Doll-House (Launch With)

The minimum that validates the probe as credible and build-in-public-worthy.

- [ ] **Public repo spine** — README, thesis (before→alive; environment-as-provenance), brand tone, back-link to Board Signal. Ships first, before room is measured.
- [ ] **Room model as-is** — OpenSCAD parametric model of measured room with furniture as-is and three zones labeled.
- [ ] **One-command render pipeline** — `make render` → committed PNG outputs. At least a top-down floor plan view and a perspective view.
- [ ] **Equipment / inventory manifest** — Refreshed YAML from the-bench-old; zone-tagged, mode-tagged.
- [ ] **Design system / brand tokens** — `design-system/tokens.yaml` (palette + type); OpenSCAD color constants; committed once, used in every render.
- [ ] **Doll-house 3D-printed floor plan** — The tangible v1 artifact. Scale model of as-is room. SVG → OpenSCAD → STL → printed. Photo in pulse log.
- [ ] **Three modes in the model** — Zone annotations in OpenSCAD; mode tags in manifest.
- [ ] **Pulse-ready mechanism established** — `pulses/` directory format defined and first entry committed (the doll-house print = v1 pulse artifact).
- [ ] **ADR format established** — At least one ADR committed (the parametric-room-as-code decision itself).
- [ ] **CHANGELOG.md** — v1.0 entry = as-is state documented.

### v2: Physical Redesign (Add After v1 Validated)

Triggered once the v1 model, spine, and doll-house are shipped and the probe has a public audience.

- [ ] **Gridfinity desk layer** — Custom OpenSCAD bin models, physically printed and installed at desk drawers. Layout planned from manifest.
- [ ] **openGrid wall layer** — Tiles mounted at maker bench (and optionally desk wall). Small tools accessible by reach.
- [ ] **Neogrid drawer management** — Deep drawer dividers for tools/materials. Connectors printed; panels cut to size.
- [ ] **Underware cable management** — Under-desk and on-wall cable channels. PETG if LED diffusion wanted. snapped to openGrid or standalone.
- [ ] **Physical bin label templates** — SVG templates using brand tokens + IBM Plex Mono. Applied to all Gridfinity bins and openGrid accessories.
- [ ] **Home Assistant mode scenes in git** — `automation/home-assistant/` YAML. Focus/Filming/Maker/Ambient. One-tap switching.
- [ ] **Creator-filming mode physical** — Key + fill + hair light installed, eye-level camera, curated background curated, bias lighting behind monitor.
- [ ] **Maker bench setup** — ESD mat, soldering station, PSU, task lighting CRI90+, fume extractor evaluated.
- [ ] **Ergonomics upgrade** — Chair, monitor arm at eye level, keyboard/mouse at elbow height, standing presets saved.
- [ ] **mmWave presence sensor** — Static presence detection for reliable auto-off. HA config in git.

### Future Consideration (v3+)

- [ ] **Basement extension** — Maker zone downstairs integrated into same manifest and HA system.
- [ ] **Acoustic treatment** — Panel placement coordinated with camera background (v2 deferred).
- [ ] **Dedicated DSLR/mirrorless** — Upgrade from USB/webcam when that proves the limiting factor.
- [ ] **Advanced AV** — Video switcher, multi-camera OBS scenes.

---

## Feature Prioritization Matrix

| Feature | Probe Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| Public repo spine | HIGH | LOW | P1 |
| Environment-as-provenance framing | HIGH | LOW | P1 |
| Room model as-is (OpenSCAD) | HIGH | MEDIUM | P1 |
| One-command render pipeline | HIGH | MEDIUM | P1 |
| Equipment / inventory manifest | HIGH | LOW | P1 |
| Design system / brand tokens | HIGH | MEDIUM | P1 |
| Doll-house 3D-printed floor plan | HIGH | HIGH | P1 |
| Three modes in model | HIGH | LOW | P1 |
| Pulse-ready mechanism | HIGH | LOW | P1 |
| ADR / decision log | MEDIUM | LOW | P1 |
| Gridfinity organizational layer | HIGH | HIGH | P2 |
| Underware cable management | HIGH | MEDIUM | P2 |
| openGrid wall layer | HIGH | HIGH | P2 |
| Neogrid drawer management | MEDIUM | HIGH | P2 |
| HA mode scenes in git | HIGH | MEDIUM | P2 |
| Creator-filming mode physical | HIGH | HIGH | P2 |
| Parametric desk accessories | MEDIUM | HIGH | P2 |
| Physical bin label templates | MEDIUM | MEDIUM | P2 |
| Maker bench setup | HIGH | HIGH | P2 |
| Ergonomics upgrade | MEDIUM | MEDIUM | P2 |
| Acoustic treatment | MEDIUM | HIGH | P3 |
| Basement extension | LOW | HIGH | P3 |
| Dedicated DSLR upgrade | MEDIUM | MEDIUM | P3 |

**Priority key:**
- P1: Must have for v1 launch (probe credibility)
- P2: Physical redesign features — v2 scope; high value when the time comes
- P3: Defer until v2 is shipped and validated

---

## Prior Art / Analogous Projects

| Project | What They Do | What The Bench Does Differently |
|---------|-------------|--------------------------------|
| **khuedoan/homelab** et al. | Versioned infrastructure-as-code for digital homelab (Kubernetes, Terraform, Ansible) | Models physical space, not just digital services. Build-in-public probe, not just personal ops. |
| **doratracyer/floor_plan** (GitHub) | SVG → OpenSCAD → printable 3D floor plan generator | Starting point for doll-house artifact; The Bench adds living-model layer, organizational systems, and the philosophical/build-in-public spine. |
| **MakerWorld Generative 3D Floor Plans** | AI-assisted 2D image → print-ready STL | Alternative path to doll-house STL; The Bench uses code-first (SVG/OpenSCAD) to stay version-controllable. |
| **handsonkatie.com home organisation** | The Gridfinity/openGrid/Underware/Neogrid ecosystem — open-source parametric organization | Sub-system within The Bench. The Bench adds room-level context, OpenSCAD modeling of layouts, and version-controlled bin designs. |
| **YouTube desk setup tours** (MakerStations, etc.) | Great physical content; ephemeral, unversioned, no code | The Bench adds version control, parametric models, structured data, and proof-of-work discipline. |
| **Autodesk Tandem / Azure Digital Twins** | Enterprise-grade digital twin platforms for buildings | Enterprise cloud-dependent; The Bench is git-native, personal-scale, and build-in-public. No cloud vendor required. |
| **Adam Savage's Undisclosed Location** | Inspirational workshop identity and tool organization | The Bench makes the documentation process the artifact, not just the finished space. No repo, no code, no provenance trail. |

---

## Organizational Ecosystem Detail

The Gridfinity/openGrid/Underware/Neogrid ecosystem (handsonkatie.com) is the physical implementation layer of "space as code" for storage. Each system covers a different surface/item-size combination:

| System | Surface | Item Size | The Bench Use Case | v1 or v2+ |
|--------|---------|-----------|-------------------|-----------|
| **Gridfinity** (42mm community standard) | Drawers, desk surface, shelves | Small items (tools, cables, nozzles, components, pens) | Desk daily-use items (STOR-04); maker bench electronics components (STOR-05) | v2 |
| **openGrid** (CC-BY universal grid, snap-fit) | Walls — both horizontal desk and vertical wall | Small-medium items (scissors, rulers, tape, soldering accessories) | Above maker bench (replaces ad-hoc pegboard); desk wall | v2 |
| **Neogrid** (parametric connector-based) | Deep drawers | Large items (tools, materials, filament, craft supplies) | Deep storage at maker bench or storage shelving | v2 |
| **Underware** (snap-together cable channels) | Under desk surface and on walls | Cables, power bricks, LED strips | Under-desk cable routing; LED diffuser channels (transparent PETG); snaps to openGrid | v2 |
| **French Cleat** | Walls — heavy load | Large/heavy tools, power tools, shelves | Above maker bench for heavy tool mounting | v2 (evaluate vs openGrid per item) |

**Key insight for roadmap:** All five systems require knowing what you're storing (manifest) and where you're storing it (room model + zone assignments) before printing. The manifest and room model (v1) are pre-conditions for ALL organizational system work (v2). Do not print bins until you know what goes in them.

**OpenSCAD integration:** Every custom Gridfinity insert, openGrid tile/accessory, and Underware channel configuration is committed to the repo as an `.scad` file (CODE-04). Community-standard STLs are referenced (linked, not committed) rather than vendored. This keeps the repo as a model of the custom decisions, not a binary STL archive.

---

## Three Modes as Concrete Features

### Deep-Focus (WFH / Zoom)
**v1 (model):** Zone annotated in OpenSCAD; deep-focus items tagged in manifest (primary monitor, keyboard, mouse, laptop, desk lamp, noise-cancelling headphones, webcam).
**v2 (physical):** Ergonomics baseline (ERGO-01–06); Underware cables hidden; Gridfinity desk daily-use items at arm's reach; HA Focus lighting scene (warm 3000K, minimal distraction); smart plugs off for non-focus devices; mmWave presence auto-triggers.

### Creator-Filming (YouTube / talking-head / desk demos)
**v1 (model):** Camera sightlines represented in OpenSCAD (viewing angles, background layer depth); filming zone annotated.
**v2 (physical):** Eye-level camera on arm (FILM-01); three-point lighting installed (key at 45°, fill, hair light — LITE-02–04); OBS integration for scene switching (FILM-05); boom-mounted microphone (FILM-03); curated background with depth layers (near desk surface / mid shelving / far wall — FILM-02); HA Filming lighting scene (balanced color temp, bias lighting dimmable); zero cables in frame (Underware).

### Electronics-Maker (soldering / 3D-print / light assembly)
**v1 (model):** Maker bench zone annotated; maker items tagged in manifest (soldering station, 3D printer, PSU, ESD mat, components).
**v2 (physical):** Dedicated maker bench separate from desk (MAKE-01); ESD mat grounded (MAKE-02); soldering station (MAKE-04); 3D printer calibrated on stable surface (MAKE-05); openGrid above bench (MAKE-09); Gridfinity bins for components (STORE-05); task lighting CRI90+ (LITE-06); fume extractor evaluated (MAKE-10); isolated power circuit for printer (CBLE-07); HA Maker scene (bright, high CRI, all equipment plugs on).

---

## Sources

- `/Users/davidnunez/src/the-bench/.planning/PROJECT.md` — PRIMARY: probe framing, v1 scope, out-of-scope, constraints, brand
- `/Users/davidnunez/src/the-bench-old/.planning/REQUIREMENTS.md` — Reference checklist: FOUND/LITE/CBLE/ERGO/MAKE/STOR/FILM/AUTO/AEST/CODE categories
- `/Users/davidnunez/src/the-bench-old/docs/aesthetic-brief.md` — Reference: anti-patterns, on-camera considerations, material direction (palette superseded by PROJECT.md)
- [Hands On Katie — Home Organisation System](https://www.handsonkatie.com/home-organisation) — Gridfinity/openGrid/Underware/Neogrid ecosystem overview (HIGH confidence — official source)
- [Hands On Katie — openGrid](https://www.handsonkatie.com/opengrid) — openGrid surfaces, cross-system compatibility, openConnect adapters (HIGH confidence)
- [Hands On Katie — Underware](https://www.handsonkatie.com/underware) — Cable management channels, LED diffuser capability, openGrid integration (HIGH confidence)
- [GitHub — doratracyer/floor_plan](https://github.com/doratracyer/floor_plan) — SVG → OpenSCAD → printable 3D floor plan generator (HIGH confidence — primary code reference for doll-house artifact)
- [MakerWorld — Generative 3D Floor Plans](https://makerworld.com/en/models/2746484-generative-3d-floor-plans) — Alternative/complementary path to doll-house STL (MEDIUM confidence)
- [Gridfinity Layout Tool — Software Comparison](https://gridfinitylayouttool.com/gridfinity-software) — OpenSCAD vs online generators for Gridfinity (MEDIUM confidence)
- WebSearch: homelab-as-code repos (khuedoan, clearlybaffled, mkuthan) — Prior art for digital infrastructure-as-code; confirms gap in physical-space modeling (MEDIUM confidence)

---

*Feature research for: The Bench — living version-controlled physical workspace model*
*Researched: 2026-06-27*
