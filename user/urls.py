from django.urls import path
from . import views

urlpatterns = [
    # Profile rendering column ->
    path("", views.profiles, name="profiles"),
    path("single-profile/<str:pk>/", views.singleProfile, name="single-profile"),
    # Authentication column ->
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register_user/", views.registerUser, name="register_user"),
    # Profile column ->
    path("user-profile/", views.userProfile, name="user-profile"),
    path("edit-profile/", views.editProfile, name="edit-profile"),
    # Skill column ->
    path("add-skill/", views.addSkill, name="add-skill"),
    path("edit-skill/<str:pk>/", views.editSkill, name="edit-skill"),
    path("delete-skill/<str:pk>/", views.deleteSkill, name="delete-skill"),
    # Reviews column ->
    path("inbox/", views.inbox, name="inbox"),
    path("message-inbox/<str:pk>/", views.messageInbox, name="message-inbox"),
    path("message-form/<str:pk>/", views.messageForm, name="message-form"),
]
