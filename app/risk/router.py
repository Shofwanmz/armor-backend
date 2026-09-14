from fastapi import APIRouter

from app.ai.client import AIClient
from app.schema.risk import (
    RiskRequest,
    RiskResponse,
)

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)

ai_client = AIClient()


@router.post(
    "",
    response_model=RiskResponse
)
def analyze_risk(request: RiskRequest):
    result = ai_client.analyze_risk(
        identity_target=request.identity_target,
        intent=request.intent,
        consent=request.consent
    )

    return RiskResponse(
        risk_level=result["risk_level"],
        risk_score=result["risk_score"]
    )