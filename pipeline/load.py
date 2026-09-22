from datetime import date
import json

from google.cloud import bigquery


def load_records(
    name: str, records: list[dict], extracted_at: date, resync: bool
) -> None:

    client = bigquery.Client(project="everloop-analytics")
    table_id = f"everloop-analytics.raw.{name}"

    # Delete all the records in the current databases partition.
    # Trivializes retries. Always happens once per database.
    if resync:
        query = f"""
            DELETE FROM `{table_id}`
            WHERE extracted_at = @extracted_at
        """
        
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter(
                    "extracted_at",
                    "DATE",
                    extracted_at,
                )
            ]
        )
        client.query(query, job_config=job_config).result()

        print(f"Deleted {name} records for {extracted_at}")

    # Start appending adalo json to bigquery json
    rows = [
        {
            "raw_payload": json.dumps(record),
            "extracted_at": extracted_at.isoformat(),
        }
        for record in records
    ]

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        raise RuntimeError(
            f"Failed APPENDING FOR {name} records: {errors}"
        )

    print(f"Appended {len(records)} {name} records into BigQuery...")
