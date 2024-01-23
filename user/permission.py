from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthor(BasePermission):
    message = "You're not allowed because you're not the authoa."


    def has_permission(self, request, view):
        if request.user:
            return True
    
    
def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return request.method in permissions.SAFE_METHODS

