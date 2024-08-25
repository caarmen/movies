from sqlalchemy.orm import Mapped, mapped_column

from movies.models.base import Base


class Studio(Base):
    __tablename__ = "studios"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
