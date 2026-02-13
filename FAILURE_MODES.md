# FAILURE_MODES.md

## Security Fail-Closed Scenarios

| Scenario | Behavior | Result | Reason |
| --- | --- | --- | --- |
| Expired JWT | InsightBridge rejects | 401 Unauthorized | JWT `exp` claim check |
| Tampered JWT | InsightBridge rejects | 401 Unauthorized | HMAC signature mismatch |
| Missing Token | InsightBridge rejects | 401 Unauthorized | Security boundary requirement |
| Telemetry Outage | InsightBridge proceeds | 200 OK | Telemetry is best-effort but logged locally |
| Bucket Outage | InsightFlow errors | 500 Internal Error | Persistence is mandatory for flow |
| Replay Attempt | Replay guard check | DENY (not implemented in this sprint, but planned) | |

## Deterministic Restart
- Services use environment variables only.
- No local state that isn't persisted to Bucket.
- Clean startup sequence ensures all boundaries are active before client traffic.
