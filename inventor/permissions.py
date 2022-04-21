from rest_framework.permissions import BasePermission


class IsInventor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_inventor)


class IsInvestor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_investor)