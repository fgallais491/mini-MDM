from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Fleet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fleets")

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE, related_name="devices")
    status = models.CharField(max_length=50, default="offline")

    def __str__(self):
        return self.name
