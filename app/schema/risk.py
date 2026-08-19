from pydantic import BaseModel


class RiskRequest(BaseModel):
    identity_target: str
    intent: str
    consent: str


class RiskResponse(BaseModel):
    risk_level: str
    risk_score: int