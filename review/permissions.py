from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj):
        return request.user == obj.user
    
