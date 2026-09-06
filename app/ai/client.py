import httpx

from app.core.config import settings


class AIClient:
    def __init__(self):
        self.base_url = settings.ai_service_url
        self.timeout = settings.ai_service_timeout

    def analyze_intent(self, prompt: str):
        return {
            "intent": "commercial_use",
            "confidence": 0.93
        }

    def analyze_risk(
        self,
        identity_target: str,
        intent: str,
        consent: str
    ):
        return {
            "risk_level": "high",
            "risk_score": 87
        }