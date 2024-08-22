from django.db import models
from movies.models.movie import Movie


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    movies = models.ManyToManyField(
        Movie,
    )
