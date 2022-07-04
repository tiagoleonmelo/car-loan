from sqlalchemy import create_engine
import pandas as pd

import logging

logging.basicConfig(level=logging.INFO)


class Loader:
    """Class responsible for loading a data source. Supports CSV format.


    Attributes:
        data_source : pd.DataFrame
            Data source represented as a pandas dataframe
        engine : sqlalchemy.Engine
            Database engine

    Methods:
        populate_db(schema_name="loan", table_name="car_loan")
            Populates a database with own data source. Fails if table already exists in
            the specified schema
    """

    def __init__(self, data_source_path: str, database_name: str) -> None:
        self.data_source = pd.read_csv(data_source_path)
        self.engine = create_engine(
            "postgresql://postgres:postgres@localhost:5432/{}".format(database_name)
        )

    def populate_db(
        self, table_name: str = "car_loan", schema_name: str = "loans"
    ) -> None:
        """Populates a database with own data source. Fails if table already exists in
        the specified schema

        Parameters
            table_name : bool, optional
                Name of the new table
            schema_name : str, optional
                Name of the schema to use

        Returns
            None
        """
        try:
            self.data_source.to_sql(
                table_name,
                self.engine,
                schema=schema_name,
                index=False,
                if_exists="replace",
            )

        except ValueError:
            logging.error("Error: Table {} already exists".format(table_name))

    def create_table(
        self, df: pd.DataFrame, table_name: str, schema_name: str = "loans"
    ) -> None:
        """Writes a table df to database.

        Parameters
            df : pd.DataFrame
                Table contents to be written to database
            table_name : bool, optional
                Name of the new table
            schema_name : str
                Name of the schema to use

        Returns
            None
        """
        try:
            df.to_sql(table_name, self.engine, schema=schema_name)

        except ValueError:
            logging.error("Error: Table {} already exists".format(table_name))
