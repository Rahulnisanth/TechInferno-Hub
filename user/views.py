from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import SearchProfiles, paginateProfiles
from django.contrib.sessions.models import Session
from django.utils import timezone


def login_user(request):
    flag = "login"
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, f"Welcome {username}, You've logged in successfully!"
            )
            return redirect("/")
        else:
            messages.error(request, "Some Error has occurred, Please try again!")
            return render(request, "login.html")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.info(request, "Your account has logged-out successfully!")
    return redirect("/")


def registerUser(request):
    flag = "register"
    form = CustomUserCreationForm
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(
                request,
                f"Hello {user.username}!,Your account has been registered successfully!",
            )
            login(request, user)
            return redirect("/")
    context = {"flag": flag, "form": form}
    return render(request, "login.html", context)


def profiles(request):
    profiles, search_query = SearchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 9)
    context = {
        "profiles": profiles,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "profiles.html", context)


@login_required(login_url="login_user")
def singleProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, "single-profile.html", context)


@login_required(login_url="login_user")
def userProfile(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "user-profile.html", context)


@login_required(login_url="login_user")
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated successfully")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "profile_form.html", context)


@login_required(login_url="login_user")
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "New Skill has been added successfully")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "skill_form.html", context)


@login_required(login_url="login_user")
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully edited {skill.name}")
            return redirect("user-profile")
    context = {"form": form}
    return render(request, "skill_form.html", context)


def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.error(request, f"{skill.name} has been deleted!")
        return redirect("user-profile")
    context = {"skill": skill}
    return render(request, "delete-skill.html", context)


@login_required(login_url="login_user")
def inbox(request):
    profile = request.user.profile
    texts = profile.messages.all()
    unreadCount = texts.filter(is_read=False).count()
    print(unreadCount)
    context = {"texts": texts, "unreadCount": unreadCount}
    return render(request, "inbox.html", context)


def messageInbox(request, pk):
    text = Message.objects.get(id=pk)
    sender = Profile.objects.get(username=text.sender)
    if text.is_read == False:
        text.is_read = True
        text.save()
    context = {"text": text, "sender": sender}
    return render(request, "message.html", context)


def messageForm(request, pk):
    receiver = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.sender = sender
            text.receiver = receiver

            if sender:
                text.name = sender.username
            text.save()
            messages.success(
                request, f"Message has been sent to {receiver} successfully"
            )
            return redirect("single-profile", pk=receiver.id)

    context = {"form": form, "profile": receiver}
    return render(request, "message_form.html", context)
