from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Asaoka Consult API")

class ChatIn(BaseModel):
    user_id: str
    message: str
    session_id: str | None = None

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/v1/chat")
def chat(payload: ChatIn, x_api_key: str | None = Header(None)):
    if not x_api_key:
        raise HTTPException(401, "missing X-API-Key")
    return {
        "reply": "API起動OK（仮応答）",
        "usage": {"prompt": 0, "completion": 0, "jpy_cost": 0.0},
        "limits": {"daily_remaining": 0, "tier": "free"},
        "session_id": payload.session_id or "s_dummy"
    }
