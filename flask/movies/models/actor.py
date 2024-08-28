from sqlalchemy.orm import Mapped, mapped_column, relationship

from movies.models.actormovies import actor_movies_table
from movies.models.base import Base


class Actor(Base):
    __tablename__ = "actors"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    movies: Mapped[list["Movie"]] = relationship(
        secondary=actor_movies_table,
        back_populates="actors",
        cascade="all, delete",
    )
