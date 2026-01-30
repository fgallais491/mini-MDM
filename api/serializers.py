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

    def validate_fleet(self, fleet):
        user = self.context['request'].user
        if fleet.owner != user:
            raise serializers.ValidationError("You can only assign devices to your own fleets.")
        return fleet

    def validate(self, data):
        user = self.context['request'].user
        if not user.fleets.exists():
            raise serializers.ValidationError("You must own at least one fleet to create a device.")
        return data
