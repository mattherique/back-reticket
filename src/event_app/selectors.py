from django.core.exceptions import ObjectDoesNotExist

from src.event_app.models import Event
from typing import Iterable
import json

def get_all_events(params) -> Iterable[Event]:
    """
    Get all events from the database.

    Returns:
        Iterable[Event]: An iterable of Event objects.
    """
    params_filter = {}

    if params:
        params_filter = params

    return Event.objects.filter(**params_filter)

def get_events_by_filter(params) -> Iterable[Event]:
    """
    Get events by filter from the database.

    Args:
        params (dict): The filter parameters.

    Returns:
        Iterable[Event]: An iterable of Event objects.
    """
    params_filter = {}

    if params:
        params_filter = json.loads(params["filter_by"])

    return Event.objects.filter(**params_filter)

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