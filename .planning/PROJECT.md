# The Bench

## What This Is

The Bench is a living, version-controlled model of my physical home office/studio — "space as code" — built in public as a **Probe** in my Signal Path framework. This repo is the *execution arm*: it models the lived-in space (furniture layout, parametric desk accessories / cable organizers / shelving, the electronics workbench, lighting + AV/streaming control) as a *running model of* the space, not a one-time renovation plan, and drives the physical redesign over successive milestones.

The defining inversion: the **public / meta / Signal-Path layer leads; the physical build hangs off it.** The ultimate deliverable is the redesigned physical Bench; the artifact *along the way* is the documented process — **before → "alive."** The deliberate over-formalization (lines of OpenSCAD just to place a desk) is the point and the hook, not a bug.

## Core Value

A stranger encountering the public repo sees a real human turning his environment into a reproducible, expressive, lovingly over-engineered system — and **wants to follow along.** The repo + public artifact are the spine; the office is what they model.

*Prioritization rule when tradeoffs arise:* ship an expressive, public proof-of-work over perfecting private infrastructure. **Silence is the only failure mode.**

## Requirements

### Validated

<!-- Shipped and confirmed valuable. -->

(None yet — ship to validate)

### Active

<!-- Current milestone (v1): stand up the spine + model the "before." All hypotheses until shipped. -->

- [ ] Public repo "spine" frames the probe: thesis (before→alive; environment-as-provenance), identity, brand, and a back-link to the governing Board Signal — shippable **without** waiting on room measurement
- [ ] "Space as code" foundation: parametric room/furniture primitives + a one-command OpenSCAD → committed-render pipeline
- [ ] The room modeled **as-is** ("before"): measured dimensions, furniture layout, and the three modes (deep-focus / creator-filming / electronics-maker) represented
- [ ] A tangible **"doll-house" 3D-printed scale floor plan** of the as-is room (à la doratracyer/floor_plan + MakerWorld generative floor-plans)
- [ ] Equipment/inventory manifest as structured data (harvested from the old repo as a refreshed checklist, not a waterfall spec)
- [ ] In-repo **design system**: refreshed palette + type tokens, usable for renders and physical signage / bin labels
- [ ] **Pulse discipline**: every phase ends with a pulse-ready proof-of-work artifact, logged in-repo (broadcasting itself handled outside this repo)

### Out of Scope

<!-- Explicit boundaries with reasoning, to prevent re-adding. -->

- **Broadcasting / publishing the pulses** (newsletter, YouTube channel ops, social posting) — that is my A4/A5 (Public Explorer / Publisher) job *outside* this repo. The repo's only obligation is to *emit* pulse-ready proof-of-work.
- **Rendering the model into davidnunez.com / the Ghost site** — not required for v1. The public surface is the GitHub repo; the deliverable is the physical Bench.
- **The full Signal Path machinery in-repo** — carry only identity + brand + a back-link to the Board. Strategy/identity/priorities are read-only from the Board (system of record); don't re-derive them here.
- **The physical redesign execution** (actual buy / install / build) — deferred to v2+ milestones. v1 models the "before."
- **Long "live-in-it-for-weeks" marination / usage-observation gates** before optimizing (e.g., "wait 2–4 weeks of real usage before Gridfinity") — explicit anti-pattern; bias to rapid proof-of-work.
- **The old 10-phase waterfall, old GSD state, `params.scad` stub, empty `zones/` + `renders/`** from `the-bench-old` — start fresh; harvest documents only.
- **Audio/music production · full-home renovation · permanent structural changes (walls/plumbing/panel) · hiring a designer** — out of bounds (the hands-on process is the point).

## Context

**The person & the framework.** I'm a public explorer of emerging futures — a builder at the tech × humanity seam who explores in public. In my Signal Path framework the **Board** (Obsidian vault) is the digital system I think and make inside; the **Bench** is its physical seat — the home office/studio. This repo is the execution arm of the governing **Signal**: `Ideaverse/Works/Signals/The Bench redesign as a build-in-public probe.md` — the **system of record for intent**. Vocabulary: Signal (curiosity) → Probe (this work) → Pulse (a quick public share) / Component (distilled insight).

**Why now.** Post-exit, the Bench is the *engine*, not a side-room. "Be the example, explore in public" is the job. This is a deliberately low-stakes **first build-in-public rep** — a contained rehearsal of the muscle on a concrete, finite physical subject.

**The prior attempt.** `~/src/the-bench-old` (read-only) stalled at **4%**, Phase 1, behind an un-done "measure the room" gate — ~90% planning capital, ~0% built artifact. It put "space as code / shareable content" as **Phase 10 (the end)**; that inverted order is probably why it stalled. **Harvested** (refreshed): the aesthetic brief, the roadmap's physical-dependency logic (as a *checklist*), and the three-mode / zero-activation-energy core value. **Left behind:** the waterfall, the state, the stub, the empty dirs.

**The brand loop (new since March).** "The Bench" is now literally a **nav item + homepage section** on the live `davidnunez.com.ghost` site — the room is a **live brand asset**. Its build-in-public photography must match the site's visual language: warm, editorial, real WIP, **no AI imagery**.

**The philosophical spine (the differentiator).** *Environment-as-provenance* — capturing the full physical context in which work is made so the environment becomes part of the work's "soul." It explores the digital/analog boundary in a post-AI age where we still have 3D bodies needing human affordances. This is the genuinely original idea that makes the probe build-in-public-worthy "in a VERY unique way" — don't let it get buried as a furniture-layout detail.

**The three modes.** deep-focus (WFH / Zoom) · creator-filming (YouTube / talking-head / desk demos / screen recordings) · electronics-maker (soldering / 3D-print / light assembly).

## Constraints

- **Tech stack**: OpenSCAD is the "space as code" engine — `brew install --cask openscad@snapshot` (**not yet installed**; the `@snapshot`/dev release is required — the bare `openscad` cask installs the deprecated 2021.01 build, which the **QuackWorks** organizer library will not run on). Plus **BOSL2** + the **QuackWorks** submodule (Gridfinity / openGrid / Underware / Neogrid). Optional `yamllint` + `check-jsonschema` for the manifest. Present: Node 22, git, python3.
- **Brand**: palette = warm cream `#f5efe2` + near-black `#1a1820` + terracotta `#ec6a43` + plum `#4a2a57` + magenta pop `#c63c82`; type = Archivo (display) · Newsreader (serif body) · IBM Plex Mono (labels). **Supersedes** the March copper + electric-blue scheme. **No AI imagery** — authentic WIP photography only.
- **Cadence**: at least **weekly** pulse-ready proof-of-work. Heaviness is a feature; *silence* is the failure mode.
- **Physicality**: real-world delays (3D-print times, shipping, paint drying, physically sorting cable bins) are *legitimate* scheduling inputs — but must **not** inflate into long marination/analysis gates. Bias to rapid, prolific proof-of-work. **Not a 3-year project.**
- **Scope guard**: a contained side-rehearsal — must not sprawl into or displace primary income work, nor "open all the channels" at once.
- **Board boundary**: strategy/identity/priorities are read-only from the Board; insights/artifacts flow *back* to the Board (as Pulses/Components).

## Key Decisions

<!-- Decisions that constrain future work. -->

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Invert the sequence — public/meta spine leads, physical build hangs off it | Old repo buried space-as-code as Phase 10 and stalled behind a measurement gate | — Pending |
| Start fresh; harvest only 3 documents from `the-bench-old` (read-only) | ~90% planning capital, ~0% built — nothing to inflect | — Pending |
| Public surface = GitHub repo; deliverable = physical Bench; pulses broadcast out-of-repo | Repo is the execution arm; broadcasting is A4/A5's job, not this project's | — Pending |
| v1 = "before" modeled + spine + doll-house print; physical redesign deferred to v2+ | Contained, shippable; exercises the toolchain without the redesign's cost/lead-time | — Pending |
| The public spine never waits on room measurement | A measurement gate is exactly what killed v0 | — Pending |
| Physical delays are real, but no long "live-in-it" marination gates | Avoid the delay/analysis trap; bias to rapid proof-of-work | — Pending |
| Refresh palette to cream/near-black/terracotta/plum/magenta; retire copper + electric-blue | Reconcile with the live `davidnunez.com` identity | — Pending |
| Over-engineering is the artifact, not the trap | The trap is infra that defers shipping with *nothing shared*; here heaviness-on-display is the hook | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd:transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-27 after initialization*
