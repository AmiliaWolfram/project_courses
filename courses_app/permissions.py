from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTutorStaffOrIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated and request.user.is_approved and obj.tutor.user == request.user:
            return True


class IsStudentOrTutor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            # Check if the user is a student or tutor
            return request.user.is_student or request.user.is_tutor
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            # Check if the user is a student or tutor and has access to the object
            return (request.user.is_student and obj.student.user == request.user) or (request.user.is_tutor and obj.tutor.user == request.user)
        return False
