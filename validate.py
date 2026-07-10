import pandas as pd

from schema_config import SCHEMA_WHITELIST


# Ensure the whitelisted columns/properties are present in the databases
def validate(databases: dict[str, pd.DataFrame]) -> None:
    for db, df in databases.items():
        actual_props = {
            prop.lower().replace(" ", "_") for prop in set(df.columns)
        }
        needed_props = SCHEMA_WHITELIST[db]
        missing = needed_props - actual_props
        if missing:
            raise ValueError(f"missing properties: {db, missing}")
