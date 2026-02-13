from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import json
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="InsightFlow - Telemetry Ingestion")

# Simplified ingestion auth for demo
INGESTION_TOKEN = os.getenv("INGESTION_TOKEN", "flow_secret_789")
BUCKET_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bucket"))

class TelemetryEvent(BaseModel):
    event_type: str
    decision_id: str
    client_id: str
    decision: str
    reason: str = None
    timestamp: str

@app.post("/telemetry/ingest")
async def ingest_telemetry(event: TelemetryEvent, x_insight_token: str = Header(None)):
    if x_insight_token != INGESTION_TOKEN:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid Ingestion Token")
    
    # Log to console
    print(f"[TELEMETRY] {event.event_type}: {event.decision} for {event.client_id} (ID: {event.decision_id})")
    
    # Persist to Bucket (Day 1-c)
    # Sanitize timestamp for filename
    ts_clean = event.timestamp.replace(":", "-").replace(".", "-")
    filename = f"decision_{event.decision_id}_{ts_clean}.json"
    filepath = os.path.join(BUCKET_DIR, filename)
    
    artifact = {
        "decision_id": event.decision_id,
        "timestamp": event.timestamp,
        "client_id": event.client_id,
        "decision": event.decision,
        "metadata": {
            "issuer": "sovereign-core",
            "enforcer": "insight-bridge",
            "reason": event.reason
        }
    }
    
    try:
        with open(filepath, "w") as f:
            json.dump(artifact, f, indent=2)
    except Exception as e:
        print(f"Failed to persist artifact: {e}")
        raise HTTPException(status_code=500, detail="Artifact persistence failure")

    return {"status": "ingested", "decision_id": event.decision_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
