from flask import Flask, request, jsonify
from src.commons import MODEL_PATH

from src.Predictor import Predictor

app = Flask(__name__)
predictor = Predictor(MODEL_PATH)


@app.route("/")
def dummy():
    """Dummy endpoint to make sure the Flask app is working"""
    return "I'm a great endpoint and I love helping Tiago test his software"


@app.route("/api/predict", methods=["POST"])
def make_predictions():
    error = None
    if request.method == "POST":
        sample = request.form["data"]

        # Ensure the schema provided matches ours
        if predictor.is_valid_sample(sample):
            label = predictor.predict(request.form["data"])
            return jsonify({"label": label})
        else:
            error = "Invalid schema"

        # if valid_login(request.form["username"], request.form["password"]):
        #    return log_the_user_in(request.form["username"])
        # else:
        #    error = "Invalid username/password"

    error = "Invalid HTTP request"
    return jsonify({"error": error})
