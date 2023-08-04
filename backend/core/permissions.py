from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return request.user.is_authenticated

        return True


class RecipePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author
                or request.user.is_staff
                or request.user.is_superuser)
