#!/usr/bin/env python3
"""
Test suite for scripts/generate-labels.py.

Validates the label generator behavior before implementation exists (TDD RED phase).
Run: python3 scripts/test_generate_labels.py
"""
import sys
import pathlib
import importlib.util
import subprocess


GENERATOR = pathlib.Path("scripts/generate-labels.py")
OUTPUT    = pathlib.Path("design-system/labels/the-bench-labels.svg")
TOKENS    = pathlib.Path("design-system/tokens.yaml")

EIGHT_TYPES = [
    "signal", "probe", "pulse", "broadcast",
    "module", "cadence", "component", "schematic",
]
BANNED_MODES = ["deep-focus", "creator-filming", "electronics-maker"]


def run_tests():
    failures = []

    # T1: generator file exists
    if not GENERATOR.exists():
        failures.append(f"FAIL T1: {GENERATOR} does not exist")
    else:
        src = GENERATOR.read_text()

        # T2: uses yaml.safe_load (security control, T-01-02-V5)
        if "yaml.safe_load" not in src:
            failures.append("FAIL T2: generator does not call yaml.safe_load()")

        # T3: does NOT call yaml.load( (forbidden — arbitrary deserialization)
        if "yaml.load(" in src:
            failures.append("FAIL T3: generator calls yaml.load() — must use safe_load()")

    # T4: run the generator and check output is non-empty
    result = subprocess.run(
        [sys.executable, str(GENERATOR)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        failures.append(f"FAIL T4: generator exited with {result.returncode}\n{result.stderr}")
    elif not OUTPUT.exists() or OUTPUT.stat().st_size == 0:
        failures.append(f"FAIL T4: {OUTPUT} is missing or empty after generator ran")
    else:
        svg = OUTPUT.read_text()

        # T5: wordmark aubergine fill (#4a2a57) present
        if "#4a2a57" not in svg:
            failures.append("FAIL T5: SVG missing aubergine wordmark fill (#4a2a57)")

        # T6: wordmark text "the-bench" present
        if "the-bench" not in svg:
            failures.append("FAIL T6: SVG missing 'the-bench' wordmark text")

        # T7: all 8 type names in SVG (ink-legend card)
        for t in EIGHT_TYPES:
            if t not in svg:
                failures.append(f"FAIL T7: SVG missing type name '{t}'")

        # T8: no mode/zone labels present (D-16/D-17)
        for mode in BANNED_MODES:
            if mode in svg:
                failures.append(f"FAIL T8: SVG contains banned mode token '{mode}'")

    # Report
    if failures:
        print("FAILED:")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        print(f"PASSED: {len(EIGHT_TYPES)+4} checks all green")
        sys.exit(0)


if __name__ == "__main__":
    run_tests()
