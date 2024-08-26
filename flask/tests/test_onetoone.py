from flask.testing import FlaskClient
import pytest
from flask import Flask
from flask_sqlalchemy import record_queries
from movies.models.movie import Movie
from movies.models.moviefinance import MovieFinance
from movies.models.studio import Studio
from movies.dbsession import db


@pytest.mark.parametrize(
    argnames=["route", "expected_sql_query_count"],
    argvalues=[
        ("/onetoone/sync/nplus1", 11),
        ("/onetoone/sync/optim", 1),
    ],
)
def test_onetoone(
    app: Flask,
    client: FlaskClient,
    captured_templates: list,
    route: str,
    expected_sql_query_count: int,
):
    with app.app_context():
        # Given some test data:
        studio = Studio(name="studio1")

        for i in range(0, 10):
            movie = Movie(
                title=f"movie {i}",
                release_year=1928,
                studio=studio,
            )

            finance = MovieFinance(
                movie=movie,
                budget=1234.0,
                box_office=1234560.0,
            )
            db.session.add(movie)
            db.session.add(finance)

        db.session.commit()

    # When the page is requested:

    with app.test_request_context() as ctx:
        response = client.get(route)
        assert response.status_code == 200

        assert len(record_queries.get_recorded_queries()) == expected_sql_query_count
        # Then the expected data is returned.
        template, context = captured_templates[0]

        assert len(context["movie_list"]) == 10
