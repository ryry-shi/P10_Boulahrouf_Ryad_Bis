from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializer import ProjectSerializer, ContributorSerializer
from .models import Projects, Contributors

class ProjectAPIView(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer


    def get_queryset(self, *args, **kwargs):
        return Projects.objects.filter(author_user_id=self.request.user)

    def get(self, *args, **kwargs):
        project = Projects.objects.get(author_user_id="username")  
        self.serializer_class = self.serializer_class(project)
        return Response(project)

    def create(self, request, *args, **kwargs):
        project = Projects(author_user_id=self.request.user)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, project_id, *args, **kwargs):
        project_data = Projects.objects.get(pk=project_id)
        project_data.delete()
        return project_data

    def put(self, project_id, *args, **kwargs):
        project_data = Projects.objects.get(pk=project_id)
        serializer = self.serializer_class(data=project_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ContributorAPIView(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributors.objects.filter()