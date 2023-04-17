from rest_framework import permissions


class AnonimCanReadOnly(permissions.BasePermission):
    """Разрешает анонимному пользователю только безопасные запросы."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    

# class IsSuperUserOrIsAdminOnly(permissions.BasePermission):
#     """
#     Права на осуществление запросов суперпользователю Джанго,
#     админу Джанго, аутентифицированному пользователю с ролью admin.
#     """

#     def has_permission(self, request, view):
#         return (
#             request.user.is_authenticated
#             and (request.user.is_superuser
#                  or request.user.is_staff
#                  or request.user.is_admin)
#         )
