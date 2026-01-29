from rest_framework import permissions

class IsOwnerOfFleetDevice(permissions, permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        object.fleet.owner == request.user

