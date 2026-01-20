from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Detail satu post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_object(self, queryset=None):
        # return get_object_or_404(Post, unique_id=self.kwargs['unique_id'], slug=self.kwargs['slug'])
        return get_object_or_404(Post, unique_id=self.kwargs['unique_id'])

# List semua post (homepage blog)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # kita buat nanti
    context_object_name = 'posts'
    ordering = ['-created_date']  # terbaru duluan

# Tambah post baru
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'thumbnail', 'featured_image', 'featured_image2']  # field yang bisa diisi
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # balik ke list setelah save

# Edit post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'thumbnail', 'featured_image' , 'featured_image2']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

# Hapus post
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

    def get(self, request, *args, **kwargs):
        # Kalau akses via GET (klik link), redirect ke list aja atau 404
        # Biar nggak butuh template
        return HttpResponseRedirect(self.success_url)

    def delete(self, request, *args, **kwargs):
        # Hapus langsung kalau POST
        return super().delete(request, *args, **kwargs)