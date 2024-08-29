import pytest
from django.test import Client
from pytest_django import DjangoAssertNumQueries

from movies.models.movie import Movie
from movies.models.finance import Finance
from movies.models.studio import Studio


@pytest.mark.parametrize(
    argnames=["route", "expected_sql_query_count"],
    argvalues=[
        ("/onetoone/nplus1/", 11),
        ("/onetoone/optim/", 1),
    ],
)
@pytest.mark.django_db
def test_one_to_one(
    client: Client,
    django_assert_num_queries: DjangoAssertNumQueries,
    route: str,
    expected_sql_query_count: int,
):

    # Given some test data:
    studio = Studio.objects.create(name="studio1")

    for i in range(0, 10):
        movie = Movie.objects.create(
            title=f"movie {i}",
            release_year=1928,
            studio=studio,
        )

        movie.finance = Finance.objects.create(
            movie=movie,
            budget=1234.0,
            box_office=1234560.0,
        )
        movie.save()

    # When the page is requested:

    with django_assert_num_queries(expected_sql_query_count):
        response = client.get(route)

    # Then the expected data is returned.
    assert response.context["movie_list"].count() == 10
