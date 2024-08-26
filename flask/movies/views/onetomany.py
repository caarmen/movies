from sqlalchemy import select
from sqlalchemy.orm import selectinload

from flask import Blueprint, render_template
from movies.dbsession import db, get_async_session
from movies.models import Studio

bp = Blueprint("onetomany", __name__, url_prefix="/onetomany")


@bp.route("/async/nplus1", methods=("GET",))
async def async_nplus1():
    async with get_async_session() as session:
        studios = (await session.scalars(select(Studio))).all()
        for studio in studios:
            await studio.awaitable_attrs.movies
        return render_template(
            "movies/onetomany.html",
            studio_list=studios,
        )


@bp.route("/async/optim", methods=("GET",))
async def async_optim():
    async with get_async_session() as session:
        studios = (
            await session.scalars(select(Studio).options(selectinload(Studio.movies)))
        ).all()
        return render_template(
            "movies/onetomany.html",
            studio_list=studios,
        )


@bp.route("/sync/nplus1", methods=("GET",))
def sync_nplus1():
    studios = db.session.scalars(select(Studio)).all()
    return render_template(
        "movies/onetomany.html",
        studio_list=studios,
    )


@bp.route("/sync/optim", methods=("GET",))
def sync_optim():
    studios = db.session.scalars(
        select(Studio).options(selectinload(Studio.movies))
    ).all()
    return render_template(
        "movies/onetomany.html",
        studio_list=studios,
    )
