from fastapi.testclient import TestClient
from app.main import app
from app import crud, schemas
from app.db.session import SessionLocal
from app.core.config import settings

# Membuat klien tes FastAPI
client = TestClient(app)

def test_create_user():
    """
    Pengujian untuk membuat user baru.
    """
    user_in = schemas.UserCreate(email="test@example.com", password="password")
    response = client.post("/api/v1/users/", json=user_in.dict())
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == user_in.email
    assert "id" in data
    assert "is_active" in data

def test_read_user():
    """
    Pengujian untuk mendapatkan user berdasarkan email.
    """
    user_in = schemas.UserCreate(email="test@example.com", password="password")
    response = client.post("/api/v1/users/", json=user_in.dict())
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]

    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == user_in.email
    assert data["id"] == user_id
