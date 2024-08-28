from sqlalchemy import Column, ForeignKey, Table

from movies.models.base import Base

actor_movies_table = Table(
    "actor_movies",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
    Column("actor_id", ForeignKey("actors.id", ondelete="CASCADE"), primary_key=True),
)
