from django.core.exceptions import ObjectDoesNotExist

from src.event_app.models import Event
from typing import Iterable

def get_all_events() -> Iterable[Event]:
    """
    Get all events from the database.

    Returns:
        Iterable[Event]: An iterable of Event objects.
    """
    return Event.objects.all()

def get_event(event_id: int) -> Event | None:
    """
    Get an event by its ID.

    Args:
        event_id (int): The ID of the event.

    Returns:
        Event: The Event object with the given ID.
    """
    try:
        return Event.objects.get(id=event_id)
    except ObjectDoesNotExist:
        return None