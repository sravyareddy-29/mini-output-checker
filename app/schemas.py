from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CheckResult(BaseModel):
    name: str
    fired: bool
    reason: str | None = None


class AnalysisResponse(BaseModel):
    trust_score: int
    verdict: str
    checks: list[CheckResult]