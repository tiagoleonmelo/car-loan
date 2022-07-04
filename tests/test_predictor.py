import pytest
from src.commons import FEATURES, MODEL_PATH
from src.Predictor import Predictor

# Instancing Predictor
@pytest.fixture()
def setup():
    return Predictor(MODEL_PATH, FEATURES)


# Testing fixtures using a dummy endpoint
def test_predictor(setup):
    assert True
