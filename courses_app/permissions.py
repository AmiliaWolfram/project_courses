from rest_framework.permissions import BasePermission


class OwnerOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.author)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and
                    obj.user.tutor == request.user.tutor)


# class IsAuthorOrIsAuthenticated(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif request.user and request.user.is_authenticated:
#             return True
#         return False
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif request.user.is_authenticated and obj.author.user == request.user:
#             return True
#         return False


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_staff:
            return True
