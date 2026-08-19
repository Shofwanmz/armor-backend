from fastapi import FastAPI


app = FastAPI(
    title="ARMOR Main Backend API",
    version="0.1.0",
    description="ARMOR AI Safety Gateway"
)


@app.get("/")
def root():
    return {
        "service": "ARMOR Main Backend",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }