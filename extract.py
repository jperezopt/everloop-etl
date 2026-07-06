from pathlib import Path

EXPECTED_DIRECTORY = "adalo_csv_database_collections"

EXPECTED_FILENAMES = {
    "Containers Out.csv",
    "Cup Stock Updates.csv",
    "Lost and Broken Cups.csv",
    "Region.csv",
    "Reports.csv",
    "Site Inventory Tracking.csv",
    "Sites.csv",
    "User History.csv",
    "User Payment Flow.csv"
    "User Payment History.csv",
    "Users.csv"}

def verify_csv_files(EXPECTED_DIRECTORY, EXPECTED_FILENAMES):
    cwd = Path(__file__).parent
    actual_directory = cwd / EXPECTED_DIRECTORY
    if not actual_directory.is_dir():
        raise FileNotFoundError(
            f"could not find '{EXPECTED_DIRECTORY}' in '{cwd}'")
    actual_filenames = {item.name for item in actual_directory.iterdir()}
    missing = EXPECTED_FILENAMES - actual_filenames
    extra = actual_filenames - EXPECTED_FILENAMES
    if missing or extra:
        raise ValueError(f"missing {sorted(missing)}, extra: {sorted(extra)}")