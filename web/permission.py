from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Projects, Issue, Contributors, MyUser
from django.shortcuts import get_object_or_404


class MyProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj, **kwargs):
        contributor = get_object_or_404(Projects, pk=obj.project_id)
        contributor_user = ([elt.user_id for elt in Contributors.objects.all()])
        for contrib in contributor_user:
            if request.user.id == contrib:
                self.message = "true"
                return True
                
        # if request.user.id == contributor_user :

        else:
            self.message = "false"
            return False
        
class ContributorPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        author = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        print(author)
        if author.author_user_id == request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False
        
class MyIssuePermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        author_issue = Issue(author_user_id=obj.author_user_id)
        if author_issue.author_user_id == request.user.id:
            return True
        else:
            self.message = "you cannot read"
            return False