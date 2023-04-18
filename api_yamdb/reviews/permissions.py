from rest_framework.permissions import BasePermission


class IsAdminOrModerator(BasePermission):
  
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or (request.user.is_staff or request.user.is_superuser)

    # def has_permission(self, request, obj):
    #     return obj.author == request.user or (request.user.is_staff or request.user.is_superuser)





    # def has_permission(self, request, view, obj):
    #     # Allow GET, HEAD or OPTIONS requests.
    #     if request.method in ['GET', 'HEAD', 'OPTIONS']:
    #         return True

    #     # Check if user is the author of the object.
    #     if obj.author == request.user:
    #         return True

    #     # Check if user is an admin or moderator.
    #     return request.user.is_staff or request.user.is_superuser
