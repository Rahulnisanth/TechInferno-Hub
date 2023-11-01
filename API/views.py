from rest_framework.response import Response
from .serializers import ProjectSerializer, ProfileSerializer
from projects.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from user.models import *

@api_view(['GET','POST'])
def getRoutes(request):
      routes = [
            {'GET': '/api/projects'},
            {'GET': '/api/projects/id'},
            {'POST': '/api/projects/id/vote'},
            {'POST': '/api/users/token'},
            {'POST': '/api/users/token/refresh'},
      ]
      return Response(routes)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getProjects(request):
      projects = Project.objects.all()
      serializer = ProjectSerializer(projects, many=True)
      return Response(serializer.data)

@api_view(['GET','POST'])
def getProject(request, pk):
      project = Project.objects.get(id=pk)
      serializer = ProjectSerializer(project, many=False)
      return Response(serializer.data)

@api_view(['GET','POST'])
def getProfiles(request):
      profiles = Profile.objects.all()
      serializer = ProfileSerializer(profiles, many=True)
      return Response(serializer.data)

@api_view(['GET','POST'])
def getProfile(request, pk):
      profile = Profile.objects.get(id=pk)
      serializer = ProfileSerializer(profile, many=False)
      return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
      tagId = request.data['tag']
      projectId = request.data['project']

      project = Project.objects.get(id=projectId)
      tag = Tag.objects.get(id=tagId)

      project.tags.remove(tag)
      return Response('Tag was deleted!')