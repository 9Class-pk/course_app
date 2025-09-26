from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Разрешает доступ только владельцу объекта.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user



class IsTeacher(BasePermission):
    """
    Разрешает доступ только пользователям с ролью teacher
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'


class IsStudent(BasePermission):
    """
    Разрешает доступ только пользователям с ролью student
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'