from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    sku: str
    name: str
    qty: int = 0
    location: str = "RECEIVING"
    qr: Optional[str] = None
    rfid: Optional[str] = None
