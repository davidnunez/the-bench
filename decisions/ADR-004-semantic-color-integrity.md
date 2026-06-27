# ADR-004: Semantic Color Integrity (Reflect, Don't Invent) + Board Boundary

**Status:** Accepted

## Context

The brand color system used in this project is not a decorative palette — it is a semantic type system. Each ink is permanently assigned a Signal Path content type:

| Ink | Signal Path type | Meaning |
|-----|-----------------|---------|
| magenta `#c63c82` | signal | a curiosity or spark worth tracking |
| aubergine `#4a2a57` | probe | hands-on exploration — where the depth lives |
| soft coral `#e59a7d` | pulse | ephemeral quick share |
| persimmon `#ec6a43` | broadcast | durable, built-to-travel share |
| amber `#d7a53a` | module | reusable operational system |
| brown `#8a5410` | cadence | recurring review rhythm |
| teal `#15807c` | component | distilled reusable insight |
| green `#2e7d52` | schematic | speculative outline composing components |

Base tones (paper `#f5efe2`, ink `#1a1820`, surface `#ede7d5`) carry no type assignment. Places (the Bench, the Board, the Rack) carry paper/cream — not a type color — because they are where the path evolves, not path stages.

Two risks arise from having a meaning-loaded color system in a hands-on build project:

**Risk 1: Decorative reuse.** A render or label uses aubergine simply because it looks good against cream, without intending to signal "probe." Once a color is used decoratively, its semantic meaning degrades and the system stops working as a wayfinding tool. Every reader who sees aubergine in the repo will correctly expect it to mean "hands-on exploration"; if it sometimes means "I just liked this color here," the signal is gone.

**Risk 2: Inventing colors.** A color is needed that doesn't exist in the system (e.g., a mode color for "electronics-maker zone"). Rather than leaving a gap, a color is invented and assigned in `tokens.yaml`. This violates the fundamental constraint: the Bench repo **reflects** the Board's brand semantics; it does not **extend** them. The Board (private vault + live Ghost site) is the source of truth. Any new color or semantic assignment must originate there, not here.

Both risks are compounded by the fact that the brand system is a moving target — it was significantly reworked in mid-2026 (pulse/broadcast split, schematic and cadence inks added, cobalt and indigo freed as unbound). `tokens.yaml` captures a pinned snapshot; it is not a live feed.

## Decision

1. **Every brand ink in this repo carries its Signal Path type meaning without exception.** An ink is never reused decoratively. If a render, label, lighting scene, or physical print uses a type color, it is because the context is an instance of that type. Aubergine means probe. Persimmon means broadcast. Always.

2. **The Bench repo reflects the Board's color semantics — it never invents them.** When a color assignment is needed and no Board value exists for it, the gap is marked `"TBD — pending Board decision"` in `tokens.yaml`. It is not filled with an invented value.

3. **Any proposed new color or semantic assignment routes back to the Board, not canonized here.** If a need emerges (e.g., a mode-specific color for the electronics-maker zone), the correct path is: propose it as a Pulse or Component back to the Board → if the Board adopts it → sync `tokens.yaml`. This is the Board boundary defined in `CLAUDE.md`: strategy and identity are read-only from the Board; insights and artifacts flow back as Pulses/Components.

4. **`design-system/tokens.yaml` is a pinned snapshot of the Board's color system.** Its provenance block names the source, the snapshot date, and the Board document. When the Board's brand changes, `tokens.yaml` is re-synced manually in v1. A `make sync-tokens` automated target is a v2 idea.

5. **The Bench's own identity color is aubergine (`#4a2a57`) on cream (`#f5efe2`)**, because The Bench is a Probe in the Signal Path framework. This is definitional, not preferential. The wordmark, repo identity elements, and primary visual signature all use this pairing.

## Consequences

**What becomes easier:**

- Every reader of the repo — and every person who encounters a printed label or render — can decode color as meaning. Aubergine in any context means "this is probe-level depth." Persimmon means "this is built to travel."
- Color decisions in future phases are constrained and therefore fast: pick the ink that matches the content type. No design debate required.
- The pinned-snapshot model makes `tokens.yaml` stable. It does not update silently when the Board changes; it updates only on deliberate `re-sync` commits, which are auditable in git history.
- Gaps are honest: a `"TBD — pending Board decision"` value in `tokens.yaml` is visible, searchable, and routes to the right decision-maker (the Board). An invented value would be invisible — it would look like a legitimate assignment.

**What requires attention:**

- **Mode colors are not type colors.** The three room modes (deep-focus / creator-filming / electronics-maker) are a different axis from Signal Path types. Assigning mode-specific colors from the type system would conflate the two axes and corrupt the semantic meaning of both. Mode-to-color mapping is deferred to Phase 5 and must route through the Board if a new ink is needed.
- `tokens.yaml` will have gaps — specifically, color assignments for uncolored terms (Bench, Board, Rack as places) are deliberately cream/paper, not typed. Any tooling that reads `tokens.yaml` must handle absent type-color keys without error.
- Cobalt (`#2f5da8`) and indigo (`#5b53b0`) are defined-but-unbound inks in `tokens.yaml` — available for future Board decisions but not assigned. They must not be used until assigned, even though they appear in the token file.
- The Board boundary means this repo cannot unilaterally decide that a new Signal Path type exists or that an existing type changes color. Any such proposal starts as a Pulse going out, not as a `tokens.yaml` edit going in.
- In v1, re-syncing `tokens.yaml` when the Board changes is a manual step. The risk is drift — `tokens.yaml` falling behind the live brand without a clear signal that it has. Mitigation: the `provenance.snapshot_date` field in `tokens.yaml` makes the snapshot age visible. A `make check-tokens-age` target that warns when the snapshot is >90 days old is a v2 idea.
