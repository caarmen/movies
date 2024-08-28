import asyncio
import csv

from sqlalchemy import delete, select, text

from flask import Blueprint
from movies.dbsession import get_async_session
from movies.models import Actor, Movie, MovieFinance, Studio

bp = Blueprint("import", __name__)


@bp.cli.command("csv")
def import_movies():
    async def command():
        async with get_async_session() as session:
            # Delete all data
            await session.execute(text("pragma foreign_keys=on"))
            await session.execute(delete(Movie))
            await session.execute(delete(MovieFinance))
            await session.execute(delete(Studio))
            await session.execute(delete(Actor))
            await session.commit()

            with open("../data/studios.csv") as studios_file, open(
                "../data/actors.csv"
            ) as actors_file, open("../data/movies.csv") as movies_file, open(
                "../data/actor_movies.csv"
            ) as actor_movies_file:
                studios_reader = csv.DictReader(studios_file)
                actors_reader = csv.DictReader(actors_file)
                movies_reader = csv.DictReader(movies_file)
                actor_movies_reader = csv.DictReader(actor_movies_file)

                for studio_line in studios_reader:
                    session.add(Studio(**studio_line))

                for actor_line in actors_reader:
                    session.add(Actor(**actor_line))

                await session.commit()

                for movie_line in movies_reader:
                    studio: Studio = (
                        await session.scalars(
                            select(Studio).filter_by(name=movie_line["studio"])
                        )
                    ).one()
                    movie = Movie(
                        title=movie_line["title"],
                        release_year=int(movie_line["release_year"]),
                        studio=studio,
                    )

                    finance = MovieFinance(
                        movie=movie,
                        budget=float(movie_line["budget"]),
                        box_office=float(movie_line["box_office"]),
                    )
                    session.add(movie)
                    session.add(finance)

                await session.commit()
                for actor_movie_line in actor_movies_reader:
                    actor: Actor = (
                        await session.scalars(
                            select(Actor).filter_by(
                                first_name=actor_movie_line["first_name"],
                                last_name=actor_movie_line["last_name"],
                            )
                        )
                    ).one()
                    session.add(actor)
                    await session.commit()
                    await session.refresh(actor, ["movies"])
                    movie: Movie = (
                        await session.scalars(
                            select(Movie).filter_by(
                                title=actor_movie_line["title"],
                            )
                        )
                    ).one()
                    actor.movies.append(movie)
                    await session.commit()

                    # await session.commit()

    asyncio.run(command())
