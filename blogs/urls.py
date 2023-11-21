from django.urls import path
from .views import *

urlpatterns = [
    path("", blogs, name="blogs"),
    path("single-blog/<str:pk>/", singleBlog, name="single-blog"),
    path("create-blog/", createBlog, name="create-blog"),
    path("edit-blog/<str:pk>/", editBlog, name="edit-blog"),
    path("delete-blog/<str:pk>/", deleteBlog, name="delete-blog"),
    path("like/<str:pk>/", likeBlog, name="like-blog"),
]
