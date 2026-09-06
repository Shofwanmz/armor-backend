from fastapi import APIRouter

from app.ai.client import AIClient
from app.schema.intent import (
    IntentRequest,
    IntentResponse,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

ai_client = AIClient()


@router.post(
    "/analyze-intent",
    response_model=IntentResponse
)
def analyze_intent(request: IntentRequest):
    result = ai_client.analyze_intent(request.prompt)

    return IntentResponse(
        intent=result["intent"],
        confidence=result["confidence"]
    )