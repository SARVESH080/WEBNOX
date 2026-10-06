"""
PhishGuard - FastAPI Detection Backend
---------------------------------------
Simple, lightweight API for analyzing URLs and returning phishing risk scores.
Run with: uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

from detector import analyze_url

app = FastAPI(
    title="WEBNOX Detection API",
    description="Rule-based real-time phishing URL risk analysis microservice",
    version="1.0.0",
)

# Enable CORS for local Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    url: str = Field(..., description="Target website URL to analyze", example="https://amazon-login-security.xyz")


class AnalyzeResponse(BaseModel):
    url: str
    risk_score: int
    verdict: str  # "safe" | "suspicious" | "phishing"
    confidence: int
    reasons: List[str]
    recommendation: str


@app.get("/")
def root():
    """Health check & API welcome message."""
    return {
        "status": "online",
        "service": "WEBNOX Phishing Detection API",
        "version": "1.0.0",
        "endpoint": "POST /analyze",
    }


@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest):
    """
    Receives a website URL, runs the rule-based phishing risk engine,
    and returns risk_score (0-100), verdict, confidence, and reasons.
    """
    target_url = payload.url.strip()

    if not target_url:
        raise HTTPException(status_code=400, detail="URL cannot be empty")

    result = analyze_url(target_url)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
