from flask_sqlalchemy import SQLAlchemy, record_queries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from movies.models.base import Base


def get_async_session() -> async_sessionmaker[AsyncSession]:
    url = "sqlite+aiosqlite:////tmp/movies.db"
    engine = create_async_engine(url)
    record_queries._listen(engine.sync_engine)
    return async_sessionmaker(engine)


sync_url = "sqlite:////tmp/movies.db"
db = SQLAlchemy(model_class=Base)
