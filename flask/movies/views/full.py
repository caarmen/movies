from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from flask import Blueprint, render_template
from movies.dbsession import db, get_async_session
from movies.models import Movie

bp = Blueprint("full", __name__, url_prefix="/full")


@bp.route("/async/nplus1", methods=("GET",))
async def async_nplus1():
    async with get_async_session() as session:
        movies = (await session.scalars(select(Movie))).all()
        for movie in movies:
            await movie.awaitable_attrs.actors
            await movie.awaitable_attrs.studio
            await movie.awaitable_attrs.finance
        return render_template(
            "movies/full.html",
            movie_list=movies,
        )


@bp.route("/async/optim", methods=("GET",))
async def async_optim():
    async with get_async_session() as session:
        movies = (
            (
                await session.scalars(
                    select(Movie).options(
                        joinedload(Movie.actors),
                        joinedload(Movie.studio),
                        joinedload(Movie.finance),
                    )
                )
            )
            .unique()
            .all()
        )
        return render_template(
            "movies/full.html",
            movie_list=movies,
        )


@bp.route("/sync/nplus1", methods=("GET",))
def sync_nplus1():
    movies = db.session.scalars(select(Movie)).all()
    return render_template(
        "movies/full.html",
        movie_list=movies,
    )


@bp.route("/sync/optim", methods=("GET",))
def sync_optim():
    movies = (
        db.session.scalars(
            select(Movie).options(
                selectinload(Movie.actors),
                joinedload(Movie.studio),
                joinedload(Movie.finance),
            )
        )
        .unique()
        .all()
    )
    return render_template(
        "movies/full.html",
        movie_list=movies,
    )
