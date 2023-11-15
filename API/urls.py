from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("profiles/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profiles/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.getRoutes),
    path("projects/", views.getProjects),
    path("project/<str:pk>/", views.getProject),
    path("profiles/", views.getProfiles),
    path("profile/<str:pk>/", views.getProfile),
    path("remove-tag/", views.removeTag),
]
