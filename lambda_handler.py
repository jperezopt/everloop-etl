from pipeline import extract, load

import json

def main():
    for name, records in extract.extract_all():
        print(f"Received {len(records)} records from {name}")
        load(records)

if __name__ == "__main__":
    main()
