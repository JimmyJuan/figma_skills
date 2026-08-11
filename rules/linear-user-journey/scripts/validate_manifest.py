#!/usr/bin/env python3
"""Validate the closed structure of a linear-journey manifest.

This validator deliberately does not decide semantic screen identity, user intent,
or whether a proposed mapping is correct.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


JOURNEY_ID = re.compile(r"J[0-9]{2}(?:-[A-Z0-9]+)*")
OCCURRENCE_ID = re.compile(r"J[0-9]{2}(?:-[A-Z0-9]+)*-[SBR][0-9]{2}")
SCREEN_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
NODE_ID = re.compile(r"[0-9]+:[0-9]+")
TRANSITION_ID = re.compile(r"T[0-9]{2,}")

SCOPES = {"main_component", "instance_override", "journey_annotation", "migration"}
MAPPING_STATUSES = {"proposed", "approved", "migrated", "disputed"}
TRANSITION_KINDS = {
    "user_action",
    "system_event",
    "decision",
    "elapsed_time",
    "alternate_entry",
    "cross_role",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def fullmatch(pattern: re.Pattern[str], value: Any) -> bool:
    return isinstance(value, str) and pattern.fullmatch(value) is not None


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    require(isinstance(data, dict), "root must be an object", errors)
    if not isinstance(data, dict):
        return errors

    allowed_root = {"version", "journey_id", "actor", "outcome", "occurrences", "transitions"}
    require(set(data) <= allowed_root, "root contains unsupported fields", errors)
    require(data.get("version") == "1.0", "version must be '1.0'", errors)
    require(fullmatch(JOURNEY_ID, data.get("journey_id")), "journey_id has an invalid format", errors)
    require(isinstance(data.get("actor"), str) and bool(data.get("actor")), "actor must be a non-empty string", errors)
    require(isinstance(data.get("outcome"), str) and bool(data.get("outcome")), "outcome must be a non-empty string", errors)

    occurrences = data.get("occurrences")
    transitions = data.get("transitions")
    require(isinstance(occurrences, list), "occurrences must be an array", errors)
    require(isinstance(transitions, list), "transitions must be an array", errors)
    if not isinstance(occurrences, list) or not isinstance(transitions, list):
        return errors

    occurrence_ids: set[str] = set()
    allowed_occurrence = {
        "occurrence_id",
        "screen_id",
        "figma_node_id",
        "main_component_node_id",
        "scope",
        "mapping_status",
        "semantic_rationale",
    }
    for index, item in enumerate(occurrences):
        prefix = f"occurrences[{index}]"
        require(isinstance(item, dict), f"{prefix} must be an object", errors)
        if not isinstance(item, dict):
            continue
        require(set(item) <= allowed_occurrence, f"{prefix} contains unsupported fields", errors)
        occurrence_id = item.get("occurrence_id")
        require(fullmatch(OCCURRENCE_ID, occurrence_id), f"{prefix}.occurrence_id has an invalid format", errors)
        require(occurrence_id not in occurrence_ids, f"{prefix}.occurrence_id is duplicated", errors)
        if isinstance(occurrence_id, str):
            occurrence_ids.add(occurrence_id)
        require(fullmatch(SCREEN_ID, item.get("screen_id")), f"{prefix}.screen_id has an invalid format", errors)
        require(fullmatch(NODE_ID, item.get("figma_node_id")), f"{prefix}.figma_node_id has an invalid format", errors)
        component_id = item.get("main_component_node_id")
        require(component_id is None or fullmatch(NODE_ID, component_id), f"{prefix}.main_component_node_id has an invalid format", errors)
        require(item.get("scope") in SCOPES, f"{prefix}.scope is invalid", errors)
        if "mapping_status" in item:
            require(item.get("mapping_status") in MAPPING_STATUSES, f"{prefix}.mapping_status is invalid", errors)
        if "semantic_rationale" in item:
            require(isinstance(item.get("semantic_rationale"), str), f"{prefix}.semantic_rationale must be a string", errors)

    transition_ids: set[str] = set()
    allowed_transition = {"transition_id", "source_occurrence_id", "target_occurrence_id", "kind", "label"}
    for index, item in enumerate(transitions):
        prefix = f"transitions[{index}]"
        require(isinstance(item, dict), f"{prefix} must be an object", errors)
        if not isinstance(item, dict):
            continue
        require(set(item) <= allowed_transition, f"{prefix} contains unsupported fields", errors)
        transition_id = item.get("transition_id")
        require(fullmatch(TRANSITION_ID, transition_id), f"{prefix}.transition_id has an invalid format", errors)
        require(transition_id not in transition_ids, f"{prefix}.transition_id is duplicated", errors)
        if isinstance(transition_id, str):
            transition_ids.add(transition_id)
        require(item.get("source_occurrence_id") in occurrence_ids, f"{prefix}.source_occurrence_id is unknown", errors)
        require(item.get("target_occurrence_id") in occurrence_ids, f"{prefix}.target_occurrence_id is unknown", errors)
        require(item.get("kind") in TRANSITION_KINDS, f"{prefix}.kind is invalid", errors)
        require(isinstance(item.get("label"), str) and bool(item.get("label")), f"{prefix}.label must be a non-empty string", errors)

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_manifest.py <manifest.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {path}")
    print("Structural validation only; semantic mappings still require model reasoning and human approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
