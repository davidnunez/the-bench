# Phase 1: Public Spine + Design System + ADRs - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-27
**Phase:** 1-Public Spine + Design System + ADRs
**Areas discussed:** README shape & "alive" hook, License model, Label SVG (subject & generation), Doll-house scale + printer (ADR-002), plus emergent: semantic color integrity, modular doll-house walls, uncolored Signal Path terms

---

## README shape & "alive" hook

| Option | Description | Selected |
|--------|-------------|----------|
| Manifesto cold-open | Lead with the idea/thesis; label SVG below | |
| Show-the-artifact first | Lead with the label SVG / swatch strip | |
| Over-engineering joke first | Lead with "40 lines to place a desk" | |

**User's choice:** Reframed the premise. Nobody follows commit-by-commit; people hit the repo later when more rendered; "it exists at all" is the signal. → A **genuine conventional GitHub README** with a tight thesis section up top, in David's voice, with wit. A casual visitor should feel something unconventional is happening *and* a nod to standards.
**Notes:** User asked me to scan `~/Ideaverse` + `~/src/davidnunez.com.ghost` for voice. Dispatched an Explore agent; surfaced `branding-brief.md` as the voice authority ("curious veteran"; lead-with-the-made-thing; no guru-fluff/purple prose). Captured as canonical ref. The "no render on day one" worry was retired as moot.

---

## License model

| Option | Description | Selected |
|--------|-------------|----------|
| MIT, whole repo | One file, maximally generous, incl. brand/photos | ✓ |
| Dual: MIT code + CC-BY content | Code MIT, creative/brand CC-BY (attribution) | |
| MIT code + brand/photos reserved | Code MIT, visual identity all-rights-reserved | |

**User's choice:** MIT, whole repo.
**Notes:** Simplest, most generous, on-brand for "be a useful example, invite don't pitch."

---

## Label SVG — generation approach

| Option | Description | Selected |
|--------|-------------|----------|
| Generated via `make labels` | Script reads tokens.yaml → emits SVG (real pipeline) | ✓ |
| Hand-authored SVG | Hand-write once, cite token source | |
| Hand-author now, stub `make labels` | Commit by hand + placeholder target | |

**User's choice:** Generated via `make labels` (real generator).
**Notes:** Most on-theme — the design-system → physical pipeline genuinely runs.

## Label SVG — subject

| Option | Description | Selected |
|--------|-------------|----------|
| Three zone-mode labels | FOCUS/FILMING/MAKER in three accents | (revised) |
| One "The Bench" wordmark | Single hero wordmark | (partial) |
| Reusable bin-label template + example | Parametric bin label | |

**User's choice:** Evolved through discussion. User flagged that the brand colors are **semantically meaningful** (Signal Path types), so coloring zones with them would break philosophical coherence — "the coherence IS the main point." → Final: generate **wordmark + eight-label ink-legend card**; defer zone/mode coloring to Phase 5; no bin label yet.
**Notes:** User's "filming ≈ pulse/broadcast" intuition matched the live Signal Path system better than the build-safe brief did.

---

## Doll-house scale + printer (ADR-002)

| Option | Description | Selected |
|--------|-------------|----------|
| ~220–260mm bed | Standard FDM | ✓ (Bambu A1 Combo) |
| ≤180mm bed | Compact | |
| 300mm+ bed | Large-format | |
| No printer yet | Assume ~220mm + checkpoint | |

**User's choice:** Bambu Lab A1 Combo (256×256 bed + AMS). → **ADR-002 locks 1:25** (footprint ~144×168mm fits; walls ~3mm print joinery cleanly; AMS enables meaning-bound ink colors). Joint feature-size verification deferred to Phase 6.

## Modular doll-house walls (emergent)

| Option | Description | Selected |
|--------|-------------|----------|
| Its own ADR | Capture architecture now, defer mechanism | ✓ |
| Fold into scale ADR + deferred idea | Lighter | |
| Defer entirely to Phase 6 | No Phase 1 ADR | |

**User's choice:** Its own ADR (ADR-003). Floor base + swappable walls via printed joinery; directs Phase 2 to build `shell.scad` as composable wall modules; mechanism (dovetail vs other) deferred to Phase 6.
**Notes:** Origin idea: swap a wall to add shelving mounts as the design iterates — the printed model becomes a living, version-controlled object (the thesis in atoms). Referenced `doratracyer/floor_plan` for structure.

## Semantic color integrity (emergent)

| Option | Description | Selected |
|--------|-------------|----------|
| Formal ADR | Lock "inks carry meaning, never reused" | ✓ |
| Encode in tokens + design-system docs | Lighter than an ADR | |

**User's choice:** Formal ADR (ADR-004). Enriched with reflect-don't-invent + the Board boundary (identity read-only from the Board).

## Uncolored Signal Path terms (emergent)

| Option | Description | Selected |
|--------|-------------|----------|
| Encode defined, mark rest pending | Defined inks + "pending — owned by Board" | ✓ (basis) |
| That + draft a proposal as a Pulse | Route candidates back to the Board | |
| Define them here as canonical | Violates Board boundary | |

**User's choice:** User then **dramatically updated the live source of truth** mid-discussion. Re-fetched `http://localhost:2368/about/` via curl (browser extension was offline). Captured the new **eight-label** system exactly (incl. pulse/broadcast split, schematic + cadence added). Decided: **full set**; **Bench/Rack/Board carry cream — no distinct ink** (they're places, not types).
**Notes:** cobalt + indigo are defined-but-unbound inks; recorded as available/reserved.

---

## Claude's Discretion

- Exact `tokens.yaml` YAML schema shape (encode the captured semantic structure faithfully).
- Label generator language (Node vs Python) and SVG layout of wordmark + legend card.
- README section ordering and ADR file formatting (lightweight standard ADR template).
- Repo metadata specifics (GitHub description/topics/social-preview) beyond "appropriate for build-in-public."

## Deferred Ideas

- Dynamic, color-shifting space via lighting (+ later robotic reconfiguration) — v2 AUTO. The project's highest-energy idea ("a joyful, meaningful design playground").
- Livestreaming the Bench for co-working / body-doubling — v2 FILM.
- Mode ↔ Signal-Path-activity ↔ ink reconciliation — Phase 5.
- Color proposals for any future place/term need — routed back to the Board as a Pulse.
- `make sync-tokens` automation — v2.
- Bin-label template — v2 (once Gridfinity bins exist).
