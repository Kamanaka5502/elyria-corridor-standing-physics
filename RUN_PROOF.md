# Run the Corridor Standing Proof

Built by **Elyria Systems — VA**.

Copyright (c) 2026 **Samantha Revita** and **Terry Snyder**. All rights reserved.

This repository is a protected public proof surface. It demonstrates the corridor-standing rule with public-safe synthetic data:

```text
valid endpoints do not prove valid transfer
```

## Clone

```bash
git clone https://github.com/Kamanaka5502/elyria-corridor-standing-physics.git
cd elyria-corridor-standing-physics
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Official CLI proof command

```bash
python corridor_cli.py financial
python corridor_cli.py financial --compact
```

## Direct proof command

```bash
python CORRIDOR_STANDING_ENGINE.py
```

Expected scenario:

```text
financial_settlement_corridor_under_degraded_transfer_relation
```

## Expected behavior

The synthetic scenario has valid source and destination boundaries but a degraded transfer relation and incomplete closure standing.

Expected consequence map:

```text
ALLOW: corridor audit snapshot
NARROW: review-only corridor scope
QUARANTINE: transfer payload or relation
ESCALATE: corridor authority review
REFUSE: financial settlement transfer
HALT: irreversible corridor effect path
REBOUND: last admissible corridor posture
```

Expected decision:

```text
REFUSE_NARROW_QUARANTINE_ESCALATE_REBOUND
```

## Run tests

```bash
python test_corridor_standing.py
```

The tests prove:

```text
valid endpoints do not admit degraded transfer
financial settlement corridor refuses transfer
safe audit action remains allowed
transfer payload/relation quarantines
corridor authority review escalates
irreversible corridor effect path halts
rebound posture is present
receipt/replay is deterministic
```

## GitHub Actions

The repository includes a proof workflow:

```text
.github/workflows/proof.yml
```

It runs the public proof CLI, proof engine, and deterministic test suite on push, pull request, and manual dispatch.

## Proof principle

Endpoint standing is necessary but not sufficient.

Transfer-relation standing must be resolved before consequence binds.

Closure standing is part of admissibility.

## Protected scope

This repository does not expose private law bundles, protected mathematical substrate, extreme-field substrate internals, production admissibility compiler logic, real financial/regulatory/energy data, NDA-bound formal proofs, or deployment-sensitive architecture.

See `PROTECTED_SCOPE.md`.
