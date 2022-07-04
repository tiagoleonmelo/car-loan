import pytest
from src.commons import TEST_SAMPLE
from src.app import app as flask_app

# Instancing the Flask application
@pytest.fixture()
def app():
    return flask_app


# Using the previous fixture to generate a client we can test
@pytest.fixture()
def client(app):
    # Create a test client using the Flask application configured for testing
    return app.test_client()


# Testing fixtures using a dummy endpoint
def test_dummy_endpoint(client):
    response = client.get("/")
    assert (
        b"I'm a great endpoint and I love helping Tiago test his software"
        == response.data
    )


# Testing prediction endpoint
def test_prediction_endpoint(client):
    # Requesting a prediction with the wrong schema should result in an error
    response = client.post(
        "/api/predict", content_type="application/json", json={"a": "value", "b": 1}
    )
    obj = response.json
    assert obj["error"] == "Invalid schema"

    # Requesting a prediction with known values
    response = client.post(
        "/api/predict", content_type="application/json", json=TEST_SAMPLE
    )
    obj = response.json
    assert obj["label"] == [0]


# Testing authenticated prediction endpoint
def test_auth_prediction_endpoint(client):
    # Requesting a prediction with no credentials should return a 401 Unauth
    response = client.post(
        "/api/secure_predict",
        content_type="application/json",
        json={"a": "value", "b": 1},
    )

    assert response.status == "401 UNAUTHORIZED"

    # Requesting a prediction with known values and wrongly authenticated
    response = client.post(
        "/api/secure_predict",
        content_type="application/json",
        json=TEST_SAMPLE,
        auth=("tleonmelo", "drogon"),
    )
    assert response.status == "401 UNAUTHORIZED"

    # Finally, requesting a prediction with known values and properly authenticated
    response = client.post(
        "/api/secure_predict",
        content_type="application/json",
        json=TEST_SAMPLE,
        auth=("tleonmelo", "dragon"),
    )

    assert response.status == "200 OK"

    obj = response.json
    assert obj["label"] == [0]
