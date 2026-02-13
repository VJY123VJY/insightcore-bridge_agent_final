# TELEMETRY_CONTRACT.md

## Service: InsightFlow
**Purpose:** Telemetry Ingestion Surface for security events.

### Endpoint: `POST /telemetry/ingest`
**Description:** Receives and logs deterministic enforcement events.

**Payload Schema:**
```json
{
  "event_type": "request.received | auth.success | auth.failure | decision.made",
  "decision_id": "uuid",
  "client_id": "string",
  "decision": "ALLOW | DENY",
  "reason": "string (optional)",
  "timestamp": "ISO8601"
}
```

**Authentication:**
- Signed ingestion (HMAC-SHA256) or Service Token in `X-Insight-Token` header.

**Persistence:**
- Events are logged to `insight_flow.log` and forwarded to Bucket.
