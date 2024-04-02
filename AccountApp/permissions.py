from rest_framework.permissions import BasePermission

class IsPublicProfileOrAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user.username)
        if request.user.is_superuser:
            return True
        return request.user.is_public