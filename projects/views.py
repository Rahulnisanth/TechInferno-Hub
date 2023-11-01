from django.shortcuts import render, redirect
from projects.utils import SearchProjects, paginateProjects
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def projects(request):
      projects, search_query = SearchProjects(request)
      custom_range, projects = paginateProjects(request, projects, 9)
      context = {'projects' : projects, 'search_query' : search_query, 'custom_range' : custom_range}
      return render(request, 'projects.html', context)

@login_required(login_url='login_user')
def singleProject(request, pk):
      projectObj = Project.objects.get(id=pk)
      form = ReviewForm()
      if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                  review = form.save(commit=False)
                  review.owner = request.user.profile
                  review.project = projectObj
                  review.save()
                  projectObj.getVotetotal
                  messages.success(request, "Review Submitted Successfully!")
                  return redirect('single-project', pk=projectObj.id)
      context = {'project' : projectObj, 'form':form}
      return render(request, 'single-project.html', context)

@login_required(login_url='login_user')
def createProject(request):
      profile = request.user.profile
      project_form = ProjectForm(instance=profile)
      if request.method == 'POST':
            newtags = request.POST.get('newtags').replace(',',' ').split()
            project_form = ProjectForm(request.POST, request.FILES)
            if project_form.is_valid():
                  project = project_form.save(commit=False)
                  project.owner = profile
                  project.save()
                  for tag in newtags:
                        tag, created = Tag.objects.get_or_create(name=tag)
                        project.tags.add(tag)
                  return redirect('projects')
      context = {'form' : project_form}
      return render(request, 'project_form.html', context)

def updateProject(request, pk):
      profile = request.user.profile
      project = profile.project_set.get(id=pk)
      project_form = ProjectForm(instance=project)
      if request.method == 'POST':
            newtags = request.POST.get('newtags').replace(',',' ').split()
            project_form = ProjectForm(request.POST, request.FILES, instance=project)
            if project_form.is_valid():
                  project_form.save()
                  for tag in newtags:
                        tag, created = Tag.objects.get_or_create(name=tag), True
                        project.tags.add(tag)
                  return redirect('projects')
      context = {'form' : project_form, 'project':project}
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