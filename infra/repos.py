from typing import Dict, Optional, List
from domain.entities import Item

class ItemsRepo:
    def __init__(self):
        self._items: Dict[str, Item] = {}

    def create(self, item: Item) -> None:
        self._items[item.sku] = item

    def get(self, sku: str) -> Optional[Item]:
        return self._items.get(sku)

    def by_location(self, location: str) -> List[Item]:
        return [i for i in self._items.values() if i.location == location]

class TagsRepo:
    def __init__(self):
        self._qr: Dict[str, str] = {}   # qr -> sku
        self._rfid: Dict[str, str] = {} # rfid -> sku

    def bind_qr(self, sku: str, qr: str) -> None:
        self._qr[qr] = sku

    def bind_rfid(self, sku: str, rfid: str) -> None:
        self._rfid[rfid] = sku

    def get_by_qr(self, qr: str) -> Optional[str]:
        return self._qr.get(qr)

    def get_by_rfid(self, rfid: str) -> Optional[str]:
        return self._rfid.get(rfid)

# Singletons for simplicity in this skeleton
items_repo = ItemsRepo()
tags_repo = TagsRepo()
