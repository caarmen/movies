from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=64)
