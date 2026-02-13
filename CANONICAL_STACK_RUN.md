# CANONICAL_STACK_RUN.md

## Startup Sequence
1. **InsightFlow**: Starts first to listen for telemetry.
2. **InsightCore**: Starts second to enable token issuance.
3. **InsightBridge**: Starts last to enforce boundaries.

## Commands (Bash/Terminal)
```bash
# Terminal 1: InsightFlow
cd insight-flow && python main.py

# Terminal 2: InsightCore
cd insight-core && python main.py

# Terminal 3: InsightBridge
cd insight-bridge && python main.py
```

## Validation Flow
1. Client requests JWT from Core.
2. Client sends request to Bridge with JWT.
3. Bridge validates JWT via local key.
4. Bridge makes ALLOW/DENY decision.
5. Bridge sends telemetry to Flow.
6. Flow persists decision to Bucket.

## Determinism Proof
- Identical inputs produce identical decision IDs in telemetry and bucket.
- No alternate run paths; all requests must have a valid JWT.
