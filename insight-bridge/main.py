from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
import jwt
import requests
import os
import uuid

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="InsightBridge - Security Enforcement")

JWT_SECRET = os.getenv("JWT_SECRET", "sovereign_fallback_secret")
FLOW_URL = os.getenv("FLOW_URL", "http://localhost:8002/telemetry/ingest")
INGESTION_TOKEN = os.getenv("INGESTION_TOKEN", "flow_secret_789")

class EnforceRequest(BaseModel):
    resource: str
    action: str

def emit_telemetry(event_type, decision_id, client_id, decision, reason=None):
    payload = {
        "event_type": event_type,
        "decision_id": decision_id,
        "client_id": client_id,
        "decision": decision,
        "reason": reason,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    headers = {"X-Insight-Token": INGESTION_TOKEN}
    try:
        response = requests.post(FLOW_URL, json=payload, headers=headers, timeout=2)
        return response.status_code == 200
    except Exception as e:
        print(f"Telemetry emission failed: {e}")
        return False

@app.post("/enforce")
async def enforce(request_body: EnforceRequest, authorization: str = Header(None)):
    decision_id = str(uuid.uuid4())
    client_id = "initial"
    
    # 0. Initial Telemetry
    emit_telemetry("request.received", decision_id, client_id, "PENDING", f"Resource: {request_body.resource}")
    
    # 1. Validate JWT (Fail-Closed)
    if not authorization or not authorization.startswith("Bearer "):
        emit_telemetry("auth.failure", decision_id, client_id, "DENY", "Missing or invalid Authorization header")
        raise HTTPException(status_code=401, detail="Authentication Required")
    
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"], audience="insight-bridge", leeway=10)
        client_id = payload.get("sub", "unknown")
    except jwt.ExpiredSignatureError:
        emit_telemetry("auth.failure", decision_id, client_id, "DENY", "Token expired")
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError as e:
        emit_telemetry("auth.failure", decision_id, client_id, "DENY", f"Invalid token: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid token")

    # 1.1 Auth Success Telemetry
    emit_telemetry("auth.success", decision_id, client_id, "PASS")

    # 2. Enforcement Logic (Deterministic)
    # Simple rule: client_id 'guest' cannot 'write'
    decision = "ALLOW"
    reason = "Policy matches"
    
    if client_id == "guest" and request_body.action == "write":
        decision = "DENY"
        reason = "Guest restricted from write operations"
    
    # 3. Emit Telemetry
    telemetry_sent = emit_telemetry("decision.made", decision_id, client_id, decision, reason)
    
    # 4. Mandatory Deterministic Response
    if decision == "DENY":
        raise HTTPException(status_code=403, detail=reason)
    
    return {
        "decision": decision,
        "decision_id": decision_id,
        "client_id": client_id,
        "telemetry_synced": telemetry_sent
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
