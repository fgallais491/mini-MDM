from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Fleet, Device
from .serializers import UserSerializer, FleetSerializer, DeviceSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FleetViewSet(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
