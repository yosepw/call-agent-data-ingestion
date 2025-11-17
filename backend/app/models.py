from pydantic import BaseModel, Field
from typing import Optional


class SIPTrunk(BaseModel):
    name: str
    sip_url: str
    username: Optional[str]
    password: Optional[str]
    codec: Optional[str] = "opus"
    dtmf: Optional[str] = "RFC2833"
    whitelist_ips: Optional[str]


class CallTask(BaseModel):
    task_id: str
    script: str
    concurrency: int = Field(default=1, ge=1)
    trunk_name: Optional[str]


class CSVUploadResponse(BaseModel):
    filename: str
    size: int


class Transcript(BaseModel):
    call_id: str
    text: str
    speaker: str
    timestamp: float
