from django.db import models


class Sport(models.Model):
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
