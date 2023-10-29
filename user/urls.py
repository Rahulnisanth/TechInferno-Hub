from django.urls import path
from . import views

urlpatterns = [
      path('', views.profiles, name='profiles'),
      path('single-profile/<str:pk>/', views.singleProfile, name='single-profile'),
      path('login_user/', views.login_user, name='login_user'),
      path('logout_user/', views.logout_user, name='logout_user'),
      path('register_user/', views.registerUser, name='register_user'),
      path('user-profile/', views.userProfile, name='user-profile'),
      path('edit-profile/', views.editProfile, name='edit-profile'),
      path('add-skill/', views.addSkill, name='add-skill'),
      path('edit-skill/<str:pk>/', views.editSkill, name='edit-skill'),
      path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),

]