import os
import pandas as pd

from dotenv import load_dotenv
from supabase import create_client
from supabase import Client
from .schema_config import SCHEMA_WHITELIST, TABLE_TYPES


def load(databases: dict[str, pd.DataFrame]):
    load_dotenv()
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    client = create_client(url, key)
    db_records = df_to_records(databases)
    responses = send_to_supabase(client, db_records)
    print(responses)


def df_to_records(databases: dict[str, pd.DataFrame]) -> list[dict]:
    return {db: df.to_dict("records") for db, df in databases.items()}


def send_to_supabase(
    client: Client, db_records: dict[str, list[dict]]
) -> list:
    if set(SCHEMA_WHITELIST) != set(TABLE_TYPES):
        raise ValueError(
            f"mismatch between SCHEMA_WHITELIST and TABLE_TYPES: "
            f"{set(SCHEMA_WHITELIST) ^ set(TABLE_TYPES)}"
        )
    responses = []
    for db, mode in TABLE_TYPES.items():
        if not db_records[db]:
            continue
        if mode == "state":
            response = client.table(db).upsert(db_records[db]).execute()
        elif mode == "history":
            response = client.table(db).insert(db_records[db]).execute()
        else:
            raise ValueError(f"unknown mode {mode} for table {db}")
        responses.append(response)
    return responses
