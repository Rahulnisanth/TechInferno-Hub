from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
      if request.user.is_authenticated:
            return redirect('/')
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                  login(request, user)
                  return redirect('/')
            else:
                  return render(request, 'login.html')
      return render(request, 'login.html')

def logout_user(request):
      logout(request)
      return redirect('/')


def profiles(request):  
      profiles = Profile.objects.all()
      context = {'profiles' : profiles}
      return render(request, 'profiles.html', context)

@login_required(login_url='login_user')
def singleProfile(request, pk):
      profile = Profile.objects.get(id=pk)
      context = {'profile' : profile}
      return render(request, 'single-profile.html', context)