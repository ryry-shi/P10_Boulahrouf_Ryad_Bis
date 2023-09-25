from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Projects, Issue, Contributors, MyUser


class MyProjectPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_user = ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        if obj.author_user_id == request.user:
            return True
        for contrib in contributor_user:
            if request.user.id == contrib.id:
                return request.method in SAFE_METHODS
            if obj.author_user_id == request.user:
                return True
        else:
            self.message = "You are not author or contributor of this project"
            return False

class MyIssuePermission(BasePermission):
    
    def has_permission(self, request, view):
        issue_author = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        if issue_author.author_user_id == request.user or Contributors.objects.filter(project_id=issue_author.project_id, user_id=request.user.id):
            return True

    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_project = ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        for contrib in contributor_project:
            if request.user == obj.author_user_id :
                return request.method in SAFE_METHODS 
            elif request.user == obj.assignee_user_id :
                return True
            elif request.user == contrib :
                return request.method in SAFE_METHODS 
        else:
            self.message = "You are not author or contributor of this project"
            return False
                
class ContributorPermission(BasePermission):

    def has_permission(self, request, view):
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        if project.author_user_id == request.user:
            return True
        elif Contributors.objects.filter(user_id=request.user.id , project_id=project.project_id):
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        contributor_project =  ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        author = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        for contributor in contributor_project:
            if author.author_user_id == request.user:
                return True
            elif contributor == request.user:
                return request.method in SAFE_METHODS
        else:
            self.message = "You are not author or contributor of this project"
            return False

class MyCommentPermission(BasePermission):
    
    def has_permission(self, request, view):
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        if project.author_user_id == request.user or Contributors.objects.filter(project_id=project.project_id, user_id=request.user.id):
            return True

        
    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_project =  ([elt.user_id for elt in Contributors.objects.filter(project_id=view.kwargs.get("project_pk"))])
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        for contributor in contributor_project:
            if obj.author_user_id.id == request.user.id:
                 return True
            elif contributor == contributor:
                 return request.method in SAFE_METHODS
            elif project.author_user_id == request.user:
                return request.method in SAFE_METHODS
        else:
            self.message = "You are not author or contributor of this project"
            return False
