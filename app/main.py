from fastapi import FastAPI

from app.schemas import TextRequest
from app.checker import analyze_text

app = FastAPI(
    title="Mini Output Checker",
    description="Checks AI-generated text for trust signals and suspicious patterns.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mini Output Checker API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/check")
def check_text(request: TextRequest):
    return analyze_text(request.text)