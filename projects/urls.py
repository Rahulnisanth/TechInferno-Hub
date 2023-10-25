from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('single-project/<str:pk>/', views.singleProject, name='single-project'),

    path('create-project/', views.createProject, name='create-project'),
]