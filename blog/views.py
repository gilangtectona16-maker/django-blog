from wsgiref import types
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .supabase import *

group_tag = set()

for post in fetch_posts():
    group_tag.update(post.get("group", []))
    
group_tags = list(group_tag)

latest_posts = fetch_latest_posts(5)
berita_panas = fetch_posts_by_types("berita panas", 5)
tips_posts = fetch_posts_by_types("tips", 5)
utama_posts = fetch_posts_by_types("utama", 5)

context = {
    "latest_posts": latest_posts,
    "berita_panas": berita_panas,
    "tips_posts": tips_posts,
    "utama_posts": utama_posts,
    "group_tags": group_tags,
}
    
def post_list(request):
    posts = fetch_posts()
    
    context.update({
        "posts": posts,
    })
    
    return render(request, "blog/post_base.html", context)

def post_detail(request, unique_id):
    post = fetch_post(unique_id)
    if not post:
        return render(request, "404.html", status=404)
    
    context.update({
        "post": post,
    })
    return render(request, "blog/post_detail.html", context)

