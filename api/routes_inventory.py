from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.usecases import move_item, inventory_by_location

router = APIRouter()

class MoveIn(BaseModel):
    sku: str
    from_loc: str
    to_loc: str
    qty: int

@router.post("/move")
def move(payload: MoveIn):
    try:
        mv = move_item(payload.sku, payload.from_loc, payload.to_loc, payload.qty)
        return {"moved": mv}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{location}")
def by_location(location: str):
    return {"items": inventory_by_location(location)}
