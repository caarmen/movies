from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from movies.models.studio import Studio


class Movie(models.Model):
    title = models.CharField(max_length=128)
    release_year = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1874),
            MaxValueValidator(limit_value=3000),
        ],
    )
    studio = models.ForeignKey(
        Studio,
        on_delete=models.PROTECT,
    )
