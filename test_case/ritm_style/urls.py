from django.urls import path
from . import views

app_name = "ritm_style"

urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news, name="news"),
    path("blog/", views.blog, name="blog"),
    path("new_format", views.new_format, name="new_format"),
]
