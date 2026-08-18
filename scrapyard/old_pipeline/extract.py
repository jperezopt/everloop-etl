import pandas as pd
from pathlib import Path

from .schema_config import EXPECTED_DIR
from .schema_config import SCHEMA_WHITELIST


def extract(
    app_dir: Path,
    expected_dir: str = EXPECTED_DIR,
    schema_whitelist: dict[str, set[str]] = SCHEMA_WHITELIST,
) -> dict[str, pd.DataFrame]:
    actual_dir = app_dir / expected_dir
    actual_files = verify_csv_files(actual_dir, schema_whitelist)
    return extract_csv_files(actual_files)


def verify_csv_files(
    actual_dir: Path, schema_whitelist: dict[str, set[str]]
) -> dict[str, Path]:
    if not actual_dir.is_dir():
        raise FileNotFoundError(f"could not find '{actual_dir}'")

    actual_files = {}
    invalid_items = []
    for item in actual_dir.iterdir():
        if item.is_file() and item.suffix.lower() == ".csv":
            actual_files[item.stem.lower()] = item
        else:
            invalid_items.append(item.name)

    expected_filenames = set(schema_whitelist.keys())
    actual_filenames = set(actual_files.keys())
    missing = expected_filenames - actual_filenames
    extra = actual_filenames - expected_filenames

    if missing or extra or invalid_items:
        raise ValueError(
            f"missing files: {sorted(missing)}, "
            f"extra files: {sorted(extra)}, "
            f"invalid items: {sorted(invalid_items)}"
        )

    return actual_files


def extract_csv_files(
    actual_files: dict[str, Path],
) -> dict[str, pd.DataFrame]:
    return {stem: pd.read_csv(path) for stem, path in actual_files.items()}
