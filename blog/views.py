from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from .supabase import *
    
# service = SupabasePostByGroupService()

def post_list(request):
    posts = fetch_posts()
    
    return render(request, "blog/post_base.html", {"posts": posts})

def post_detail(request, unique_id, slug):
    post = fetch_post(unique_id)

    if not post:
        raise Http404("Post not found")

    # ambil slug asli dari data supabase
    real_slug = post.get("slug")

    # kalau slug di URL tidak sama dengan slug asli → redirect ke URL yang benar
    if slug != real_slug:
        return redirect("post_detail", unique_id=unique_id, slug=real_slug)

    return render(request, "blog/post_detail.html", {"post": post})
    
def group_page(request, group_name):
    all_posts = fetch_posts()

    # 🔥 filter pakai Python
    group_posts = [
        post for post in all_posts
        if group_name in post.get("groups", [])
    ]

    # pagination ala kamu
    page = int(request.GET.get("page", 1))
    limit = 15
    start = (page - 1) * limit
    end = start + limit

    masonry_posts = [
        m for m in group_posts
        if m.get("types") == "berita panas" or m.get("types") == "utama"
    ]

    carousel_posts = [
        p for p in group_posts
        if p.get("types") == "berita panas"
    ][:5]

    context = {
        "group_name": group_name,
        "carousel_posts": carousel_posts,
        "masonry_posts": masonry_posts,
        "page": page,
        "has_more": end < len(group_posts),
    }

    return render(request, "blog/group_page.html", context)