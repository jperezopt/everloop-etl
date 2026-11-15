from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from pipeline import extract, load


def main():
    extracted_at = (
        datetime.now(ZoneInfo("America/Chicago")).date()
        - timedelta(days=1)
    )

    for table_name, records in extract.extract_all(page_size=50):
        load.load_records(table_name, records, extracted_at)


if __name__ == "__main__":
    main()