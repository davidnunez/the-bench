# Pitfalls Research

**Domain:** Build-in-public, version-controlled "space as code" physical workspace project
**Researched:** 2026-06-27
**Confidence:** HIGH (grounded in documented v0 post-mortem + domain-specific technical verification)

---

## Critical Pitfalls

### Pitfall 1: The Measurement Gate — Gating the Public Spine on a Physical Prerequisite

**What goes wrong:**
The public repository spine (README, thesis framing, brand identity, repo structure) never launches because it waits on a room measurement task that keeps getting deferred. v0 confirmed this exactly: Plan 01-02 (room measurement → `params.scad`) was the Phase 1 blocker; the project stalled at 4% with the measurement noted as "coming tonight" — and it never came. No public artifact ever shipped.

**Why it happens:**
It feels rational to say "I can't model the room until I know its dimensions." But the public spine does not require accurate dimensions. The repo story, the thesis ("environment as provenance"), the README, the brand tokens, and the scaffolding of the `params.scad` file with placeholder values are all measurment-independent. The conflation of "accurate model" with "any model" creates a fake dependency.

**How to avoid:**
Make measurement non-blocking by design. The spine phase must produce a public artifact that requires zero physical measurements to ship. The `params.scad` file ships first with explicit placeholder values and a comment marking them as TBD. Measurements then fill in those placeholders in a subsequent plan — they do not gate the spine. Rule: **the public repo goes live before any tape measure is picked up.**

**Warning signs:**
- Phase 1 plan list includes "measure room" before "publish README"
- Any plan's description starts with "First, we need to measure..."
- More than one plan passes without a publicly shareable artifact being committed
- `params.scad` is blocked waiting on physical data

**Phase to address:**
Spine / Phase 1 — must be explicitly structured so the first deliverable is a live public repo with a README, brand, and thesis. Measurements are a separate, parallel, non-blocking sub-task.

---

### Pitfall 2: Planning Capital Inversion — 90% Infrastructure, 0% Audience Artifact

**What goes wrong:**
The project spends all its early energy on internal scaffolding — ADR frameworks, YAML schemas, directory structures, mood boards, `params.scad` stubs — before a single artifact that a stranger could meaningfully follow exists in the public repo. v0 collapsed here: 2 of 5 Phase 1 plans were "initialize repo structure" (internal) and "establish mood board" (internal), and the project stalled before any public-facing output shipped. The repo had a skeleton and an aesthetic brief; it had no story.

**Why it happens:**
Infrastructure feels like progress because it is real work. ADR templates, manifest schemas, and directory conventions are genuinely useful. But they are entirely invisible to a build-in-public audience. The psychological reward of "the scaffold is right" substitutes for the discipline of "something must ship publicly this week."

**How to avoid:**
Apply the one-artifact rule: every phase must produce a pulse-ready public deliverable as its first or second plan, not its last. The repo README with the thesis, the design system tokens, the first render — these are the real Phase 1 deliverables. Infrastructure plans (ADR template, schema) are helpers that arrive in the same phase but are never the phase's gateway. If a phase can be described entirely in terms of internal tasks, rewrite it.

**Warning signs:**
- Phase 1 has three "setup" plans before the first shareable output plan
- The word "scaffold," "skeleton," or "template" appears in more than one plan name
- A week passes and the only new commit is a `.gitignore` update
- Someone would have to read the code to know anything happened

**Phase to address:**
Spine / Phase 1 — invert the plan order: public README first, then infrastructure.

---

### Pitfall 3: Cascading Wait Gates — Mandatory Idle Periods Chained in Series

**What goes wrong:**
The roadmap encodes multiple "wait X weeks for Y before doing Z" gates in series. v0's roadmap had: Phase 6 HA "2–4 week manual validation" → Phase 7 Gridfinity "after 2–4 weeks of real usage patterns" → Phase 8 presence automation "only after manual scenes proven stable." These chain into a potential 6–8 week mandatory idle period where the project produces nothing and the build-in-public audience sees nothing.

**Why it happens:**
The logic sounds defensible in isolation: "don't automate what you haven't validated manually" and "don't print custom storage for usage patterns you haven't observed yet" are both reasonable engineering instincts. The failure is treating these as sequential gates rather than parallel constraints. You can run HA in manual mode while simultaneously designing Gridfinity. You can observe usage patterns for a week, not a month.

**How to avoid:**
No wait gate exceeds two weeks. During any mandated wait period, a parallel plan must be identified that produces a proof-of-work artifact. "Validate HA manually" and "design Gridfinity baseplates in OpenSCAD" can run concurrently. If a phase has no concrete output during its wait period, it is not a phase — it is dead time. Shrink wait periods to their actual minimum; "2–4 weeks" is often "3–5 days of real data."

**Warning signs:**
- A plan's description says "wait X weeks" with no parallel deliverable named
- A phase success criterion requires a calendar period to elapse with no artifact
- The roadmap has two consecutive wait-gated phases
- The phrase "after real usage patterns emerge" appears without a time box

**Phase to address:**
Home Automation and Gridfinity phases — redesign them to overlap, not sequence. The marination gate belongs in the roadmap's phase structure, not in individual plan timelines.

---

### Pitfall 4: The Marination Trap — Letting Things "Live in the Space" Before Acting

**What goes wrong:**
A piece of equipment arrives, gets placed "temporarily," and stays there for three weeks because "I want to see how I use it before committing." A Gridfinity baseplate gets designed but not printed because "I should observe my workflow more." A cable gets managed "good enough for now." Each individual marination feels like insight-gathering; cumulatively they are the project not moving.

**Why it happens:**
Marination masquerades as empiricism. "I'm learning how I actually work before optimizing" sounds rigorous. In a build-in-public context it is delay. The audience doesn't see the learning; they see silence. The real-world truth is that most usage patterns are predictable in advance (a soldering iron lives at the maker bench; USB cables go in the drawer nearest the desk) and the cost of being slightly wrong about organization is low — you move a bin.

**How to avoid:**
Bias hard to rapid, prolific proof-of-work. Default to installing and iterating rather than observing and then installing. The cost of a wrong bin placement is 5 minutes. The cost of a 3-week marination is 3 weeks of no pulse. Explicit rule: **if a thing can be installed in under 2 hours, install it and share it; do not wait.** Gridfinity gets installed as soon as the drawer dimensions are measured, not after usage patterns are "known."

**Warning signs:**
- Any plan's rationale includes "after I've lived with it for a while"
- Equipment has been in the room for >1 week without being installed or decided on
- A phase's first plan is described as "observe and document" rather than "install and ship"
- The words "eventually" or "when I have more data" appear in plan descriptions

**Phase to address:**
Storage / Gridfinity phase and any phase that involves physical installation — explicitly state "install first, iterate second" in phase rationale.

---

### Pitfall 5: Scope Sprawl — Opening All the Channels, Displacing Income Work

**What goes wrong:**
The project expands organically into adjacent territories: audio production setup gets added to the maker bench scope; a newsletter gets started alongside the repo; YouTube channel ops land in the project backlog; a full home renovation thread opens because "while we're at it..." Each expansion feels natural at the time; collectively they convert a contained 3-month probe into an 18-month sprawl that competes with primary income work.

**Why it happens:**
Build-in-public projects attract tangential ambition. Every tool in the room becomes a potential content vertical. The mistake is treating "related" as "in scope." Broadcasting (newsletter, YouTube channel ops, social posting) is explicitly adjacent to this project but must stay outside it — the repo's job is to emit pulse-ready artifacts, not to operate the channels.

**How to avoid:**
The out-of-scope list in PROJECT.md is a hard boundary, not a soft guideline. Add a scope-check gate to every new plan proposal: "Does this displace primary income work? Does it open a new channel? Does it belong in PROJECT.md's Out of Scope list?" If yes to any, park it in the Board (Obsidian) as a future Signal, not in this repo. The scope guard is: **audio/music production, full-home renovation, structural changes, hiring a designer, and broadcasting operations are permanently out of scope.**

**Warning signs:**
- A plan proposal is about content ops rather than physical build or code
- "While we're at it" appears in a plan description
- The project estimate has grown by >50% since last milestone
- A week's work primarily served the channel rather than the Bench
- Total active plans exceeds 8 at once

**Phase to address:**
Every phase boundary — explicitly recheck scope at each `/gsd:transition`. Add a one-sentence scope confirmation to each phase's definition of done.

---

### Pitfall 6: The 3-Year Project Anti-Pattern — No Time Horizon, Always "One More Thing"

**What goes wrong:**
The project never declares a milestone done because there is always something slightly better: better cable management, one more Gridfinity bin design, another HA scene. Without a hard time horizon, the project horizons expand to fill all available attention. v0's roadmap had 10 phases with no time estimate; there was nothing to push against.

**Why it happens:**
Physical workspace projects are inherently open-ended: a room can always be improved. Build-in-public projects add another dimension: content can always be expanded. The combination is particularly dangerous because improvement and audience-building feel like they justify indefinite extension.

**How to avoid:**
Every milestone has an explicit time budget at the top of its planning documents. The current milestone (v1: "before" state modeled + spine + doll-house print) must have a declared end date or duration. The rule: **a milestone that takes longer than 12 weeks has failed its own scope.** At 8 weeks, run a scope triage; at 10 weeks, cut to minimum viable completion. Phases that aren't started by week 8 roll to the next milestone.

**Warning signs:**
- More than 10 active plans exist at once
- A milestone has been "in progress" for >8 weeks
- The phrase "I just want to also..." appears in phase planning
- New requirements are added at phase 5 of a 6-phase milestone

**Phase to address:**
Milestone planning — set a time box in the first plan. Phase transitions enforce the time box.

---

## Technical Debt Patterns

Shortcuts that seem reasonable but create long-term problems specific to this domain.

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Hardcoding room dimensions in multiple .scad files instead of params.scad | Faster first model | Every measurement change requires hunting 10 files; models drift out of sync | Never — params.scad is the single source |
| Using F5 preview to export STL | Faster iteration cycle | Broken geometry, manifold errors in printed parts; approximations in CSG pass silently | Never for STLs committed to repo |
| Printing a full Gridfinity set before a prototype fit-check | Fills drawers immediately | Entire print batch unusable if drawer tolerance is off by >2mm | Never — always verify with one baseplate first |
| Mixing Gridfinity and OpenGrid bins in the same drawer | "Both look compatible" | Bins from different systems do not share depth/height standards; drawers become inconsistent | Never — pick one system per zone |
| Committing placeholder params.scad without marking them as placeholder | Looks like progress | Future contributors (or future-you) treat placeholder dimensions as real; errors propagate | Acceptable IF values are clearly marked `// PLACEHOLDER — not measured` |
| Setting $fn globally high (>64) during development | Smooth circles in preview | Render time multiplies with each object; 30-item room model becomes 20-minute render | Only for final F6 render artifacts; use $fn=12 during development |
| Storing HA config only in the UI (not committed YAML) | Faster scene prototyping | Config is lost on HA reinstall; repo is not the source of truth | Never — all HA config ships as committed YAML |

---

## Integration Gotchas

Common mistakes when connecting physical and digital components of this project.

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| OpenSCAD → STL → slicer | Exporting from F5 preview; slicer reports non-manifold errors silently and slices anyway | Always F6 render before STL export; verify with slicer mesh analysis before printing |
| params.scad → physical reality | Treating params.scad as "live" (updating it as changes are made) without preserving the "before" snapshot | Tag the "before" commit; keep `params-before.scad` snapshot or use git tags before any redesign changes |
| Gridfinity model → actual drawer | Measuring outer drawer dimension instead of inner usable dimension, ignoring drawer rail/slide clearance | Measure inner usable dimension; subtract 4–6mm for clearance; verify against the model note that IKEA Alex 9-drawer depth (425mm) differs from 5-drawer (525mm) |
| OpenSCAD include/use chain | `use` vs. `include` confusion — `use` imports only modules, `include` imports variables/constants too; mixing them causes params to be undefined | Establish explicit conventions: params.scad always uses `include`; utility modules use `use` |
| Floor plan SVG → OpenSCAD (doratracyer approach) | SVG exported in wrong units (px instead of mm); the resulting model is 3.78× wrong scale | Set SVG export to mm units in Inkscape; verify that 1mm in SVG = 1mm in OpenSCAD output before committing |
| 3D printed scale model → real dimensions | Choosing 1:25 scale, finding real 100mm walls become 4mm prints — at or below FDM minimum wall thickness (0.8mm supported, 1.2mm reliable) | Calculate print wall thickness before committing to scale: minimum 1.5mm print wall; work backwards to scale (1:50 is safer than 1:25 for a typical room) |

---

## Performance Traps

Patterns that work at small scale but fail as the model grows.

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| High $fn on all cylinders/spheres globally | Preview takes 30+ seconds for a room model; F6 render approaches hours | Set $fn=12 as global default; override to 64 only in the final render module | Any room model with >10 furniture items at $fn=32 |
| `render()` calls inside reusable furniture modules | Entire assembly re-renders even when only one item changes; exponential time growth | Never call `render()` inside reusable modules; call it only at the top level for final artifact generation | As soon as `render()` appears inside a module used 5+ times |
| Union of many overlapping objects without hull/minkowski | CSG tree grows; preview approximation diverges from actual geometry | Use hull() for convex shapes; structure models to minimize deep union nesting | Usually visible by item 15 in a complex assembly |
| `difference()` with very complex subtracted geometry | OpenSCAD computes the subtraction for every instance | Compute the subtracted shape once, store as variable, reuse | Any model with repeated `difference()` using the same subtracted shape |

---

## Scope Guard Failures

Domain-specific scope violations that look like legitimate project work.

| Mistake | How It Enters | Prevention |
|---------|---------------|------------|
| Broadcasting operations (posting, scheduling, newsletter) land in the project backlog | "I should track my content calendar here" | Repo emits pulse-ready artifacts; channel ops live in the Board (Obsidian). The repo's scope ends at commit. |
| Audio/music production setup added to the maker bench phase | "While I'm setting up the bench, I should also..." | Hard boundary: audio/music production is explicitly out of scope in PROJECT.md; reconfirm at every phase gate |
| The design system expands to drive the website/newsletter | "Since I have the tokens, I should use them everywhere" | Design system scope: palette + type tokens usable for renders and physical labels. Website is separate project. |
| ADR count grows >10 before Phase 1 ships | Over-formalization of every decision | ADRs for consequential, irreversible decisions only; not for "I decided to name the file params.scad" |
| Phase planning documents become the artifact instead of the build | "I wrote a great phase plan today" | Plans are maps, not territory. No plan counts as proof-of-work. Only committed artifacts count. |

---

## "Looks Done But Isn't" Checklist

Things that appear complete but are missing the critical proof-of-work substance.

- [ ] **Spine published:** Does the README tell a stranger what this is, why it matters, and what they'll see next? Or is it just a file listing?
- [ ] **params.scad "live":** Are the dimensions real measured values, or are they still placeholders without being marked as such?
- [ ] **Gridfinity baseplates installed:** Is there a prototype fit-check commit showing the first baseplate physically in the drawer, or only STL files?
- [ ] **HA config committed:** Is the YAML actually committed to `config/home-assistant/`, or does "HA is configured" mean "it's set up in the UI"?
- [ ] **OpenSCAD pipeline reproducible:** Can a fresh clone run `make renders` and produce the committed PNGs, or are some renders manually generated?
- [ ] **STLs from F6, not F5:** Do the committed STL files come from an F6 render pipeline, or from File > Export (which may be using F5 approximation)?
- [ ] **Floor plan scale verified:** Has a test print at the chosen scale confirmed wall thickness is ≥1.5mm before committing to printing the full model?
- [ ] **Phase pulse exists:** Does the phase end with a committed, pulse-ready artifact that could be shared externally — or just internal infrastructure?

---

## Recovery Strategies

When pitfalls occur despite prevention, how to recover.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Measurement gate stall (project pauses for >1 week) | LOW | Declare a "spine sprint": ship the public README and brand scaffold with explicit placeholder dimensions. Never resume waterfall order — spine first, measurements fill in. |
| Planning capital inversion (3+ plans, no public artifact) | LOW | Immediate: identify the fastest possible public artifact in the current phase; ship it before any more infrastructure work. Review plan order to ensure this doesn't recur. |
| Cascading wait gate (project idle for 2+ weeks) | MEDIUM | Identify what can be done in parallel during the wait; start it immediately. If nothing can be done in parallel, shrink the wait period to its empirical minimum (1 week, not 4). |
| Marination trap (item sits unoptimized for >2 weeks) | LOW | Install it now; share the install as a pulse. If the install takes <2 hours, it should have shipped 2 weeks ago. |
| Scope sprawl (new channel or out-of-scope work started) | MEDIUM | Stop immediately; move the work to the Board as a future Signal. Do not "finish the chapter" — park it at the current state and return to the core scope. |
| OpenSCAD unit drift (model is 25.4x wrong scale) | MEDIUM | Identify the unit source in params.scad; fix at the entry point; verify all child files reference params, not hardcoded values. Never fix by scaling outputs. |
| Gridfinity print batch misfit | MEDIUM | Do not reprint the full batch. Identify the correct inner usable dimension; adjust the OpenSCAD model; print one verification piece; then reprint. |
| F5/F6 STL error (printed part has broken geometry) | MEDIUM-HIGH | Re-render with F6; check for non-manifold in slicer; fix OpenSCAD model if needed. Add F6-only STL export to the CI/pipeline documentation. |

---

## Pitfall-to-Phase Mapping

How roadmap phases should be structured to prevent each pitfall.

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Measurement gate | Spine phase (first) — README ships before tape measure | First committed artifact is a public-facing README, not params.scad |
| Planning capital inversion | Spine phase — first 2 plans produce public artifacts, not scaffolding | At least one plan in the first phase is "publish X to repo" |
| Cascading wait gates | HA + Gridfinity phases — redesigned to overlap, with parallel deliverables during any wait | No phase success criterion requires a calendar period with no artifact |
| Marination trap | Storage/Gridfinity phase — "install first, iterate second" stated as the phase operating principle | Gridfinity ships in the same week as drawer measurement, not weeks later |
| Scope sprawl | Every phase boundary — scope recheck at `/gsd:transition` | Out-of-scope list confirmed unchanged at each transition |
| 3-year project anti-pattern | Milestone planning — time box stated in milestone plan | Milestone has a declared end date; scope triage runs at 8 weeks |
| OpenSCAD unit drift | Model foundation phase — params.scad structure and unit convention established | Only one unit (mm) used in params.scad; child files have no hardcoded dimensions |
| F5/F6 STL errors | Any phase that produces STL artifacts — F6 render pipeline defined | All STL commits come from the render pipeline, not File > Export |
| OpenSCAD assembly slowdown | Model foundation phase — $fn convention and render vs. preview settings documented | Preview uses $fn=12; final render uses $fn=64; render time for room model stays under 5 minutes |
| Gridfinity measurement error | Storage/Gridfinity phase — prototype-first rule stated | First Gridfinity plan is "measure inner usable dimensions + print one baseplate prototype" |
| Over-printing before fit verification | Storage/Gridfinity phase — explicit prototype gate | Batch print plan is blocked until prototype fit photo is committed |
| Grid system mixing | Storage/Gridfinity phase — system choice locked in ADR | One ADR names the chosen system per zone; mixing requires ADR revision |
| Floor plan scale failure | Doll-house print phase — scale calculation done before modeling | Phase 0 sub-task: calculate wall thickness at chosen scale; minimum 1.5mm confirmed |
| Physical delay inflation | All phases with physical components | Every phase with a print/ship/cure step names what gets built *during* the wait |
| Repo coherence gap | Spine phase — README narrative as the first deliverable | A stranger reading the README understands the project thesis without reading any code |

---

## Sources

- `/Users/davidnunez/src/the-bench-old/.planning/STATE.md` — direct evidence of Phase 1 stall; measurement gate blocker; 4% completion
- `/Users/davidnunez/src/the-bench-old/.planning/ROADMAP.md` — 2–4 week wait gates in Phase 6 (06-06), Phase 7 goal, Phase 8 dependency; "Space as Code" as Phase 10
- `/Users/davidnunez/src/the-bench/.planning/PROJECT.md` — owner-stated anti-patterns; out-of-scope list; the "silence is the only failure mode" prioritization rule
- [OpenSCAD Render Times — MakerBlock](https://makerblock.com/2025/04/openscad-render-times/) — $fn / render() performance impact with measured examples
- [OpenSCAD F6 Render vs. F5 Preview Issue #6301](https://github.com/openscad/openscad/issues/6301) — documented divergence between F5 and F6 geometry
- [Gridfinity Baseplate for IKEA Alex (Measurements Fixed) — Printables](https://www.printables.com/model/987829-gridfinity-baseplate-for-ikea-alex-measurements-fi) — real-world evidence of ALEX dimension variation and misfit problems requiring sawing/sanding
- [openGrid — openGrid.world](https://www.opengrid.world/) — grid unit specification (28mm) and Gridfinity compatibility documentation
- [Neogrid — Hands On Katie](https://www.handsonkatie.com/neogrid) — Neogrid vs. Gridfinity vs. openGrid system comparison
- [FDM Minimum Wall Thickness — BigRep](https://bigrep.com/posts/designing-wall-thickness-for-3d-printing/) — 0.8mm supported, 1.2mm reliable, 1.5mm recommended minimum for FDM walls
- [doratracyer/floor_plan — GitHub](https://github.com/doratracyer/floor_plan) — SVG → OpenSCAD → STL pipeline for 3D-printable floor plans; unit handling in workflow

---
*Pitfalls research for: build-in-public space-as-code physical workspace project*
*Researched: 2026-06-27*
