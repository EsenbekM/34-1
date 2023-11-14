from django.contrib import admin
from django.urls import path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view),
    path('test/', views.test_view),
]
