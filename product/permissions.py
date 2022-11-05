from rest_framework import permissions
from rest_framework.views import Request, View


class IsSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method == "GET"
            or request.user.is_authenticated
            and request.user.is_seller
        )


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == "GET" or request.user == obj.seller
