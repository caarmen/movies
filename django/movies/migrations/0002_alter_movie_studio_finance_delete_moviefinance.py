# Generated by Django 5.1 on 2024-08-28 22:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="studio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="movies.studio"
            ),
        ),
        migrations.CreateModel(
            name="Finance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "budget",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=13,
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=0)
                        ],
                    ),
                ),
                (
                    "box_office",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=13,
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=0)
                        ],
                    ),
                ),
                (
                    "movie",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="MovieFinance",
        ),
    ]