import pytest
from django.test import Client

from movies.models.movie import Movie
from movies.models.moviefinance import MovieFinance
from movies.models.studio import Studio


@pytest.mark.django_db
def test_step1(
    client: Client,
    django_assert_num_queries,
):

    # Given some test data:
    studio = Studio.objects.create(name="studio1")

    for i in range(0, 10):
        movie = Movie.objects.create(
            title=f"movie {i}",
            release_year=1928,
            studio=studio,
        )

        movie.finance = MovieFinance.objects.create(
            movie=movie,
            budget=1234.0,
            box_office=1234560.0,
        )
        movie.save()

    # When the page is requested:

    with django_assert_num_queries(1):
        response = client.get("/step1/")

    # Then the expected data is returned.
    assert response.context["movie_list"].count() == 10
