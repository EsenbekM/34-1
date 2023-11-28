from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('posts/', views.posts_view),
    path('posts/create/', views.post_create),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('hashtags/', views.hashtags_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
