---
phase: 1
slug: public-spine-design-system-adrs
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-06-27
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> Phase 1 deliverables are primarily committed text artifacts (README, LICENSE,
> tokens.yaml, generated SVG, ADRs). Validation is proportional: file-existence
> checks, YAML syntax/lint, and a generator smoke test. No unit-test framework.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | None — shell + `make` targets (`make validate`, `make labels`) |
| **Config file** | `Makefile` (Wave 0 creates `.PHONY: validate labels`) |
| **Quick run command** | `make validate` |
| **Full suite command** | `make validate && make labels` |
| **Estimated runtime** | ~3 seconds |

---

## Sampling Rate

- **After any change to `tokens.yaml`:** Run `make validate`
- **After any change to the generator or tokens:** Run `make labels`
- **Before phase gate / `/gsd:verify-work`:** `make validate && make labels` both green
- **Max feedback latency:** ~3 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| tokens-parse | tokens | — | DSGN-01 | — | N/A | lint | `yamllint design-system/tokens.yaml` | ❌ W0 (Makefile target) | ⬜ pending |
| tokens-8types | tokens | — | DSGN-01 | — | N/A | smoke | `python3 -c "import yaml; t=yaml.safe_load(open('design-system/tokens.yaml')); assert len(t['types'])==8"` | ❌ W0 (`make validate` step) | ⬜ pending |
| labels-svg | labels | — | DSGN-03 | — | `yaml.safe_load()` (not `yaml.load()`) | smoke | `make labels && test -s design-system/labels/the-bench-labels.svg` | ❌ W0 (`make labels`) | ⬜ pending |
| license-mit | spine | — | SPINE-04 | — | N/A | smoke | `grep -q 'MIT License' LICENSE` | ❌ (human check acceptable) | ⬜ pending |
| adrs-exist | adrs | — | CODE-06 | — | N/A | smoke | `ls decisions/ADR-00{1,2,3,4}-*.md` | ❌ (human check acceptable) | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

*Plan/Wave columns finalized by the planner; rows above are the validation contract the plans must satisfy.*

---

## Wave 0 Requirements

- [ ] `Makefile` — declare `.PHONY: validate labels`
- [ ] `make validate` — `yamllint design-system/tokens.yaml` + 8-types Python assertion
- [ ] `make labels` — invoke `scripts/generate-labels.py` + `-s` check on output SVG

*These are the only validation-infrastructure gaps; everything else is artifact existence/grep.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| README orients a stranger to the before→alive thesis + Board back-link | SPINE-01 | Subjective/editorial quality not script-checkable | Read README.md top-to-bottom; confirm thesis section, repo structure, and a working back-link to davidnunez.com's "The Bench" |
| Generated SVG renders as wordmark (aubergine-on-cream) + 8-label ink-legend card | DSGN-03 | Visual rendering not asserted by smoke test | Open `the-bench-labels.svg` in a browser/Inkscape; confirm wordmark + 8 swatches with correct meanings |
| Repo metadata (description, topics, About) set on GitHub | SPINE-01 | Lives on GitHub, not in repo | Check repo About panel after push |

---

## Validation Sign-Off

- [ ] All tasks have an automated verify command or a Wave 0 dependency
- [ ] Sampling continuity: validation artifacts (`make validate`/`make labels`) reachable from every plan touching tokens or generator
- [ ] Wave 0 covers all MISSING references (Makefile targets)
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter (after planner maps tasks)

**Approval:** pending
