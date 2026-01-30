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
        return Fleet.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsOwnerOfFleetDevice]

    def get_queryset(self):
        queryset = Device.objects.filter(fleet__owner=self.request.user)
        fleet_id = self.request.query_params.get('fleet')
        if fleet_id:
            queryset = queryset.filter(fleet_id=fleet_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save()
