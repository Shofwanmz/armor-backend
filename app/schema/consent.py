from pydantic import BaseModel


class ConsentRequest(BaseModel):
    identity_id: str
    request_id: str


class ConsentResponse(BaseModel):
    status: str