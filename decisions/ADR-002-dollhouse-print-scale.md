# ADR-002: Doll-House Print Scale = 1:25

**Status:** Accepted

## Context

The doll-house floor plan is a 3D-printed scale model of the physical room — a tangible proof-of-work artifact that makes the "space as code" thesis legible to anyone who picks it up. Before writing a line of OpenSCAD for the floor plan, the print scale must be locked. Scale is the most consequential parameter: it determines whether the model fits the printer bed, whether printed walls are thick enough to survive handling, and whether there is room for the printed joint features required by ADR-003.

The primary printer is a **Bambu Lab A1**, with a print volume of **256 × 256 × 256 mm** (usable bed area: approximately 256 × 256 mm). The target room is approximately 3.6 m × 4.2 m (these are estimated dimensions; the exact values will be confirmed in Phase 4 measurement and updated in `params.scad`, but the scale decision must be made before modeling begins so the architecture is correct from the start).

Three candidate scales were evaluated:

| Scale | Room footprint (3.6 × 4.2 m) | Wall thickness at 150mm real wall | Fits A1 bed? | Wall printability |
|-------|-------------------------------|-----------------------------------|--------------|-------------------|
| 1:50  | 72 × 84 mm                   | 3 mm                              | Yes (easily) | OK but small; hard to read and handle |
| 1:25  | 144 × 168 mm                 | 6 mm                              | Yes (fits with margin) | Good — room for joinery features |
| 1:20  | 180 × 210 mm                 | 7.5 mm                            | Marginal for full footprint | Good, but full-floor base may not fit |

At **1:25**, a 3.6 × 4.2 m room prints as approximately **144 × 168 mm** — the entire floor plan fits on the A1 bed in a single print with room to spare. Any individual wall (up to ~168 mm at 1:25) also fits easily as a standalone print.

Wall thickness at 1:25 scales a 150 mm real wall to **6 mm printed** — well above the FDM minimum reliable wall thickness of 1.5 mm, and thick enough to accommodate the printed connector joinery specified in ADR-003. (The joint mechanism itself is deferred to Phase 6, but the 6 mm wall gives adequate material to work with.)

The AMS multi-material system on the A1 enables printing walls and the floor base in distinct colors. Combined with ADR-004's semantic color system, this means walls can carry meaning-bound brand inks — the physical model becomes a direct instantiation of the design system.

## Decision

The doll-house print scale is **1:25**. This is a Phase 1 success criterion and is locked before any `.scad` file for the floor plan is written.

`params.scad` will define:
```openscad
SCALE       = 1/25;      // doll-house print scale
// Usage: printed_dimension = real_mm * SCALE
```

All floor-plan and wall geometry derives from this single constant. The full room footprint at 1:25 fits the Bambu Lab A1 (256 × 256 mm bed) with margin. Individual walls at 1:25 fit in any orientation.

The exact joint feature-size verification (minimum connector dimension at 6 mm wall thickness) is deferred to Phase 6, where the joint mechanism will be selected and prototyped (see ADR-003).

## Consequences

**What becomes easier:**

- The entire room floor plan prints in one job on the A1. No bed-splitting, no assembly of floor sections.
- Individual walls print easily as standalone replacement pieces — a wall section can be reprinted to add shelving mount cutouts without reprinting the whole model.
- At 6 mm printed wall thickness, there is ample material for dovetail or tab-and-slot joinery features (the minimum reliable FDM joint feature is approximately 1.5–2 mm; 6 mm provides 3× margin).
- AMS color assignment at 1:25 is practical: a 6 mm wall is large enough for a clean color transition, unlike the 3 mm walls that would result from 1:50.
- The SCALE constant in `params.scad` means future room dimension updates (Phase 4 measurement) automatically propagate to print dimensions without any manual scale recalculation.

**What requires attention:**

- At 1:25, text labels and fine surface details (door swing arcs, outlet symbols) need to be no smaller than ~2 mm printed — approximately 50 mm real-world features. Sub-50 mm labels should be omitted or moved to a separate legend card rather than embossed on the model.
- The scale locks a physical constraint into the codebase before the room is measured. If the room turns out to be significantly larger than 3.6 × 4.2 m (e.g., 5 × 6 m), the floor plan footprint at 1:25 would be 200 × 240 mm — still fits the A1, but with less margin. If the room is ≥ 6.4 m in any dimension, this ADR must be revisited (the footprint would exceed 256 mm).
- Joint feature-size verification is explicitly deferred to Phase 6. The scale is locked now; whether the joint mechanism works at this scale is confirmed in Phase 6 before any floor plan STL is committed for printing.
