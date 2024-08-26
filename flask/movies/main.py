import logging
from asyncio import iscoroutinefunction

import uvicorn
from asgiref.sync import async_to_sync
from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask
from movies.commands import importcsv
from movies.dbsession import db, sync_url


class MyDebugToolbarExtension(DebugToolbarExtension):
    def process_view(self, app, view_func, view_kwargs):
        processed_view = super().process_view(app, view_func, view_kwargs)
        if iscoroutinefunction(processed_view):
            processed_view = async_to_sync(processed_view)
        return processed_view


def create_app(db_url=sync_url):
    from movies.views import full, step1, step2, step3

    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static/",
    )
    app.register_blueprint(step1.bp)
    app.register_blueprint(step2.bp)
    app.register_blueprint(step3.bp)
    app.register_blueprint(full.bp)
    app.register_blueprint(importcsv.bp)
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    app.config["SECRET_KEY"] = "<replace with a secret key>"
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    db.init_app(app)
    MyDebugToolbarExtension(app)
    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app(),
        host="127.0.0.1",
        port=8001,
        log_level="debug",
    )
