from django.urls import path
from . import views

urlpatterns = [
      path('', views.profiles, name='profiles'),
      path('single-profile/<str:pk>/', views.singleProfile, name='single-profile'),
      path('login_user/', views.login_user, name='login_user'),
      path('logout_user/', views.logout_user, name='logout_user'),

]