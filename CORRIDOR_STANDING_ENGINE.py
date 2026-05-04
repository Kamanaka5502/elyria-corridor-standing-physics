#!/usr/bin/env python3
"""
Elyria Corridor Standing Engine
Built by Elyria Systems — VA

Public-safe synthetic proof engine for corridor standing.

Category rule:
valid endpoints do not prove valid transfer.
The transfer relation itself must retain standing.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any, Dict, List


@dataclass(frozen=True)
class CorridorRequest:
    corridor_id: str
    domain: str
    source_boundary: str
    destination_boundary: str
    requested_transfer: str
    protected_effect: str


@dataclass(frozen=True)
class CorridorStandingVector:
    source_standing: float
    destination_standing: float
    transfer_relation: float
    ramp_lawfulity: float
    stability_bound: float
    phase_coherence: float
    transfer_continuity: float
    causal_admissibility: float
    debt_bound: float
    authority_validity: float
    closure_standing: float
    replayability: float

    def normalized(self) -> Dict[str, float]:
        return asdict(self)


@dataclass(frozen=True)
class CorridorResolution:
    decision: str
    allowed: List[str]
    narrowed: List[str]
    quarantined: List[str]
    escalated: List[str]
    refused: List[str]
    halted: List[str]
    rebound: List[str]
    standing_margin: float
    reasons: List[str]
    receipt: Dict[str, str]


def stable_hash(obj: Any) -> str:
    encoded = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


class CorridorStandingEngine:
    law_id = "ELYRIA_CORRIDOR_STANDING_PUBLIC_SAFE_V1"
    law_version = "1.0.0"
    threshold = 0.50

    def evaluate(self, request: CorridorRequest, standing: CorridorStandingVector) -> CorridorResolution:
        v = standing.normalized()
        standing_margin = round(min(v.values()) - self.threshold, 3)

        threshold_messages = {
            "source_standing": "source boundary standing degraded",
            "destination_standing": "destination boundary standing degraded",
            "transfer_relation": "transfer relation lacks standing",
            "ramp_lawfulity": "ramp lawfulity below corridor absorption threshold",
            "stability_bound": "corridor stability bound degraded",
            "phase_coherence": "phase/coherence relation degraded",
            "transfer_continuity": "transfer continuity incomplete",
            "causal_admissibility": "causal admissibility insufficient",
            "debt_bound": "consequence debt exceeds admissible bound",
            "authority_validity": "authority validity degraded at transfer",
            "closure_standing": "closure standing incomplete",
            "replayability": "replayability below proof threshold",
        }
        reasons = [message for key, message in threshold_messages.items() if v[key] < self.threshold]

        allowed: List[str] = []
        narrowed: List[str] = []
        quarantined: List[str] = []
        escalated: List[str] = []
        refused: List[str] = []
        halted: List[str] = []
        rebound: List[str] = []

        if standing_margin >= 0:
            decision = "TRANSFER"
            allowed.append(request.requested_transfer)
        else:
            decision = "REFUSE_NARROW_QUARANTINE_ESCALATE_REBOUND"
            allowed.append("corridor_audit_snapshot")
            narrowed.append("review_only_corridor_scope")
            refused.append(request.requested_transfer)
            rebound.append("last_admissible_corridor_posture")

            if v["transfer_relation"] < self.threshold or v["transfer_continuity"] < self.threshold:
                quarantined.append("transfer_payload_or_relation")
            if v["authority_validity"] < self.threshold or v["closure_standing"] < self.threshold:
                escalated.append("corridor_authority_review")
            if v["closure_standing"] < self.threshold or v["causal_admissibility"] < self.threshold:
                halted.append("irreversible_corridor_effect_path")

        decision_payload = {
            "law_id": self.law_id,
            "law_version": self.law_version,
            "request": asdict(request),
            "standing_vector": v,
            "decision": decision,
            "standing_margin": standing_margin,
            "allowed": allowed,
            "narrowed": narrowed,
            "quarantined": quarantined,
            "escalated": escalated,
            "refused": refused,
            "halted": halted,
            "rebound": rebound,
            "reasons": reasons,
        }

        receipt = {
            "law_hash": stable_hash({"law_id": self.law_id, "law_version": self.law_version}),
            "request_hash": stable_hash(asdict(request)),
            "standing_vector_hash": stable_hash(v),
            "decision_hash": stable_hash(decision_payload),
            "replay_token": stable_hash({"replay": decision_payload}),
        }

        return CorridorResolution(
            decision=decision,
            allowed=allowed,
            narrowed=narrowed,
            quarantined=quarantined,
            escalated=escalated,
            refused=refused,
            halted=halted,
            rebound=rebound,
            standing_margin=standing_margin,
            reasons=reasons,
            receipt=receipt,
        )


def demo_financial_settlement_corridor() -> Dict[str, Any]:
    request = CorridorRequest(
        corridor_id="FIN-SETTLE-CORRIDOR-VA-001",
        domain="financial_settlement_corridor",
        source_boundary="synthetic_sender_account_boundary",
        destination_boundary="synthetic_receiver_account_boundary",
        requested_transfer="execute_financial_settlement_transfer",
        protected_effect="settlement_transfer",
    )
    standing = CorridorStandingVector(
        source_standing=0.82,
        destination_standing=0.84,
        transfer_relation=0.37,
        ramp_lawfulity=0.62,
        stability_bound=0.58,
        phase_coherence=0.55,
        transfer_continuity=0.44,
        causal_admissibility=0.61,
        debt_bound=0.46,
        authority_validity=0.49,
        closure_standing=0.41,
        replayability=0.93,
    )
    resolution = CorridorStandingEngine().evaluate(request, standing)
    return {
        "engine": "Elyria Corridor Standing Engine",
        "built_by": "Elyria Systems — VA",
        "scenario": "financial_settlement_corridor_under_degraded_transfer_relation",
        "request": asdict(request),
        "standing_vector": standing.normalized(),
        "resolution": asdict(resolution),
    }


if __name__ == "__main__":
    print(json.dumps(demo_financial_settlement_corridor(), indent=2, sort_keys=True))
