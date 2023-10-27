from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

def projects(request):
      projects = Project.objects.all()
      context = {'projects' : projects}
      return render(request, 'projects.html', context)

def singleProject(request, pk):
      projectObj = Project.objects.get(id=pk)
      context = {'project' : projectObj }
      return render(request, 'single-project.html', context)

def createProject(request):
      project_form = ProjectForm()
      if request.method == 'POST':
            project_form = ProjectForm(request.POST, request.FILES)
            if project_form.is_valid():
                  project_form.save()
                  return redirect('projects')
      context = {'form' : project_form}
      return render(request, 'project_form.html', context)

def updateProject(request, pk):
      project = Project.objects.get(id=pk)
      project_form = ProjectForm(instance=project)
      if request.method == 'POST':
            project_form = ProjectForm(request.POST, request.FILES, instance=project)
            if project_form.is_valid():
                  project_form.save()
                  return redirect('projects')
      context = {'form' : project_form}
      return render(request, 'project_form.html', context)

def deleteProject(request, pk):
      project = Project.objects.get(id=pk)
      if request.method == 'POST':
            project.delete()
            return redirect('projects')
      context = {'object' : project}
      return render(request, 'delete-project.html', context)