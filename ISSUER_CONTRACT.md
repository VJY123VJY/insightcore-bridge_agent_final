# ISSUER_CONTRACT.md

## Service: InsightCore
**Purpose:** Sovereign JWT Issuer for BHIV Ecosystem.

### Endpoint: `POST /auth/issue`
**Description:** Issues a cryptographically signed JWT for service authentication.

**Request Body:**
```json
{
  "client_id": "string",
  "client_secret": "string"
}
```

**Claims Structure:**
- `iss`: sovereign-core
- `aud`: insight-bridge
- `sub`: client_id
- `jti`: Unique token identifier (UUID4)
- `exp`: Expiration time (1 hour from issue)
- `iat`: Issued at time

**Security:**
- Signing Algorithm: HS256 (Environment-driven secret)
- Fail-Closed: Invalid secrets return 401.

**Environment Variables:**
- `JWT_SECRET`: Secret key for signing.
- `CORE_PORT`: Default 8001.
