from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
      flag = 'login'
      if request.user.is_authenticated:
            return redirect('/')
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                  login(request, user)
                  messages.success(request, 'User has logged in successfully')
                  return redirect('/')
            else:
                  messages.error(request, 'An Error has occurred')
                  return render(request, 'login.html')
      return render(request, 'login.html')

def logout_user(request):
      logout(request)
      messages.info(request, 'User has logged out')
      return redirect('/')

def registerUser(request):
      flag = 'register'
      form = CustomUserCreationForm
      if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save(commit=False)
                  user.save()
                  messages.success(request, 'User was successfully registered')
                  login(request, user)
                  return redirect('/')
      context = {'flag' : flag, 'form' : form}
      return render(request, 'login.html', context)

@login_required(login_url='login_user')
def userProfile(request):
      return render(request, 'user-profile.html')

def profiles(request):  
      profiles = Profile.objects.all()
      context = {'profiles' : profiles}
      return render(request, 'profiles.html', context)

@login_required(login_url='login_user')
def singleProfile(request, pk):
      profile = Profile.objects.get(id=pk)
      context = {'profile' : profile}
      return render(request, 'single-profile.html', context)