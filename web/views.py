from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from web.permission import MyIssuePermission, MyProjectPermission

from .serializer import (
    IssueSerializer,
    ProjectSerializer,
    ContributorSerializer,
    CommentSerializer,
)
from .models import Comment, Projects, Contributors, Issue, Comment


class ProjectAPIView(viewsets.ModelViewSet):
    permission_classes = [MyProjectPermission]
    serializer_class = ProjectSerializer

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        return Projects.objects.all()

    def create(self, request, *args, **kwargs):
        project = Projects(author_user_id=self.request.user)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

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

    def get_queryset(self, **kwargs):
        print(self.kwargs)
        print(self.request.user.id)
        return Contributors.objects.filter(project_id=self.kwargs["project_pk"])

    def create(self, request, *arg, **kwargs):
        issue_data = Contributors(
            project_id=self.kwargs.get("project_pk"), user_id=self.request.user.id
        )
        serializer = self.serializer_class(issue_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, project_id, *args, **kwargs):
        author = Contributors.objects.get(pk=project_id)
        author.delete()
        return author

    def put(self, *args, **kwargs):
        print(self.kwargs)
        author = Contributors.objects.get(pk=self.kwargs["projects_id"])
        serializer = self.serializer_class(data=author)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class IssueAPIView(viewsets.ModelViewSet):
    permission_classes = [MyIssuePermission]
    serializer_class = IssueSerializer

    def get_queryset(self, **kwargs):
        return Issue.objects.all()

    def create(self, request, *arg, **kwargs):
        issue_data = Issue(
            author_user_id=self.request.user,
            assignee_user_id=self.request.user,
            project_id=self.kwargs.get("project_pk"),
        )
        serializer = self.serializer_class(issue_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, project_id, *args, **kwargs):
        issue = Issue.objects.get(pk=project_id)
        issue.delete()
        return issue

    def put(self, *args, **kwargs):
        author = Issue.objects.get(pk=self.kwargs.get["projects_id"])
        serializer = self.serializer_class(data=author)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self, **kwargs):
        print(self.kwargs.get("issue_pk"))
        return Comment.objects.all()

    def create(self, request, *arg, **kwargs):
        comment = Comment(author_user_id=self.request.user)
        serializer = self.serializer_class(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, project_id, *args, **kwargs):
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return comment

    def put(self, *args, **kwargs):
        comment = Comment.objects.get(pk=id)
        serializer = self.serializer_class(data=comment)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
