from fastapi import FastAPI
from api.routes_items import router as items_router
from api.routes_scan import router as scan_router
from api.routes_inventory import router as inv_router

app = FastAPI(title="RFID+QR WMS", version="0.1.0")

app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(scan_router, prefix="/scan", tags=["scan"])
app.include_router(inv_router, prefix="/inventory", tags=["inventory"])
