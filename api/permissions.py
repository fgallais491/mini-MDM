from rest_framework import permissions

class IsOwnerOfFleetDevice(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        obj.fleet.owner == request.user

