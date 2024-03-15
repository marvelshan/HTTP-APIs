from json import dumps
import pytest
from app import app


@pytest.fixture
def client():
    """Creates a Flask test client with TESTING mode enabled."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_signIp_request_valid_data(client):
    """Tests the /signIn endpoint with valid user data."""
    response = client.post(
        "/api/signIn",
        data=dumps(
            {
                "username": "Flask1",
                "password": "testPassword1234",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["success"] is True


def test_signIn_request_valueError_invalid_password(client):
    """Tests the /signUp endpoint with invalid password."""
    response = client.post(
        "/api/signIn",
        data=dumps(
            {
                "username": "Flask1",
                "password": "testpassword",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 401
    assert response.json["success"] is False
    assert (
        response.json["reason"]
        == "Invalid password"
    )


def test_signIn_request_valueError_user_not_found(client):
    """Tests the /signIn endpoint with user not found."""
    response = client.post(
        "/api/signIn",
        data=dumps(
            {
                "username": "Django",
                "password": "testpassword",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 404
    assert response.json["success"] is False
    assert (
        response.json["reason"]
        == "User not found"
    )
