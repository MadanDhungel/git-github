import pytest

from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_main_route(client):
    resp = client.get('/main.html')
    assert resp.status_code == 200
