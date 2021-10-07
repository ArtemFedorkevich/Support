from rest_framework import permissions
from .models import Problem


# Permission for adding of question by users only in problems where user is owner
class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        index = view.kwargs.get('pk')
        data = Problem.objects.get(pk=index)
        return request.user.id == data.owner_id and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
