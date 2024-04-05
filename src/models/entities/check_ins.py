
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql.functions import func
from src.models.settings.base import Base

class Checkins(Base):
    '''This class is responsible for creating the checkins table.'''
    __tablename__ = 'checkins'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendee_id = Column(String, ForeignKey('attendees.id'))


    def __repr__(self) -> str:
        '''This method returns the string representation of the Checkins class.'''
        return f"Checkins [attendee_id={self.attendee_id}, created_at={self.created_at}]"