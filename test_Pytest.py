from fastapi.testclient import TestClient
from my_project.app import get_application
from my_project.config import settings


app = get_application()


def test_ready():
    settings.USE_REDIS = False

    with TestClient(app) as client:
        response = client.get("/api/ready")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_ready_invalid():
    with TestClient(app) as client:
        response = client.get("/api/ready/123")
        assert response.status_code == 404