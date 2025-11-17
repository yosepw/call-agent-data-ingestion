from fastapi import APIRouter, UploadFile, File, HTTPException
from ..models import SIPTrunk, CallTask, CSVUploadResponse

router = APIRouter()


@router.post("/sip/onboard")
async def onboard_trunk(trunk: SIPTrunk):
    return {"status": "ok", "trunk": trunk}


@router.post("/csv/upload", response_model=CSVUploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}


@router.post("/call/start")
async def start_call(task: CallTask):
    return {"status": "enqueued", "task": task}


@router.get("/health")
async def health():
    return {"ok": True}
