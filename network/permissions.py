from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """
    Разрешение для активных сотрудников
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'is_active', False)
