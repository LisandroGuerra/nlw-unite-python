'''This module is responsible for creating the events table.'''

from sqlalchemy import Column, Integer, String
from src.models.settings.base import Base

class Events(Base):
    '''This class is responsible for creating the events table.'''
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)


    def __repr__(self) -> str:
        event_info = [f"{key}={value}" for key, value in self.__dict__.items()
                      if not key.startswith('_')]
        return f"Events ({', '.join(event_info)})"
