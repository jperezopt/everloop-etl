from etl.transform import normalize_df, filter_whitelist_cols
from pathlib import Path
import pandas as pd
import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"

@pytest.fixture
def users_df():
    return pd.read_csv(FIXTURES_DIR / "Users.csv")

def test_transform(users_df):
    print(users_df["users"].dtypes)
    users_df = normalize_df(users_df)
    filter_whitelist_cols(users_df)
    print(users_df["users"].dtypes)
    users_df_records = users_df["users"].to_dict("records")
    for record in users_df_records:
        for col, data in record.items():
            print(col + ":", data)
