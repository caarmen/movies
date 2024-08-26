from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from movies.models.base import Base


class Studio(Base, AsyncAttrs):
    __tablename__ = "studios"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    movies: Mapped[list["Movie"]] = relationship(
        back_populates="studio",
    )
