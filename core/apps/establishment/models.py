from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from apps.user.models import UserAccount
from apps.service.models import Service


class Establishment(models.Model):
    name = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to='photos/%Y/%m')
    address = models.CharField(max_length=255)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name
