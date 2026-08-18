from pipeline import extract, extract_api, validate, transform, load

import json


def main():
    for name, page in extract_api.extract_all():
        print(f"received {len(page)} records from {name}")

if __name__ == "__main__":
    main()
