from joblib import load

from src.commons import FEATURES


class Predictor:
    """Class that serves as an interface to the model"""

    def __init__(self, model_path, features=FEATURES) -> None:
        self.model = load(model_path)
        self.features = features

    def predict(self, loan_application):
        # Do any preprocessing steps here
        return self.model.predict(loan_application)

    def is_valid_sample(self, sample):
        """Return whether a given sample matches our model's schema"""
        return sorted(list(sample.keys())) == sorted(self.features)
