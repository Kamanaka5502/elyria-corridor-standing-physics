# Scenario Index

Built by **Elyria Systems — VA**.

Copyright (c) 2026 **Samantha Revita** and **Terry Snyder**. All rights reserved.

This index separates active public-safe corridor scenarios from future protected lanes.

## Active public lanes

| Scenario ID | Domain | Protected effect | Purpose |
|---|---|---|---|
| `financial_settlement_corridor` | Financial settlement | `settlement_transfer` | Show that valid sender and valid receiver do not prove valid settlement relation. |
| `regulated_data_transfer_corridor` | Regulated data | `external_data_transfer` | Show that lawful source and approved destination do not prove transfer standing. |
| `ai_action_corridor` | AI agent operations | `autonomous_tool_effect` | Show that delegated authority and valid tool endpoint do not prove action-corridor standing. |
| `energy_transfer_corridor` | Energy systems | `energy_transfer` | Show that valid generation and valid load do not prove transfer stability or closure standing. |

## Future protected lane

| Scenario ID | Domain | Protected effect | Status |
|---|---|---|---|
| `extreme_field_transfer_corridor` | Extreme-field physics | `field_transfer_event` | Future controlled-review lane only. Not active public proof. |

## Active scenario behavior

### Financial settlement corridor

```text
Input condition:
  sender standing appears valid
  receiver standing appears valid
  custody relation degraded
  liquidity transfer relation unstable
  reversal path incomplete

Expected result:
  ALLOW settlement audit snapshot
  NARROW to review-only settlement state
  ESCALATE treasury / settlement authority
  REFUSE settlement transfer
  REBOUND to last admissible settlement posture
```

### Regulated data transfer corridor

```text
Input condition:
  source system valid
  destination workspace approved historically
  purpose limitation degraded
  minimization incomplete
  transfer relation has elevated exfiltration pressure
  closure / deletion standing incomplete

Expected result:
  ALLOW metadata-only audit trace
  NARROW to field-minimized transfer review
  QUARANTINE transfer payload
  ESCALATE data protection review
  REFUSE external data transfer
```

### AI action corridor

```text
Input condition:
  agent has delegated task authority
  tool endpoint exists
  context standing has degraded
  consequence scope expanded
  rollback relation incomplete

Expected result:
  ALLOW observation and receipt
  NARROW tool scope
  ESCALATE human authority
  REFUSE autonomous tool effect
  HALT irreversible action path
```

### Energy transfer corridor

```text
Input condition:
  generation source valid
  load destination valid
  ramp exceeds corridor absorption
  phase / grid coherence degraded
  closure path unstable

Expected result:
  ALLOW telemetry snapshot
  NARROW to simulation-only transfer
  ESCALATE grid / system authority
  REFUSE energy transfer
  HALT unsafe ramp path
```

## Scenario admission rule

A scenario may enter this public repo only if it satisfies:

```text
synthetic data only
no production credentials
no live endpoint references
no customer-specific policies
no deployment-sensitive architecture
no private law-bundle disclosure
clear source boundary
clear destination boundary
clear transfer relation
clear closure condition
clear consequence map
receipt/replay path planned
```

## Consequence map vocabulary

```text
FORM        corridor may form within verified scope
TRANSFER    relation may carry consequence within verified scope
CLOSE       closure standing is satisfied
SETTLE      downstream settlement may bind
NARROW      reduced corridor scope only
QUARANTINE  unstable payload/relation isolated
ESCALATE    higher authority or witness required
REFUSE      no current standing to transfer
HALT        unsafe transfer path stopped
TERMINATE   active corridor must close/terminate safely
REBOUND     return to nearest lawful posture
```

## Public safety boundary

This scenario index is not a production policy catalog. It is a public proof map for reviewers. Production scenarios, customer policies, private weights, protected law bundles, extreme-field internals, and sensitive deployment details remain outside this repository.
