from sqlalchemy import ForeignKey, SmallInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from movies.models.actormovies import actor_movies_table
from movies.models.base import Base


class Movie(Base, AsyncAttrs):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    release_year: Mapped[int] = mapped_column(SmallInteger())
    finance: Mapped["Finance"] = relationship(back_populates="movie")
    studio_id: Mapped[int] = mapped_column(
        ForeignKey(
            "studios.id",
            ondelete="RESTRICT",
        )
    )
    studio: Mapped["Studio"] = relationship(
        back_populates="movies",
    )
    actors: Mapped[list["Actor"]] = relationship(
        secondary=actor_movies_table,
        back_populates="movies",
        cascade="all, delete",
    )
