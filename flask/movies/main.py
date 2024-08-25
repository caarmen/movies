import logging

import uvicorn

from flask import Flask


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static/",
    )
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app(),
        host="127.0.0.1",
        port=8001,
        log_level="debug",
    )
