import pandas as pd
from joblib import load
from sqlalchemy import create_engine

from src.commons import API_TABLE_NAME, DB_NAME, FEATURES, SCHEMA_NAME, TARGET


class Predictor:
    """Class that serves as an interface to the model. Stores predictions made in its own
    table


    Attributes:
        model : sklearn model
            Sci-kit learn trained model
        features : list[str]
            Schema used to train the model
        engine : sqlalchemy.Engine
            Engine to interact with DB to save predictions

    Methods:
        populate_db(schema_name="loan", table_name="car_loan")
            Populates a database with own data source. Fails if table already exists in
            the specified schema
    """

    def __init__(
        self, model_path: str, features: list = FEATURES, database_name: str = DB_NAME
    ) -> None:
        self.model = load(model_path)
        self.features = features
        self.engine = create_engine(
            "postgresql://postgres:postgres@localhost:5432/{}".format(database_name)
        )

    def predict(self, loan_application: dict):
        # Convert dict to array
        df = pd.DataFrame(loan_application, index=[0])

        # Do any preprocessing steps here #

        # Make prediction
        prediction = self.model.predict(df[self.features])

        # Store prediction to db
        df[TARGET] = prediction
        df[self.features + [TARGET]].to_sql(
            API_TABLE_NAME,
            self.engine,
            schema=SCHEMA_NAME,
            index=False,
            if_exists="append",
        )

        # Return predicted label
        return prediction

    def is_valid_sample(self, sample):
        """Return whether a given sample matches our model's schema"""
        return sorted(list(sample.keys())) == sorted(self.features)
