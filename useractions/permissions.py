from rest_framework import permissions

from useractions.models import Problem


# Permission for adding of question by users only in problems where user is owner
class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        if list(request.data) == []:
            return request.user.is_authenticated
        else:
            question = request.data.get('question', {})
            result = dict(question)
            data = Problem.objects.get(pk=result['title_id'])
        return request.user.id == data.owner_id and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
