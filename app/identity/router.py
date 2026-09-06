from fastapi import APIRouter

from app.schema.identity import (
    IdentityEnrollRequest,
    IdentityEnrollResponse,
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