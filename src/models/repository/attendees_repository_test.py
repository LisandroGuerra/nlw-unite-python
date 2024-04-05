import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Create new register in database")
def teste_insert_attendee():
    event_id = 'uuid-event-1'
    attendee_info = {
        'uuid': 'attendee-uuid-event-1',
        'name': 'Lix Doe',
        'email': 'lix.d@email.com',
        'event_id': event_id
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee_info)
    assert response == attendee_info
    print(response)


@pytest.mark.skip(reason="Integration test is not necessary at the moment")
def test_get_attendee_badge_by_id():
    attendee_id = 'attendee-uuid-event-3'
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
