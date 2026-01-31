from wsgiref import types
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .supabase import *
    
def post_list(request):
    posts = fetch_posts()
    
    return render(request, "blog/post_base.html", {"posts": posts})

def post_detail(request, unique_id):
    post = fetch_post(unique_id)
    if not post:
        return render(request, "404.html", status=404)
    return render(request, "blog/post_detail.html", {"post": post})

