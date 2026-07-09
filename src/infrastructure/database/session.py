from sqlmodel import create_engine,Session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from src.core.config import settings

_psql_engine = create_engine(
    url=settings.POSTGRESQL_URL
)

_psql_session_maker = sessionmaker(
    class_=Session, autocommit=False, autoflush=False, bind=_psql_engine
)

@contextmanager
def get_psql_session():
    session = _psql_session_maker()
    try:
        yield session
    finally:
        session.close()