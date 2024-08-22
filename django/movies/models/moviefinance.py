from django.core.validators import MinValueValidator
from django.db import models
from movies.models.movie import Movie


class MovieFinance(models.Model):
    movie = models.OneToOneField(
        Movie,
        on_delete=models.CASCADE,
        related_name="finance",
    )
    budget = models.DecimalField(
        validators=[MinValueValidator(limit_value=0)],
        max_digits=13,
        decimal_places=2,
    )
    box_office = models.DecimalField(
        validators=[MinValueValidator(limit_value=0)],
        max_digits=13,
        decimal_places=2,
    )
