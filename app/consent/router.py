from fastapi import APIRouter, HTTPException

from app.schema.consent import (
    ConsentRequest,
    ConsentRequestResponse,
    ConsentStatusResponse,
    ConsentRespondRequest,
    ConsentRespondResponse,
)

router = APIRouter(
    prefix="/consent",
    tags=["Consent"]
)


consent_store = {}


@router.post(
    "/request",
    response_model=ConsentRequestResponse
)
def request_consent(request: ConsentRequest):
    consent_id = f"CONSENT-{len(consent_store) + 1:03d}"

    consent_store[consent_id] = {
        "consent_id": consent_id,
        "requester_id": request.requester_id,
        "owner_id": request.owner_id,
        "intent": request.intent,
        "status": "pending",
    }

    return ConsentRequestResponse(
        consent_id=consent_id,
        status="pending",
        message="Consent request created successfully"
    )


@router.get(
    "/status",
    response_model=ConsentStatusResponse
)
def get_consent_status(consent_id: str):
    consent = consent_store.get(consent_id)

    if not consent:
        raise HTTPException(
            status_code=404,
            detail="Consent request not found"
        )

    return ConsentStatusResponse(**consent)


@router.post(
    "/respond",
    response_model=ConsentRespondResponse
)
def respond_consent(request: ConsentRespondRequest):
    consent = consent_store.get(request.consent_id)

    if not consent:
        raise HTTPException(
            status_code=404,
            detail="Consent request not found"
        )

    if request.response not in ["approved", "denied"]:
        raise HTTPException(
            status_code=400,
            detail="Response must be 'approved' or 'denied'"
        )

    consent["status"] = request.response

    return ConsentRespondResponse(
        consent_id=request.consent_id,
        status=request.response,
        message="Consent response recorded successfully"
    )