import pandas as pd

from schema_config import EXPECTED_PROPERTIES


def validate_schemas(databases: dict[str, pd.DataFrame]) -> None:
    for db, df in databases.items():
        expected_props = EXPECTED_PROPERTIES[db]
        actual_props = {
            prop.lower().replace("- ", "").replace(" ", "_")
            for prop in set(df.columns)
        }
        missing = expected_props - actual_props
        extra = actual_props - expected_props
        if missing or extra:
            raise ValueError(f"missing: {missing}, extra: {extra}")
