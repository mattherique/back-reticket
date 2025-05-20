from src.event_app.models import Event
from src.event_app.serializers import EventSerializer


def create_event(data: dict) -> Event:
    """
    Create a new event in the database.

    Args:
        data (dict): The data for the new event.

    Returns:
        Event: The created Event object.
    """
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_event(event: Event, data: dict) -> Event:
    """
    Update an existing event in the database.

    Args:
        event (Event): The event to update.
        data (dict): The new data for the event.

    Returns:
        Event: The updated Event object.
    """
    serializer = EventSerializer(event, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()