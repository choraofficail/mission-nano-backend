from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any

app = FastAPI(
    title="Mission Nano Backend",
    description="FastAPI backend created by Himmat",
    version="2.0.0"
)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Mission Nano Backend running ✅"}

class AIRequest(BaseModel):
    prompt: str = Field(..., min_length=5, max_length=500, example="Explain Python in simple terms.")
    user_id: str = Field("guest", example="himmat123")

@app.post("/ai/chat", response_model=Dict[str, Any])
async def ai_chat(data: AIRequest, request: Request):
    user_prompt = data.prompt
    user_id = data.user_id

    if "bad word" in user_prompt.lower():
        raise HTTPException(status_code=400, detail="Inappropriate content detected.")

    ai_reply = f"Hi {user_id}, I got your message: '{user_prompt}'. Processing it now."
    return {
        "status": "success",
        "user_id": user_id,
        "reply": ai_reply,
        "prompt_length": len(user_prompt)
    }
  
