# the-bench Makefile
# ──────────────────────────────────────────────────────────────────────────────
# Build pipeline for the design-system → physical pipeline.
# Phase 1 targets: validate (YAML lint + schema smoke) and labels (SVG generator).
# Phase 2+ will add: renders (OpenSCAD headless CLI), stl, sync-tokens.
#
# Prerequisites: yamllint (brew install yamllint), python3 + PyYAML (pip install PyYAML)
# ──────────────────────────────────────────────────────────────────────────────

PYTHON   := python3
OPENSCAD := openscad

TOKENS   := design-system/tokens.yaml
LABELS   := design-system/labels/the-bench-labels.svg
GENERATOR := scripts/generate-labels.py

.PHONY: validate labels renders clean help

# ── validate ──────────────────────────────────────────────────────────────────
# Run yamllint on tokens.yaml, then assert exactly 8 Signal Path type keys.
validate:
	@echo "── validate: tokens.yaml ────────────────────────────────────────────────"
	yamllint $(TOKENS)
	@$(PYTHON) -c "\
import yaml, sys; \
t = yaml.safe_load(open('$(TOKENS)')); \
n = len(t.get('types', {})); \
assert n == 8, f'Expected 8 type keys, found {n}: {list(t[\"types\"].keys())}'; \
print('types: OK (8 types)')"
	@echo "── validate: PASSED ─────────────────────────────────────────────────────"

# ── labels ────────────────────────────────────────────────────────────────────
# Generate the wordmark + 8-label ink-legend SVG from tokens.yaml.
labels:
	@echo "── labels: generating SVG from tokens.yaml ──────────────────────────────"
	$(PYTHON) $(GENERATOR)
	@test -s $(LABELS) || { echo "ERROR: $(LABELS) is empty or missing"; exit 1; }
	@$(PYTHON) -c "import xml.dom.minidom; xml.dom.minidom.parse('$(LABELS)'); print('SVG well-formed XML: OK')"
	@echo "── labels: PASSED — $(LABELS) generated ─────────────────────────────────"

# ── renders ───────────────────────────────────────────────────────────────────
# Phase 2+ only: OpenSCAD headless renders. No-op stub until Phase 2.
renders:
	@echo "── renders: Phase 2+ target — not yet active ────────────────────────────"

# ── clean ─────────────────────────────────────────────────────────────────────
clean:
	@rm -f $(LABELS)
	@echo "Removed generated artifacts."

# ── help ──────────────────────────────────────────────────────────────────────
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "  validate   Lint tokens.yaml + assert exactly 8 Signal Path type keys"
	@echo "  labels     Generate design-system/labels/the-bench-labels.svg"
	@echo "  renders    (Phase 2+) Run OpenSCAD headless renders — stub until Phase 2"
	@echo "  clean      Remove generated artifacts"
	@echo "  help       Show this message"
