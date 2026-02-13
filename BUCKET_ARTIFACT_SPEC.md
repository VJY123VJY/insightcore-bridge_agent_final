# BUCKET_ARTIFACT_SPEC.md

## Service: Bucket
**Purpose:** Immutable Artifact Persistence.

### Storage Structure:
Artifacts are stored as JSON files in a flattened structure for deterministic retrieval.

**Filename Pattern:**
`decision_{decision_id}_{timestamp}.json`

**Content Schema:**
```json
{
  "decision_id": "uuid",
  "timestamp": "ISO8601",
  "client_id": "string",
  "decision": "ALLOW | DENY",
  "metadata": {
    "issuer": "sovereign-core",
    "enforcer": "insight-bridge"
  }
}
```

**Consistency:**
- Atomic write-and-flush.
- Read-only once written.
