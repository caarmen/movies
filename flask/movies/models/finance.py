from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from movies.models.base import Base


class Finance(Base):
    __tablename__ = "finance"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    budget: Mapped[float] = mapped_column()
    box_office: Mapped[float] = mapped_column()
    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movies.id", ondelete="CASCADE"),
        unique=True,
    )
    movie: Mapped["Movie"] = relationship(back_populates="finance")
