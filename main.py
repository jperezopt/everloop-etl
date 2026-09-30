from datetime import datetime, timezone

from pipeline import extract, load


def main():
    extracted_at = datetime.now(timezone.utc).date()
    print(extracted_at)
    for name, records in extract.extract_all(50):
        load.load_records(name, records, extracted_at)


if __name__ == "__main__":
    main()
