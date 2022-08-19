from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name: 'Service'
        verbose_name_plural: 'Services'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
