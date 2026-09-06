from fastapi import FastAPI

from app.core.config import settings
from app.identity.router import router as identity_router
from app.intent.router import router as intent_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="ARMOR AI Safety Gateway"
)

app.include_router(identity_router)
app.include_router(intent_router)

@app.get("/")
def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }