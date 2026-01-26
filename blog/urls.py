from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('manage/', PostListView.as_view(), name='post_list'),
    # path('manage/create/', PostCreateView.as_view(), name='post_create'),
    # path('manage/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    # path('manage/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('', post_list, name='post_list'),
    
    path("read/<str:unique_id>/", post_detail, name="post_detail"),

    # path('read/<int:year>/<int:month>/<int:day>/<str:unique_id>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # path('<str:unique_id>/', PostDetailView.as_view(), name='post_detail'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)