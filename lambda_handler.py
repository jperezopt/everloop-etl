from pipeline import extract, extract_api, validate, transform, load

import json


def main():
    for name, page in extract_api.extract_all():
        print(name, json.dumps([user["Username"] for user in page], indent=1))


if __name__ == "__main__":
    main()
