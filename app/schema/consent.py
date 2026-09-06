from pydantic import BaseModel


class ConsentRequest(BaseModel):
    requester_id: str
    owner_id: str
    intent: str


class ConsentRequestResponse(BaseModel):
    consent_id: str
    status: str
    message: str


class ConsentStatusResponse(BaseModel):
    consent_id: str
    requester_id: str
    owner_id: str
    intent: str
    status: str


class ConsentRespondRequest(BaseModel):
    consent_id: str
    response: str


class ConsentRespondResponse(BaseModel):
    consent_id: str
    status: str
    message: str