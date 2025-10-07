from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.usecases import items_service

router = APIRouter()

class ItemIn(BaseModel):
    sku: str
    name: str
    qty: int = 0
    location: str = "RECEIVING"
    qr: Optional[str] = None
    rfid: Optional[str] = None

@router.post("", status_code=201)
def create_item(payload: ItemIn):
    if items_service.get(payload.sku):
        raise HTTPException(status_code=409, detail="Item already exists")
    items_service.create(
        sku=payload.sku, name=payload.name, qty=payload.qty,
        location=payload.location, qr=payload.qr, rfid=payload.rfid
    )
    return {"ok": True}

@router.get("/{sku}")
def get_item(sku: str):
    it = items_service.get(sku)
    if not it:
        raise HTTPException(status_code=404, detail="Not found")
    return it
