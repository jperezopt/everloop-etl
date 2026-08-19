from datetime import date


def load_records(
    name: str, records: list[dict], extracted_at: date, truncate: bool
) -> None:
    # Truncate
    if truncate:
        print(f"Truncated some {name} records from BigQuery")
    else:
        print(f"Truncated 0 {name} records from BigQuery")
    # Append
    print(f"Appended {len(records)} {name} records into BigQuery...")
