from etl.transform import normalize_df, filter_whitelist_cols
import pandas as pd


def test_transform():
    users_db = {"users": pd.read_csv("csv_database_collections/Users.csv")}
    print(users_db["users"].dtypes)
    users_db = normalize_df(users_db)
    filter_whitelist_cols(users_db)
    print(users_db["users"].dtypes)
    users_db_records = users_db["users"].to_dict("records")
    for record in users_db_records:
        for col, data in record.items():
            print(col + ":", data)
