import pytest
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
