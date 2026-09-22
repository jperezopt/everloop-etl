import json
from datetime import datetime, timezone

from pipeline import extract, load


def main():
    extracted_at = datetime.now(timezone.utc).date()
    print(extracted_at)
    seen = set()
    resync = True
    for name, records in extract.extract_all(50):
        resync = name not in seen
        load.load_records(name, records, extracted_at, resync)
        seen.add(name)
        print(seen)


if __name__ == "__main__":
    main()
