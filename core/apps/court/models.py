from django.db import models
from datetime import datetime
from apps.sport.models import Sport


class Court(models.Model):
    name = models.CharField(max_length=255)
