from pydantic import BaseModel

class IdentityEnrollRequest(BaseModel):
    identity_id: str
    image: str

class IdentityEnrollResponse(BaseModel):
    identity_id: str
    status: str
    message: str

class IdentityVerifyRequest(BaseModel):
    identity_id: str
    image: str

class IdentityVerifyResponse(BaseModel):
    match: bool
    confidence: float
    identity_id: str
    status: str

class IdentityProfileResponse(BaseModel):
    identity_id: str
    status: str
    enrolled: bool

class IdentityLockRequest(BaseModel):
    identity_id: str

class IdentityLockResponse(BaseModel):
    identity_id: str
    status: str
    message: str
