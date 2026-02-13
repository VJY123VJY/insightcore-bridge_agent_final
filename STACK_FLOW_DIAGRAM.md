# STACK_FLOW_DIAGRAM.md

## Sequence Flow

```text
Client          InsightCore        InsightBridge        InsightFlow        Bucket
  |                  |                   |                   |               |
  |--- /auth/issue ->|                   |                   |               |
  |<-- Valid JWT ----|                   |                   |               |
  |                  |                   |                   |               |
  |---- /enforce (JWT) ----------------->|                   |               |
  |                  |            [Validate JWT]             |               |
  |                  |            [Make Decision]            |               |
  |                  |                   |--- /telemetry --->|               |
  |                  |                   |                   |---- Store --->|
  |<-- Decision result ------------------|                   |               |
```

## Data Lifecycle
1. **Identity Phase:** Core produces a signed claim.
2. **Enforcement Phase:** Bridge validates the claim and applies logic.
3. **Observability Phase:** Flow converts the event into a persistent artifact.
