from flask_sqlalchemy import SQLAlchemy

from movies.models.base import Base

sync_url = "sqlite:////tmp/movies.db"
db = SQLAlchemy(model_class=Base)
