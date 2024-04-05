from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError


class CheckInsRepository:
    '''This class is responsible for handling the checkins table.'''

    def insert_check_in(self, attendee_id: str) -> str:
        '''This method inserts a new checkin into the checkins table.'''
        with db_connection_handler as database:
            try:
                check_in = CheckIns(attendee_id=attendee_id)
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            
            except IntegrityError:
                raise Exception(f"Attendee with id {attendee_id} already checked in.")
            
            except Exception as exception:
                database.session.rollback()
                raise exception