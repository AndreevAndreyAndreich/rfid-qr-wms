from typing import Dict, List, Optional
from domain.entities import Item
from infra.repos import items_repo, tags_repo

class ItemsService:
    def create(self, sku: str, name: str, qty: int = 0, location: str = "RECEIVING",
               qr: Optional[str] = None, rfid: Optional[str] = None) -> None:
        item = Item(sku=sku, name=name, qty=qty, location=location, qr=qr, rfid=rfid)
        items_repo.create(item)
        if qr:
            tags_repo.bind_qr(sku, qr)
        if rfid:
            tags_repo.bind_rfid(sku, rfid)

    def get(self, sku: str) -> Optional[Dict]:
        it = items_repo.get(sku)
        if not it:
            return None
        return it.__dict__

    def by_location(self, location: str) -> List[Dict]:
        return [i.__dict__ for i in items_repo.by_location(location)]

items_service = ItemsService()

def resolve_qr(qr: str) -> Optional[Dict]:
    sku = tags_repo.get_by_qr(qr)
    if not sku:
        return None
    return items_service.get(sku)

def resolve_rfid_batch(rfids: List[str]) -> List[Dict]:
    out = []
    for tid in rfids:
        sku = tags_repo.get_by_rfid(tid)
        if sku:
            obj = items_service.get(sku)
            if obj:
                out.append(obj)
    return out

def move_item(sku: str, from_loc: str, to_loc: str, qty: int) -> Dict:
    it = items_repo.get(sku)
    if not it:
        raise ValueError("Item not found")
    if it.location != from_loc:
        raise ValueError("Item not in the specified from_loc")
    if qty <= 0 or qty > it.qty:
        raise ValueError("Invalid qty")
    # simple move: decrease from_loc qty and move location if fully moved
    if qty == it.qty:
        it.location = to_loc
    # for simplicity we keep a single qty per item; ignore partial splits in this skeleton
    return {"sku": sku, "from": from_loc, "to": to_loc, "qty": qty}

def inventory_by_location(location: str) -> List[Dict]:
    return items_service.by_location(location)
