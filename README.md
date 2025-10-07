# RFID + QR Warehouse Management System (Skeleton)

Teaching-oriented WMS prototype supporting **RFID** and **QR** identification.

## Features
- Minimal FastAPI service
- Endpoints for scanning QR/RFID, items CRUD (basic), inventory moves (simplified)
- In-memory repositories (easy to run)
- Pytest tests
- GitHub Actions CI workflow
- Dockerfile for containerized run

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
# Open http://localhost:8000/docs
```

## Run tests
```bash
pytest -q
```

## Docker
```bash
docker build -t rfid-qr-wms:local .
docker run -p 8000:8000 rfid-qr-wms:local
```

## Notes
This is a skeleton intended for coursework. Replace in-memory repos with a DB layer (SQLite/Postgres via SQLAlchemy) for a production-like setup.
