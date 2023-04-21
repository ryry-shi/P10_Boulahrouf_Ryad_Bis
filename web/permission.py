from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Projects, Issue, Contributors, MyUser


class MyProjectPermission(BasePermission):


    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_user = ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        if obj.author_user_id == request.user:
            return True
        for contrib in contributor_user:
            print(request.user.id, contrib)
            if request.user.id == contrib:
                return request.method in SAFE_METHODS
            if obj.author_user_id == request.user:
                return True
            else:
                self.message = "you are not contributor"
                return False

class MyIssuePermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        # issue_author = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        # contributors = Contributors.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user.id)
        # print(contributors  )
        # if issue_author.author_user_id == request.user:
        #     return True
        # elif contributors == request.user.id:
        #     return True
        
        
    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_project = ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        for contrib in contributor_project:
            print(contrib)
            if request.user == obj.author_user_id :
                return True
            elif request.user == obj.assignee_user_id :
                return True
            elif request.user.id == contrib :
                return request.method in SAFE_METHODS 
            elif request.user == obj.assignee_user_id :
                return True
            else:
                self.message = "you are not contributor or author"
                return False
                
class ContributorPermission(BasePermission):

    def has_permission(self, request, view):
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        contributors = Contributors.objects.get(user_id=request.user.id)
        if project.author_user_id == request.user:
            return True
        elif contributors.user_id == request.user.id and contributors.project_id == project.project_id:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        contributor_project =  ([elt.user_id for elt in Contributors.objects.filter(project_id=obj.project_id)])
        author = Projects.objects.get(project_id=obj.project_id)
        for contributor in contributor_project:
            if author.author_user_id == request.user:
                return True
            elif contributor == request.user.id:
                return request.method in SAFE_METHODS
            else:
                self.message = "you are not author or contributor"
                return False

class MyCommentPermission(BasePermission):
    
    def has_permission(self, request, view):
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        contributors = Contributors.objects.get(project_id=view.kwargs.get("project_pk"), user_id=request.user.id)
        if project.author_user_id == request.user:
            return True
        elif contributors.user_id == request.user.id:
            return True
        
    def has_object_permission(self, request, view, obj, **kwargs):
        contributor_project =  ([elt.user_id for elt in Contributors.objects.filter(project_id=view.kwargs.get("project_pk"))])
        project = Projects.objects.get(project_id=view.kwargs.get("project_pk"))
        for contributor in contributor_project:
            if obj.author_user_id.id == contributor:
                return True
            elif request.user == contributor:
                return request.method in SAFE_METHODS
            elif project.author_user_id == request.user:
                return request.method in SAFE_METHODS
            else:
                self.message = "false"
                return False
