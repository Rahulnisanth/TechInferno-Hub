from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def projects(request):
      projects = Project.objects.all()
      context = {'projects' : projects}
      return render(request, 'projects.html', context)

def singleProject(request, pk):
      projectObj = Project.objects.get(id=pk)
      context = {'projectObj' : projectObj }
      return render(request, 'single-project.html', context)

def createProject(request):
      return render(request, 'project_form.html')