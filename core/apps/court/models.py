from django.db import models
from datetime import datetime
from apps.sport.models import Sport
from apps.establishment.models import Establishment


class Court(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=5)
    establishmet = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
