"""Simple script to perform ETL using Loader class"""

import logging
import time

from commons import DATA_SOURCE, DB_NAME, SCHEMA_NAME, TABLE_NAME
from Loader import Loader

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Instancing loader")
    start = time.time()
    loader = Loader(data_source_path=DATA_SOURCE, database_name=DB_NAME)

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))

    logging.info("Populating DB")
    start = time.time()
    loader.populate_db(table_name=TABLE_NAME, schema_name=SCHEMA_NAME)

    end = time.time()
    elapsed = end - start
    logging.info("Elapsed time: {0:.2f}".format(elapsed))


if __name__ == "__main__":
    main()
