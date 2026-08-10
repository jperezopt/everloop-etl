import requests
from config import COLLECTIONS_URL, COLLECTION_IDS, API_KEY


def extract_all():
    with requests.Session() as session:
        session.headers.update({"Authorization": f"Bearer {API_KEY}"})
        for name, cid in COLLECTION_IDS.items():
            url = COLLECTIONS_URL + cid
            try:
                for page in paginate(session, url):
                    yield name, page
            except requests.RequestException as e:
                raise RuntimeError(
                    f"Extraction failed for collection '{name}' at {url}"
                ) from e


def paginate(session: requests.Session, url: str, limit=1000):
    # TODO: Manage 5 req/s limit. Either add no pacing and use the responses
    # retry timers, or add pacing and a safety retry fallback.
    offset = 0
    while True:
        resp = session.get(
            url=url,
            params={"offset": offset, "limit": limit},
            timeout=30,
        )
        resp.raise_for_status()
        records = resp.json()["records"]
        yield records
        if len(records) < limit:
            return
        offset += limit
