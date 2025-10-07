from fastapi.testclient import TestClient
from main import app
from services.usecases import items_service

client = TestClient(app)

def setup_module(_):
    # seed one known item with QR/RFID
    items_service.create(sku="ABC-1", name="Demo Item", qty=10, location="RECEIVING",
                         qr="QR-123", rfid="TID-999")

def test_qr_not_found():
    resp = client.post("/scan/qr", json={"qr": "UNKNOWN"})
    assert resp.status_code == 404

def test_qr_found():
    resp = client.post("/scan/qr", json={"qr": "QR-123"})
    assert resp.status_code == 200
    assert resp.json()["sku"] == "ABC-1"

def test_rfid_batch():
    resp = client.post("/scan/rfid", json={"rfids": ["TID-999", "TID-000"]})
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["matches"]) == 1
    assert data["matches"][0]["sku"] == "ABC-1"
