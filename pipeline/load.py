# Called by lambda_handler.py within the extraction generator.
# Will be sending <= 1000 records into bigquery.
# Records are a list of dictionaries, JSON to BQ?

def load(records: list[dict]) -> None:
    print(f"Loading {len(records)} into BigQuery...")