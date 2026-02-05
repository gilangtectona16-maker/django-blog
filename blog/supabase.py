from unicodedata import category
import requests
from django.conf import settings
from django.core.cache import cache

HEADERS = {
    "apikey": settings.SUPABASE_API_KEY,
    "Authorization": f"Bearer {settings.SUPABASE_API_KEY}",
    "Content-Type": "application/json",
}

BASE_URL = f"{settings.SUPABASE_URL}/rest/v1/posts"

# pakai session biar koneksi lebih efisien
session = requests.Session()
session.headers.update(HEADERS)

TIMEOUT = 2  # detik
CACHE_TTL = 60    # cache 60 detik

def fetch_posts():
    cache_key = "all_posts"
    data = cache.get(cache_key)
    
    if not data:
        r = requests.get(
            BASE_URL,
            headers=HEADERS,
            params={"select": "*", "order": "created_at.desc"},
            timeout=TIMEOUT
        )
        r.raise_for_status()
        data = r.json()
        cache.set(cache_key, data, CACHE_TTL)
    return data

def fetch_post(uid):
    r = requests.get(
        BASE_URL,
        headers=HEADERS,
        params={"unique_id": f"eq.{uid}", "select": "*"}
    )
    r.raise_for_status()
    data = r.json()
    return data[0] if data else None

def fetch_posts_by_types(types, limit=5):
    cache_key = f"posts_type_{types}_{limit}"
    data = cache.get(cache_key)

    if not data:
        url = f"{BASE_URL}?types=eq.{types}&order=created_at.desc&limit={limit}"
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        cache.set(cache_key, data, CACHE_TTL)

    return data


def fetch_latest_posts(limit=5):
    cache_key = f"latest_posts_{limit}"
    data = cache.get(cache_key)

    if not data:
        url = f"{BASE_URL}?order=created_at.desc&limit={limit}"
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        cache.set(cache_key, data, CACHE_TTL)

    return data

# class SupabasePostByGroupService:
#     def __init__(self):
#         self.base_url = BASE_URL
#         self.headers = HEADERS

#     def _get(self, params):
#         r = requests.get(
#             self.base_url,
#             headers=self.headers,
#             params=params,
#             timeout=10
#         )
#         r.raise_for_status()
#         return r.json()

#     # 🔥 INI YANG KAMU MAU: group jsonb
#     def fetch_posts_by_group(self, group_name, limit=15, offset=0):
#         params = {
#             "select": "*",
#             "groups": f'cs.{{"{group_name}"}}',
#             "limit": limit,
#             "offset": offset,
#             "order": "created_at.desc"
#         }
#         return self._get(params)

#     # 🔥 khusus carousel berita panas per group (opsional)
#     def fetch_hot_posts_by_group(self, group_name, limit=5):
#         params = {
#             "select": "*",
#             "groups": f'cs.{{"{group_name}"}}',
#             "types": 'eq."berita panas"',
#             "limit": limit,
#             "order": "created_at.desc"
#         }
#         return self._get(params)