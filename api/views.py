from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Fleet, Device
from .serializers import UserSerializer, FleetSerializer, DeviceSerializer

from .permissions import IsOwnerOfFleetDevice

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FleetViewSet(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer


    def get_queryset(self):
        return Fleet.objects.filter(owner = self)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.owner)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsOwnerOfFleetDevice]

    def get_queryset(self):
        return Device.objects.filter(fleet_owner = self.request.user)
