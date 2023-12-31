from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("single-project/<str:pk>/", views.singleProject, name="single-project"),
    path("add-like/<str:pk>/", views.addLike, name="add-like"),
    path("create-project/", views.createProject, name="create-project"),
    path("update-project/<str:pk>/", views.updateProject, name="update-project"),
    path("delete-project/<str:pk>/", views.deleteProject, name="delete-project"),
    path(
        "download-documentation/<str:pk>/",
        views.download_documentation,
        name="download-documentation",
    ),
    path("add-favorite/<str:pk>/", views.addFavorite, name="add-favorite"),
    path("favorite-list/", views.favoriteList, name="favorite-list"),
]
