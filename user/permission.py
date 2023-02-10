from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    message = "You're not allowed because you're not the authoa."

    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username:
            return True
        elif request.method == 'POST':
            return True
        return False


