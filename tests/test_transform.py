from etl.transform import normalize_df, filter_whitelist_cols
import pandas as pd

def test_transform():
    users_db = {"users": pd.read_csv("csv_database_collections/Users.csv")}
    users_db = normalize_df(users_db)
    filter_whitelist_cols(users_db)
    print()
    for col in users_db["users"]:
        print(col)