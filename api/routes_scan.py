from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.usecases import resolve_qr, resolve_rfid_batch

router = APIRouter()

class QRIn(BaseModel):
    qr: str

class RFIDBatchIn(BaseModel):
    rfids: list[str]

@router.post("/qr")
def scan_qr(payload: QRIn):
    item = resolve_qr(payload.qr)
    if not item:
        raise HTTPException(status_code=404, detail="QR not found")
    return item

@router.post("/rfid")
def scan_rfid(payload: RFIDBatchIn):
    return {"matches": resolve_rfid_batch(payload.rfids)}
