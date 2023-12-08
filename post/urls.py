from django.urls import path
from post import views


urlpatterns = [
    path('', views.main_view),
    path('posts/', views.PostListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<int:post_id>/', views.PostDetailView.as_view()),
    path('posts/<int:post_id>/update/', views.PostUpdateView.as_view()),
    path('hashtags/', views.hashtags_view),
]

