import pandas as pd
from pathlib import Path

from schema_config import EXPECTED_DIR
from schema_config import EXPECTED_FILES


def extract(
    expected_dir: str = EXPECTED_DIR, expected_files: set[str] = EXPECTED_FILES
) -> dict[str, pd.DataFrame]:
    actual_dir = Path(__file__).parent / expected_dir
    verify_csv_files(actual_dir, expected_files)
    return extract_csv_files(actual_dir, expected_files)


def verify_csv_files(actual_dir: Path, expected_files: set[str]) -> None:
    if not actual_dir.is_dir():
        raise FileNotFoundError(f"could not find '{actual_dir}'")

    actual_files = {item.name for item in actual_dir.iterdir()}
    missing = expected_files - actual_files
    extra = actual_files - expected_files

    if missing or extra:
        raise ValueError(f"missing {sorted(missing)}, extra: {sorted(extra)}")


def extract_csv_files(
    actual_dir: Path, expected_files: set[str]
) -> dict[str, pd.DataFrame]:
    databases = {}
    for file in expected_files:
        databases[Path(file).stem] = pd.read_csv(actual_dir / file)
    return databases
