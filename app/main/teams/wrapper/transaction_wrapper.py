import functools

from flask import current_app
from mongoengine import get_connection, get_db

TRANSACTION_DB = 'TRANSACTION_DB'
TRANSACTION_SESSION = 'TRANSACTION_SESSION'


def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        mongo = get_connection()
        kwargs.setdefault(TRANSACTION_DB, mongo.get_database(get_db().name))
        if current_app and not current_app.testing:
            with mongo.start_session() as session:
                with session.start_transaction():
                    try:
                        kwargs.setdefault(TRANSACTION_SESSION, session)
                        return func(*args, **kwargs)
                    except Exception as e:
                        session.abort_transaction()
                        raise e
        else:
            kwargs.setdefault(TRANSACTION_SESSION, {})
            return func(*args, **kwargs)

    return wrapper
