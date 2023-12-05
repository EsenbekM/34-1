from django.urls import path
from post import views


urlpatterns = [
    path('', views.main_view),
    path('posts/', views.posts_view),
    path('posts/create/', views.post_create),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('posts/<int:post_id>/update/', views.post_update_view),
    path('hashtags/', views.hashtags_view),
]

