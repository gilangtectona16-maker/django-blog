# blog/context_processors.py
from .supabase import *

# service = SupabasePostByGroupService()

def common_data(request):
    group_tag = set()
    all_posts = fetch_posts()  # ambil sekali di sini
    for post in all_posts:
        group_tag.update(post.get("groups", []))

    return {
        'group_tags': list(group_tag),
        'latest_posts': fetch_latest_posts(5),
        'berita_panas': fetch_posts_by_types("berita panas", 5),
        'tips_posts': fetch_posts_by_types("tips", 5),
        'utama_posts': fetch_posts_by_types("utama", 5),
    }