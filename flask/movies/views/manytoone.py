from sqlalchemy import select
from sqlalchemy.orm import joinedload

from flask import Blueprint, render_template
from movies.dbsession import db, get_async_session
from movies.models import Movie

bp = Blueprint("manytoone", __name__, url_prefix="/manytoone")


@bp.route("/async/nplus1", methods=("GET",))
async def async_nplus1():
    async with get_async_session() as session:
        movies = (await session.scalars(select(Movie))).all()
        for movie in movies:
            await movie.awaitable_attrs.studio
        return render_template(
            "movies/manytoone.html",
            movie_list=movies,
        )


@bp.route("/async/optim", methods=("GET",))
async def async_optim():
    async with get_async_session() as session:
        movies = (
            await session.scalars(select(Movie).options(joinedload(Movie.studio)))
        ).all()
        return render_template(
            "movies/manytoone.html",
            movie_list=movies,
        )


@bp.route("/sync/nplus1", methods=("GET",))
def sync_nplus1():
    movies = db.session.scalars(select(Movie)).all()
    return render_template(
        "movies/manytoone.html",
        movie_list=movies,
    )


@bp.route("/sync/optim", methods=("GET",))
def sync_optim():
    movies = db.session.scalars(
        select(Movie).options(
            joinedload(
                Movie.studio,
            )
        ),
    ).all()
    return render_template(
        "movies/manytoone.html",
        movie_list=movies,
    )
