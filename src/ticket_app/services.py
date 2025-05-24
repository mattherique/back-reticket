from src.ticket_app.models import Ticket
from src.ticket_app.serializers import TicketSerializer

def create_ticket(data: dict) -> Ticket:
    serializer = TicketSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_ticket(ticket: Ticket, data: dict) -> Ticket:
    serializer = TicketSerializer(ticket, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
