from django.shortcuts import render, redirect
from projects.utils import SearchProjects
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def projects(request):
      projects, search_query = SearchProjects(request)
      context = {'projects' : projects, 'search_query' : search_query}
      return render(request, 'projects.html', context)

@login_required(login_url='login_user')
def singleProject(request, pk):
      projectObj = Project.objects.get(id=pk)
      context = {'project' : projectObj }
      return render(request, 'single-project.html', context)

@login_required(login_url='login_user')
def createProject(request):
      profile = request.user.profile
      project_form = ProjectForm(instance=profile)
      if request.method == 'POST':
            project_form = ProjectForm(request.POST, request.FILES)
            if project_form.is_valid():
                  project = project_form.save(commit=False)
                  project.owner = profile
                  project.save()
                  return redirect('projects')
      context = {'form' : project_form}
      return render(request, 'project_form.html', context)

def updateProject(request, pk):
      profile = request.user.profile
      project = profile.project_set.get(id=pk)
      project_form = ProjectForm(instance=project)
      if request.method == 'POST':
            project_form = ProjectForm(request.POST, request.FILES, instance=project)
            if project_form.is_valid():
                  project_form.save()
                  return redirect('projects')
      context = {'form' : project_form}
      return render(request, 'project_form.html', context)

def deleteProject(request, pk):
      profile = request.user.profile
      project = profile.project_set.get(id=pk)
      project_form = ProjectForm(instance=project)
      if request.method == 'POST':
            project.delete()
            return redirect('projects')
      context = {'object' : project}
      return render(request, 'delete-project.html', context)