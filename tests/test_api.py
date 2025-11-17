import io
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json() == {"ok": True}

def test_onboard_trunk():
    payload = {
        "name": "test-trunk",
        "sip_url": "sip:test",
        "username": "u",
        "password": "p",
    }
    r = client.post("/api/sip/onboard", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"

def test_upload_csv():
    csv_content = b"name,phone\nAlice,+62812345\n"
    files = {"file": ("test.csv", io.BytesIO(csv_content), "text/csv")}
    r = client.post("/api/csv/upload", files=files)
    assert r.status_code == 200
    data = r.json()
    assert data["filename"] == "test.csv"
    assert data["size"] == len(csv_content)

def test_start_call():
    payload = {"task_id": "t1", "script": "Halo", "concurrency": 1}
    r = client.post("/api/call/start", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "enqueued"
