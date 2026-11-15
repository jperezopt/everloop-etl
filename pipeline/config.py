import os

from dotenv import load_dotenv

# Load the Adalo API key from the environment or local .env file.
load_dotenv()

API_KEY = os.environ.get("EVERLOOP_API_KEY")
if not API_KEY:
    raise RuntimeError("EVERLOOP_API_KEY environment variable is not set")

# Adalo application and collections endpoint
APP_ID = "f66b08b2-d3fd-487b-856d-289678bc9578"
COLLECTIONS_URL = f"https://api.adalo.com/v0/apps/{APP_ID}/collections/"

# Collection names must match their corresponding BigQuery raw table names
# Find collection IDs in Adalo: Database → Collection → API Documentation
# Adding a collection here automatically includes it in extraction
COLLECTION_IDS = {
    "cup_stock_updates": "t_b460390e1747492e91333eb999386bd5",
    "user_history": "t_3fa458a0fdd54cb5b8d8dda20209ee3b",
    "sites": "t_4f1def22438341f291b1d2c5ac568bff",
}