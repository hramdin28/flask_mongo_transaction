import pytest
from mongoengine import disconnect, connect

from app import create_app


@pytest.fixture()
def app():
    app = create_app('test')
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def mongo_db():
    disconnect()
    connection = connect(db='mongotest', host='mongomock://localhost')
    yield connection
    disconnect()
