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




class IsTeacherOwner(BasePermission):
    def has_permission(self, request, view):

    # create actions: только teacher или admin
        if view.action in ["create"]:
            return bool(request.user and request.user.is_authenticated and request.user.role in ("teacher", "admin"))
    # остальные действия будут проверяться на уровне объекта
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.role == "admin":
            return True
    # course ownership
        if hasattr(obj, "created_by"):
            return obj.created_by == request.user
    # lesson -> course.created_by
        if hasattr(obj, "course") and hasattr(obj.course, "created_by"):
            return obj.course.created_by == request.user
    # assignment -> lesson -> course.created_by
        if hasattr(obj, "lesson") and hasattr(obj.lesson.course, "created_by"):
            return obj.lesson.course.created_by == request.user
        return False