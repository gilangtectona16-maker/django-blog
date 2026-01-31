from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    
    path("read/<str:unique_id>/", post_detail, name="post_detail"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)