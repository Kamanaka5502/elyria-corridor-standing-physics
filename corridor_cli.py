#!/usr/bin/env python3
"""
Elyria Corridor Standing CLI
Built by Elyria Systems — VA

Public-safe command surface for corridor-standing proof scenarios.
"""
from __future__ import annotations

import argparse
import json
from typing import Any, Dict

from CORRIDOR_STANDING_ENGINE import demo_financial_settlement_corridor


SCENARIOS = {
    "financial": demo_financial_settlement_corridor,
}


def run_scenario(name: str) -> Dict[str, Any]:
    if name not in SCENARIOS:
        raise SystemExit(f"Unknown scenario: {name}. Valid options: {', '.join(sorted(SCENARIOS))}")
    return SCENARIOS[name]()


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="corridor-standing",
        description="Run public-safe Elyria corridor-standing proof scenarios.",
    )
    parser.add_argument(
        "scenario",
        choices=sorted(SCENARIOS.keys()),
        help="Proof scenario to run.",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Emit compact JSON instead of pretty JSON.",
    )
    args = parser.parse_args()

    result = run_scenario(args.scenario)
    if args.compact:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
