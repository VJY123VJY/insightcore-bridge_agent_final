🛡️ Sovereign Security Stack

Core → Bridge → Flow → Bucket
A deterministic, sovereign, auditable end-to-end JWT + Telemetry architecture.

📌 Overview

This project activates a full sovereign security loop:

InsightCore (JWT Issuer)
        ↓
InsightBridge (Enforcement Layer)
        ↓
InsightFlow (Telemetry Surface)
        ↓
Bucket (Artifact Persistence)


This is NOT a feature implementation.
This is a deterministic system activation.

🔐 InsightCore — Sovereign JWT Issuer
Purpose

Canonical /auth/issue endpoint

Environment-driven signing

Strict issuer contract

Deterministic claim structure

🚀 How to Run InsightCore
1️⃣ Navigate to folder
cd insight-core

2️⃣ Install dependencies
pip install fastapi uvicorn python-dotenv pyjwt

3️⃣ Create .env file
JWT_SECRET=bhiv_sovereign_2026_key_!!
CORE_CLIENT_SECRET=bridge_secret_123
INGESTION_TOKEN=flow_secret_789

4️⃣ Start server
uvicorn main:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🔑 POST /auth/issue
Request Body
{
  "client_id": "bridge-agent",
  "client_secret": "bridge_secret_123"
}

Response
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

🧾 JWT Claim Structure
Claim	Purpose
iss	sovereign-core
aud	insight-bridge
sub	client_id
jti	unique token ID
iat	issued at
exp	expiry (1 hour)
🌉 InsightBridge — Enforcement Layer
Responsibilities

Validates JWT issued by Core

Rejects tampered or expired tokens

No debug bypass allowed

No alternate run paths

Fail-closed architecture

Enforcement Guarantees

✔ Only accepts tokens signed by JWT_SECRET
✔ Audience must equal insight-bridge
✔ Issuer must equal sovereign-core

🌊 InsightFlow — Telemetry Ingestion Surface
Purpose

Public ingestion endpoint

Validates ingestion token

Forwards artifacts to Bucket

No silent failures

🪣 Bucket — Artifact Persistence
Purpose

Stores telemetry decisions

Stores failure artifacts

Ensures audit traceability

🧱 System Guarantees

This stack ensures:

Deterministic startup

No secret hardcoding

No enforcement bypass

No speculative architecture

Environment-driven configuration

Observable failure modes

Auditable decision artifacts

📁 Project Structure
insight_bridge_agent_final/
│
├── insight-core/
│   └── main.py
│
├── insight-bridge/
│   └── main.py
│
├── insight-flow/
│   └── main.py
│
├── bucket/
│   └── decision_*.json
│
└── README.md

🛑 What Is NOT Allowed

Changing Bridge enforcement guarantees

Debug authentication bypass

Hardcoded secrets

Alternate execution paths

Silent telemetry failure

🎯 Target Outcome

A real, sovereign, auditable stack that:

Works outside isolation

Enforces JWT contract strictly

Persists telemetry artifacts

Demonstrates deterministic behavior

🧠 Owner

Vijay — Full Stack Integration Owner

Responsible for:

Core JWT issuer

Bridge wiring

Flow ingestion stability

End-to-end validation proof

📌 Stability Target

Real effort window: 1–2 focused days

Internal stability: 12–18 hours

Zero drift allowed
