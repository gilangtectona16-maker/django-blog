import requests
from django.conf import settings

HEADERS = {
    "apikey": settings.SUPABASE_API_KEY,
    "Authorization": f"Bearer {settings.SUPABASE_API_KEY}",
    "Content-Type": "application/json",
}

BASE_URL = f"{settings.SUPABASE_URL}/rest/v1/posts"

def fetch_posts():
    r = requests.get(
        BASE_URL,
        headers=HEADERS,
        params={"select": "*", "order": "created_at.desc"}
    )
    r.raise_for_status()
    return r.json()

def fetch_post(uid):
    r = requests.get(
        BASE_URL,
        headers=HEADERS,
        params={"unique_id": f"eq.{uid}", "select": "*"}
    )
    r.raise_for_status()
    data = r.json()
    return data[0] if data else None
