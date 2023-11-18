from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("single-blog/<str:pk>/", views.singleBlog, name="single-blog"),
    path("single-blog/<str:pk>/toggle-like/", views.toggle_like, name="toggle-like"),
]
