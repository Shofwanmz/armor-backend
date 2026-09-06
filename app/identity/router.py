from fastapi import APIRouter

from app.schema.identity import (
    IdentityEnrollRequest,
    IdentityEnrollResponse,
    IdentityVerifyRequest,
    IdentityVerifyResponse,
    IdentityProfileResponse,
)

router = APIRouter(
    prefix="/identity",
    tags=["Identity"]
)

@router.post(
    "/enroll",
    response_model=IdentityEnrollResponse
)
def enroll_identity(request: IdentityEnrollRequest):
    return IdentityEnrollResponse(
        identity_id=request.identity_id,
        status="enrolled",
        message="Identity enrolled successfully"
    )

@router.post(
    "/verify",
    response_model=IdentityVerifyResponse
)
def verify_identity(request: IdentityVerifyRequest):
    return IdentityVerifyResponse(
        match=True,
        confidence=0.95,
        identity_id=request.identity_id,
        status="verified"
    )

@router.get(
    "/profile",
    response_model=IdentityProfileResponse
)
def get_identity_profile():
    return IdentityProfileResponse(
        identity_id="ARMOR-001",
        status="active",
        enrolled=True
    )