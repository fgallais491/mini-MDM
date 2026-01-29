from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Fleet, Device


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ['id','name']


class UserSerializer(serializers.ModelSerializer):
    fleets = FleetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'fleets']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'