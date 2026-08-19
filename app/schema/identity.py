from pydantic import BaseModel


class IdentityVerifyRequest(BaseModel):
    identity_id: str
    image: str


class IdentityVerifyResponse(BaseModel):
    match: bool
    confidence: float
    identity_id: str
    status: str