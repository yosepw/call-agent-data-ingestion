from fastapi import FastAPI, Depends, Header, HTTPException, status
from pydantic import BaseModel
from typing import Any, Dict, Optional
from datetime import datetime
import os

from app.db import PostgreSQLConnector


class IngestionPayload(BaseModel):
    user_id: str
    timestamp: datetime
    data_payload: Dict[str, Any]


app = FastAPI(title="Data Ingestion Service")


async def get_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing API Key")
    expected = os.getenv("API_KEY", "PLACEHOLDER_API_KEY")
    if x_api_key != expected:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    return x_api_key


@app.on_event("startup")
async def on_startup():
    app.state.db = PostgreSQLConnector()
    await app.state.db.connect()


@app.on_event("shutdown")
async def on_shutdown():
    if hasattr(app.state, "db") and app.state.db:
        await app.state.db.close()


@app.post("/api/v1/data_ingestion", status_code=201)
async def ingest(payload: IngestionPayload, api_key: str = Depends(get_api_key)):
    try:
        record_id = await app.state.db.insert_record(
            payload.user_id, payload.timestamp, payload.data_payload
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Database error while inserting record")
    return {"id": record_id}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
