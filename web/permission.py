from rest_framework.permissions import BasePermission
from rest_framework import permissions


class MyProjectPermission(BasePermission):
    message = "You're not allowed because you're not the authoa."

    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username:
            return True
        elif request.method == "POST":
            return True
        return False
