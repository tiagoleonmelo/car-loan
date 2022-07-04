import json

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from src.commons import MODEL_PATH

from src.Predictor import Predictor

app = Flask(__name__)
auth = HTTPBasicAuth()
predictor = Predictor(MODEL_PATH)

USERS = {"tleonmelo": generate_password_hash("dragon")}


@auth.verify_password
def verify_password(username: str, password: str):
    """Utility function to verify whether username matches saved password to authenticate
    users.

    Parameters
        username: str
            Name of the user trying to authenticate themselves
        password: str
            Password of the user in plaintext

    Returns
        boolean : whether the username/password combination is valid
    """
    if username in USERS:
        return check_password_hash(USERS.get(username), password)
    return False


@app.route("/")
def dummy():
    """Dummy endpoint to make sure the Flask app is working"""
    return "I'm a great endpoint and I love helping Tiago test his software"


@app.route("/api/predict", methods=["POST"])
def make_predictions():
    """Insecure authentication endpoint. Does not support authentication, just returns
    a prediction given an incoming set of features. Verifies schema.

    POST
        data: dictionary containing {feature_name: value} for each of the features used
        when training the model

        response:
            error: Error raised in this request
            label: list of labels for each of the submitted examples
    """

    error = "Invalid HTTP request"

    if request.method == "POST":
        sample = json.loads(request.data)

        # Ensure the schema provided matches ours
        if predictor.is_valid_sample(sample):
            label = predictor.predict(sample)
            return jsonify({"label": label.tolist()})
        else:
            error = "Invalid schema"

    return jsonify({"error": error})


@app.route("/api/secure_predict", methods=["POST"])
@auth.login_required
def make_auth_predictions():
    """Same as above, but supporting basic authentication"""

    error = "Invalid HTTP request"

    if request.method == "POST":
        sample = json.loads(request.data)

        # Ensure the schema provided matches ours
        if predictor.is_valid_sample(sample):
            label = predictor.predict(sample)
            return jsonify({"label": label.tolist()})
        else:
            error = "Invalid schema"

    return jsonify({"error": error})
