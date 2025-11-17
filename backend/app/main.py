from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .api import calls

app = FastAPI(title="call-agent-data-ingestion")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calls.router, prefix="/api")

# Serve the minimal frontend (mounted at /)
app.mount("/", StaticFiles(directory="./frontend", html=True), name="frontend")


@app.get("/healthz")
async def health():
    return {"status": "ok"}
