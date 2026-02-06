from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path("read/<str:unique_id>/<str:slug>/", post_detail, name="post_detail"),
    
    path("group/<str:group_name>/", group_page, name="group_page"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)