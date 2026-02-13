# STACK_ARCHITECTURE.md

## High-Level Design
The Sovereign Stack is a distributed security architecture designed for deterministic enforcement and auditable telemetry.

### Components:
1. **InsightCore (Issuer):** The root of trust. Handles identity and signs tokens.
2. **InsightBridge (Enforcer):** The security spine. Validates tokens locally and enforces policy.
3. **InsightFlow (Observer):** The telemetry sink. Collects events for real-time monitoring.
4. **Bucket (Historian):** The immutable storage. Persists decisions for audit and provenance.

## Boundary Security
- No service trusts another without a valid JWT.
- Keys are rotated via environment injection.
- Fail-closed logic ensures that an unauthenticated request never reaches a resource.
