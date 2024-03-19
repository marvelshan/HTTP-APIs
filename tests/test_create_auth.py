from json import dumps
import pytest
from app import app


@pytest.fixture
def client():
    """Creates a Flask test client with TESTING mode enabled."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_signUp_request_valid_data(client):
    """Tests the /signUp endpoint with valid user data."""
    response = client.post(
        "/api/signUp",
        data=dumps(
            {
                "username": "Flask34",
                "password": "testPassword1234",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json["success"] is True


def test_signUp_request_username_exists(client):
    """Tests the /signUp endpoint with valid user data."""
    response = client.post(
        "/api/signUp",
        data=dumps(
            {
                "username": "Flask20",
                "password": "testPassword1234",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.json["success"] is False
    assert response.json["reason"] == "Username already exists"


def test_signUp_request_valueError_lack_uppercase(client):
    """Tests the /signUp endpoint with valid user data."""
    response = client.post(
        "/api/signUp",
        data=dumps(
            {
                "username": "Flask1",
                "password": "testpassword1234",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.json["success"] is False
    assert (
        response.json["reason"]
        == "Value error, Password must contain at least one uppercase letter"
    )
