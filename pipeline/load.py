import json
from datetime import date

from google.cloud import bigquery

PROJECT = "everloop-analytics"
_client = bigquery.Client(project=PROJECT)


def load_records(name: str, records: list[dict], extracted_at: date) -> None:
    """Load records atomically into raw.{table_name}

    Grabs the table from BigQuery to determine if it's:
    - Partitioned by extracted_at: replace todays partition, idempotent
    - Unpartitioned: whole table is replaced
    """
    table_id = f"{PROJECT}.raw.{name}"
    table = _client.get_table(table_id)

    if table.time_partitioning:
        destination = f"{table_id}${extracted_at:%Y%m%d}"
    else:
        destination = table_id

    rows = [
        {"raw_payload": json.dumps(r), "extracted_at": extracted_at.isoformat()}
        for r in records
    ]

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema=table.schema,
    )

    _client.load_table_from_json(rows, destination, job_config=job_config).result()

    print(f"Loaded {len(records)} {name} records into {destination}")
