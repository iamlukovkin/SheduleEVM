"""Connection to database."""
import sqlalchemy as sa
import config
from .models import Base
from sqlalchemy.orm import sessionmaker


engine: sa.engine.base.Engine = sa.create_engine(config.DATABASE['ConnectionString'])
Base.metadata.create_all(engine)


def get_engine() -> sa.engine.base.Engine:
    """Get engine."""
    return engine


def get_connection() -> sa.engine.base.Connection:
    """Get connection."""
    return engine.connect()


def get_session():
    """Get session."""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def close_connection():
    """Close connection."""
    engine.dispose()


def close_session():
    """Close session."""
    engine.dispose()
