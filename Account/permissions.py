from rest_framework.permissions import BasePermission

class IsPublicProfileOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_public