from pydantic import BaseModel


class DecisionRequest(BaseModel):
    identity_result: dict
    intent: str
    risk_level: str
    consent: str


class DecisionResponse(BaseModel):
    decision: str
    reason: str