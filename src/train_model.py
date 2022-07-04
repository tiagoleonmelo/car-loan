"""Simple script to train a model using data read from Loader class"""

import logging
import time

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from joblib import dump

from commons import DATA_SOURCE, DB_NAME, FEATURES, MODEL_PATH, SCHEMA_NAME, TARGET
from Loader import Loader

logging.basicConfig(level=logging.INFO)


def main():
    # Instancing the data wrapper
    logging.info("Instancing loader")
    start = time.time()
    loader = Loader(data_source_path=DATA_SOURCE, database_name=DB_NAME)

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))

    # Splitting the data
    logging.info("Splitting data into train, validation and test")
    start = time.time()

    # Fetch data (don't use IDs to train)
    df = loader.data_source.copy().drop(["customer_id"], axis=1)
    labels = df.pop(TARGET)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], labels, test_size=0.3
    )

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))

    # Training the model
    logging.info("Training model")
    start = time.time()

    # Instance model
    clf = LogisticRegression()

    # Train model and save it
    clf.fit(X_train, y_train)

    # Using joblib to write pickle object
    # https://scikit-learn.org/stable/model_persistence.html#python-specific-serialization
    dump(clf, MODEL_PATH)

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))

    # Scoring the model on test
    logging.info("Scoring model on test")
    start = time.time()

    # Score model on test set first to build a report
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
    print("Accuracy: {0:.2f}".format(accuracy_score(y_test, y_pred)))

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))

    # Scoring the model on full set
    logging.info("Scoring model on full set")
    start = time.time()

    # Score model on full set and write to database
    predictions_df = pd.DataFrame([])
    predictions_df["preds"] = clf.predict(df)
    loader.create_table(
        predictions_df, table_name="predictions", schema_name=SCHEMA_NAME
    )

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))


if __name__ == "__main__":
    main()
