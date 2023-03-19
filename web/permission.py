from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Projects, Issue, Contributors
from django.shortcuts import get_object_or_404


class MyProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            False

    def has_object_permission(self, request, view, obj):
        project = Projects(author_user_id=request.user)

        if project.author_user_id == obj.author_user_id:
            return True
        else:
            self.message = "this is not your project"
            False

class ContributorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            False

    def has_object_permission(self, request, view, obj):
        contributor = Contributors.objects.filter(project_id=self.project_id)
        if contributor.project_id == obj.user_id:
            return True
        else:
            self.message = "this is not your project"
            False

class MyIssuePermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool
        elif request.method == "POST":
            return bool(...) 
        elif request.method == "PUT" or request.method == "DELETE":
            return bool(...) #idem que ci dessous, sinon bloquant


    def has_object_permission(self, request, view, obj):

        author_issue = Issue(author_user_id=obj.author_user_id)
        if author_issue.author_user_id == request.user.id:
            return True
        else:
            self.message = "you cannot read"
            return False