import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("EVERLOOP_API_KEY")
if not API_KEY:
    raise RuntimeError("Add EVERLOOP_API_KEY to .env")

APP_ID = "f66b08b2-d3fd-487b-856d-289678bc9578"
COLLECTIONS_URL = f"https://api.adalo.com/v0/apps/{APP_ID}/collections/"

COLLECTION_IDS = {
    "users": "t_a229afcff3994430ae617cc80e03bc63",
    "containers_out":"t_ad7134d6a8084bb79841d7380d84c7e6"
}