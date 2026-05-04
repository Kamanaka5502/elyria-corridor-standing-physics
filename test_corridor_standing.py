#!/usr/bin/env python3
"""
Elyria Corridor Standing Tests
Built by Elyria Systems — VA

Public-safe tests for the first synthetic corridor proof surface.
"""
from __future__ import annotations

from CORRIDOR_STANDING_ENGINE import demo_financial_settlement_corridor


def test_financial_settlement_refuses_degraded_transfer_relation():
    proof = demo_financial_settlement_corridor()
    resolution = proof["resolution"]

    assert resolution["decision"] == "REFUSE_NARROW_QUARANTINE_ESCALATE_REBOUND"
    assert "execute_financial_settlement_transfer" in resolution["refused"]
    assert "corridor_audit_snapshot" in resolution["allowed"]
    assert "review_only_corridor_scope" in resolution["narrowed"]
    assert "transfer_payload_or_relation" in resolution["quarantined"]
    assert "corridor_authority_review" in resolution["escalated"]
    assert "irreversible_corridor_effect_path" in resolution["halted"]
    assert "last_admissible_corridor_posture" in resolution["rebound"]
    assert resolution["standing_margin"] < 0


def test_financial_settlement_replay_is_deterministic():
    first = demo_financial_settlement_corridor()
    second = demo_financial_settlement_corridor()

    assert first["resolution"]["receipt"] == second["resolution"]["receipt"]
    assert first["resolution"]["receipt"]["replay_token"] == second["resolution"]["receipt"]["replay_token"]


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-q"]))
