from pathlib import Path

from etl import extract, validate, transform, load


def main():
    app_dir = Path(__file__).resolve().parent
    databases = extract(app_dir)
    validate(databases)
    databases = transform(databases)
    load(databases)


if __name__ == "__main__":
    main()
