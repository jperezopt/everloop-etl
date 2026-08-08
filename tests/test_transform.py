from pipeline.transform import normalize_df, filter_whitelist_cols
from pathlib import Path
import pandas as pd
import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"

@pytest.fixture
def users_df():
    return pd.read_csv(FIXTURES_DIR / "Users.csv")

def test_transform(users_df):
    users_db = {'users': users_df}
    users_db = normalize_df(users_db)
    filter_whitelist_cols(users_db)
    print(users_db['users'].dtypes)
    user_db_records = users_db["users"].to_dict("records")
    for record in user_db_records:
        for col, data in record.items():
            print(col + ":", data)
