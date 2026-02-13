# OBSERVABILITY_STACK.md

## Traceability Map
A single request can be traced across the stack using the `decision_id`.

1. **InsightBridge Log:**
   `[ENFORCE] decision_id="uuid-123" client_id="user-a" action="read" decision="ALLOW"`
2. **InsightFlow Log:**
   `[TELEMETRY] decision.made: ALLOW for user-a (ID: uuid-123)`
3. **Bucket Artifact:**
   `bucket/decision_uuid-123.json`

## Log Structure
All services log to standard out in a deterministic, parsable format.
- Format: `[SERVICE] [LEVEL] [EVENT] metadata...`
