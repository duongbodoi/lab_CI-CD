from app import app

client = app.test_client()

def test_healthz_returns_200():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}