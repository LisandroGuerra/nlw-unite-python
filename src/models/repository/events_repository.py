from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class EventsRepository:
    def insert_event(self, events_info: Dict) -> Dict:
        '''This method is responsible for inserting an event into the database.'''
        with db_connection_handler as database:
            try:
                new_event = Events(
                id = events_info.get('uuid'),
                title = events_info.get('title'),
                details = events_info.get('details'),
                slug = events_info.get('slug'),
                maximum_attendees = events_info.get('maximum_attendees')
                )
                database.session.add(new_event)
                database.session.commit()
                #database.session.refresh(new_event)
                return events_info
            
            except IntegrityError:
                raise Exception('Event already exists in the database.')
            except Exception as exception:
                database.session.rollback()
                raise exception
        

    def get_event_by_uuid(self, event_uuid: str) -> Events:
        '''This method is responsible for retrieving an event from the database by its uuid.'''
        with db_connection_handler as database:
            try:
                event = database.session.query(Events).filter(Events.id == event_uuid).one()
                return event
            
            except NoResultFound:
                # raise Exception('Event not found in the database.')
                return None