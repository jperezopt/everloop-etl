from datetime import date

from google.cloud import bigquery

PROJECT = "everloop-analytics"
_client = bigquery.Client(project=PROJECT)


def load_records(table_name: str, records: list[dict], extracted_at: date) -> None:
    """Load records atomically into raw.{table_name}

    replace extraction date's partition for partitioned tables,
    or replace entire table for unpartitioned tables
    """
    table_id = f"{PROJECT}.raw.{table_name}"
    table = _client.get_table(table_id)

    if table.time_partitioning:
        destination = f"{table_id}${extracted_at:%Y%m%d}"
    else:
        destination = table_id

    rows = [
        {"raw_payload": r, "extracted_at": extracted_at.isoformat()}
        for r in records
    ]

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema=table.schema,
    )

    _client.load_table_from_json(rows, destination, job_config=job_config).result()

    print(f"Loaded {len(records)} {table_name} records into {destination}")
