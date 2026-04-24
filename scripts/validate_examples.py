#!/usr/bin/env python3
"""Lightweight validation for the RANStein SelfAudit fixtures.

This is intentionally dependency-free. The JSON schemas are the public machine
boundary; this script provides a quick local smoke test for the checked-in
examples and the golden dismounting fixture.
"""

from __future__ import annotations

import json
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - optional local dependency
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
SCHEMA = ROOT / "schema"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_l1_shape(l1: dict) -> None:
    required = {
        "agent_type",
        "source_profile",
        "sessions",
        "memory_state",
        "phi_trajectory",
        "operator_usage",
        "commitments",
        "family_entries",
        "risk_tier",
        "warnings",
    }
    require(required <= set(l1), f"input_l1.json missing keys: {sorted(required - set(l1))}")
    require(l1["agent_type"] == "self", "agent_type must be self")
    require(
        l1["source_profile"]["session_count"] == len(l1["sessions"]),
        "source_profile.session_count must match sessions length",
    )


def validate_output_shape(output: dict) -> None:
    require({"layers", "audit_log", "risk_tier"} <= set(output), "output envelope missing top-level keys")
    layers = output["layers"]
    require({"L2", "L3A", "L3B", "L3C", "L4"} <= set(layers), "output layers missing required blocks")
    require(2 <= len(layers["L3A"]) <= 4, "L3A must contain 2-4 hypotheses")
    require(isinstance(layers["L3B"], list), "L3B must be a list")
    require(isinstance(layers["L4"], list), "L4 must be a list")


def validate_cross_references(output: dict) -> None:
    layers = output["layers"]
    pattern_ids = {p["pattern_id"] for p in layers["L2"]["output_patterns"]}
    pattern_ids |= {p["pattern_id"] for p in layers["L2"]["memory_practice_patterns"]}

    hypothesis_ids = {h["hypothesis_id"] for h in layers["L3A"]}
    dismounting_ids = {d["dismounting_id"] for d in layers["L3B"]}
    finding_ids = {f["audit_id"] for f in layers["L3C"]}

    for hypothesis in layers["L3A"]:
        if hypothesis["constraint_status"] != "violates_UNSOURCED":
            missing = set(hypothesis["evidence_patterns"]) - pattern_ids
            require(not missing, f"L3A {hypothesis['hypothesis_id']} cites unknown patterns: {sorted(missing)}")

    for finding in layers["L3C"]:
        missing = set(finding["evidence_patterns"]) - pattern_ids
        require(not missing, f"L3C {finding['audit_id']} cites unknown patterns: {sorted(missing)}")

    for fragility in layers["L4"]:
        require(fragility["probe"]["probe_risk"] in {"low", "medium"}, f"L4 {fragility['fragility_id']} has invalid probe risk")
        require(
            set(fragility["source_hypotheses"]) <= hypothesis_ids,
            f"L4 {fragility['fragility_id']} cites unknown hypotheses",
        )
        require(
            set(fragility["source_dismountings"]) <= dismounting_ids,
            f"L4 {fragility['fragility_id']} cites unknown dismountings",
        )
        require(
            set(fragility["source_findings"]) <= finding_ids,
            f"L4 {fragility['fragility_id']} cites unknown findings",
        )


def validate_golden(golden: dict, output: dict) -> None:
    expected = golden["expected_dismounting"]
    matches = [
        item
        for item in output["layers"]["L3B"]
        if item["operator_name"] == expected["operator_name"]
        and item["severity"] == expected["severity"]
        and item["evidence_type"] == expected["evidence_type"]
        and item["evidence_sessions"] == expected["evidence_sessions"]
    ]
    require(matches, "golden dismounting fixture did not match output_env.json")


def validate_with_jsonschema(instance: dict, schema: dict, label: str) -> bool:
    if Draft202012Validator is None:
        return False
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.path) or "<root>"
        raise AssertionError(f"{label} failed JSON Schema validation at {location}: {first.message}")
    return True


def main() -> None:
    require((SCHEMA / "SelfAudit_L1.schema.json").exists(), "missing SelfAudit_L1 schema")
    require((SCHEMA / "OUTPUT_ENV_SELFAUDIT.schema.json").exists(), "missing OUTPUT_ENV_SELFAUDIT schema")

    l1 = load_json(EXAMPLES / "input_l1.json")
    output = load_json(EXAMPLES / "output_env.json")
    golden = load_json(EXAMPLES / "golden_dismounting_audit.json")
    l1_schema = load_json(SCHEMA / "SelfAudit_L1.schema.json")
    output_schema = load_json(SCHEMA / "OUTPUT_ENV_SELFAUDIT.schema.json")

    jsonschema_used = validate_with_jsonschema(l1, l1_schema, "input_l1.json")
    jsonschema_used = validate_with_jsonschema(output, output_schema, "output_env.json") or jsonschema_used

    validate_l1_shape(l1)
    validate_output_shape(output)
    validate_cross_references(output)
    validate_golden(golden, output)

    suffix = " with JSON Schema" if jsonschema_used else " with dependency-free shape checks"
    print(f"ok: examples and golden dismounting fixture validated{suffix}")


if __name__ == "__main__":
    main()
