import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='This test creates new register in DB.')
def test_insert_event():
    events_repository = EventsRepository()
    events_info = {
        'uuid': 'uuid-event-3',
        'title': 'Event 3',
        'details': 'Details of event 3',
        'slug': 'slug-event-3',
        'maximum_attendees': 30
    }
    response = events_repository.insert_event(events_info)
    print(response)
    assert response == events_info


@pytest.mark.skip(reason='This test is unescessary.')
def test_get_event_by_uuid():
    events_repository = EventsRepository()
    event_uuid = 'uuid-event-2'
    response = events_repository.get_event_by_uuid(event_uuid)
    print(response)
    assert response.id == event_uuid
    assert response.title == 'Event 2'
    assert response.details == 'Details of event 2'
    assert response.slug == 'slug-event-2'
    assert response.maximum_attendees == 20
