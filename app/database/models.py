"""Database models."""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Lesson(Base):
    """Lesson model."""

    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group = Column(String)
    day = Column(String)
    time = Column(String)
    week = Column(String)
    lesson = Column(String)

    def get_group(self):
        """Get group."""
        return self.group.replace('gr_', '')