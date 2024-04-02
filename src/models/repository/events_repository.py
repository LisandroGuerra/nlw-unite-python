from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events

class EventsRepository:
    def insert_event(self, events_info: Dict) -> Dict:
        '''This method is responsible for inserting an event into the database.'''
        with db_connection_handler as database:
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
        

    def get_event_by_uuid(self, event_uuid: str) -> Events:
        '''This method is responsible for retrieving an event from the database by its uuid.'''
        with db_connection_handler as database:
            event = database.session.query(Events).filter(Events.id == event_uuid).one()
            return event