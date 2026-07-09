import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

client = create_client(url, key)
