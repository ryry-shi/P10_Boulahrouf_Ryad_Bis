from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializer import ProjectSerializer
from .models import Projects

class ProjectAPIView(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    # queryset = Projects.objects.all()


    def get_queryset(self):
        return Projects.objects.filter(author_user_id=1)

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

    # def post(self, request,*args, **kwargs):

    #     project_data = request.data
    #     serializer = self.serializer_class(data=project_data)
    #     if serializer.is_valid:
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
