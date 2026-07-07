from pathlib import Path
import pandas as pd

EXPECTED_DIR = "adalo_csv_database_collections"
EXPECTED_FILES = {
    "Containers_Out.csv",
    "Cup_Stock_Updates.csv",
    "Lost_and_Broken_Cups.csv",
    "Region.csv",
    "Reports.csv",
    "Site_Inventory_Tracking.csv",
    "Sites.csv",
    "User_History.csv",
    "User_Payment_Flow.csv",
    "User_Payment_History.csv",
    "Users.csv",
}


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
