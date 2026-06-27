# ADR-003: Modular Doll-House: Floor Base + Swappable Walls

**Status:** Accepted

## Context

ADR-002 locked the 1:25 print scale, which means the full room floor plan fits on a single Bambu Lab A1 print bed. The next structural question is how the doll-house model decomposes — specifically, whether it is a single monolithic print or a set of joinable parts.

A monolithic floor-plan model (floor + walls printed together as one piece) is the simplest first implementation but has a critical limitation: any change to the room layout or wall configuration requires reprinting the entire model. Since the thesis of this project is "space as code" — an iterative, version-controlled physical object — a monolithic model directly contradicts the probe's core value. A wall with new shelving mounts, a door swing correction, or a partition addition should be expressible as "reprint one wall panel."

The doll-house model must therefore be *composable* from the start. The joint mechanism that connects wall panels to the floor base is a separate, dependent decision: the correct mechanism (dovetail slot, tab-and-slot, friction fit, snap-fit, etc.) depends on minimum printable feature size at 6 mm wall thickness, AMS color-change constraints, and the specific printer's dimensional accuracy — all of which require a physical prototype to verify. That mechanism decision is deferred to Phase 6.

**What this ADR does decide:** the *architecture* — that the doll-house decomposes into a floor/base + individual swappable walls — and the *consequence for Phase 2* modeling: `shell.scad` must be built as composable wall modules from the start, not as a monolithic shell that is later refactored.

The refactoring cost matters. If Phase 2 builds a monolithic `shell.scad` (floor + walls as one `linear_extrude` from a single polygon), changing it to a composable module architecture in Phase 6 requires rewriting the core room geometry. If Phase 2 builds composable wall modules from day one — each wall as its own module accepting a connector geometry parameter — the Phase 6 work is adding connector geometry to existing modules, not restructuring them. The architecture decision must precede the implementation.

## Decision

The doll-house physical model decomposes into:

1. **A floor base** — prints flat; contains the room footprint outline, door thresholds, any floor-level features. Serves as the reference plane all walls mount to.
2. **Individual swappable wall panels** — each exterior wall (and any significant interior partition) is a separate printed part that attaches to the floor base via printed connectors. Reprinting one wall panel updates that section of the physical model without affecting others.

`shell.scad` (to be created in Phase 2) must implement this decomposition as **composable wall modules** from the start:

```openscad
// Correct architecture (composable from day 1)
module floor_base() { ... }
module wall_north(connector_female=true) { ... }
module wall_south(connector_female=true) { ... }
module wall_east(connector_female=true) { ... }
module wall_west(connector_female=true) { ... }

// Incorrect architecture (monolithic — do not do this)
// module room_shell() { linear_extrude(...) polygon([...]); }
```

The `connector_female` parameter (or equivalent) is a placeholder geometry stub in Phase 2. The actual connector profile is filled in when the Phase 6 joint mechanism is selected. The stub must be present so Phase 6 does not require a structural refactor.

The joint *mechanism* — the specific geometry of the connector (dovetail vs. tab-and-slot vs. snap-fit vs. other) — is explicitly **not decided here**. It is deferred to Phase 6, where a physical prototype will verify the chosen geometry against the printer's dimensional accuracy at 6 mm wall thickness.

## Consequences

**What becomes easier:**

- The physical doll-house is a living, version-controlled object. Reprinting one wall is a `make stl WALL=north` invocation, not a full reprint.
- Phase 2 implements the correct architecture without needing to know the connector geometry — the stub parameter keeps the structure clean.
- Phase 6 can add connector geometry to existing wall modules rather than restructuring `shell.scad`. The architectural refactoring cost is paid now (zero cost — it's the first implementation) rather than in Phase 6 (high cost — would touch every wall module).
- Wall panels can be printed in different AMS colors, making color-by-zone assignments (deferred to Phase 5) physically realizable in the model itself.
- Individual wall replacements enable rapid iteration: "add a bracket notch to the north wall" is a 20-minute reprint, not a full rebuild.

**What requires attention:**

- **Joint mechanism deferred to Phase 6.** The connector profile between wall panels and the floor base is not decided here. Phase 6 will prototype, verify, and commit the mechanism as a Phase 6 deliverable. Do not reopen this sub-decision before Phase 6.
- The `connector_female` stub parameter in Phase 2 wall modules must be clearly documented as a placeholder (a `// PHASE-6-STUB` comment in `shell.scad`) so it is not accidentally instantiated with placeholder geometry that looks complete but does not interlock.
- The floor base serves as the registration plane for all walls. Its perimeter geometry must be accurate to the room dimensions locked in `params.scad`; walls reference the base edge for their position. Any change to room dimensions flows through `params.scad` and the base geometry automatically — no hardcoding of dimensions in wall modules.
- "Swappable" requires that connector geometry is consistent across all wall-to-floor joints. Phase 6 must define a single connector profile used throughout, not per-wall custom joints. Inconsistent joint geometry would make the model non-composable in practice.
