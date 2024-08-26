from pathlib import Path

from flask import template_rendered
import pytest

from alembic import command
from alembic.config import Config
from movies.main import create_app


@pytest.fixture
def db_path(tmp_path: Path) -> str:
    return str(tmp_path / "database.db")


@pytest.fixture(autouse=True)
def apply_alembic_migration(
    db_path: str,
    monkeypatch: pytest.MonkeyPatch,
):
    with monkeypatch.context() as mp:
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", f"sqlite+aiosqlite:///{db_path}")
        command.upgrade(alembic_cfg, "head")


@pytest.fixture()
def app(db_path):
    app = create_app(db_url=f"sqlite:///{db_path}")

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


# https://stackoverflow.com/a/58204843
@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **kwargs):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        recorded.clear()
        template_rendered.disconnect(record, app)
