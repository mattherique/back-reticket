from django.core.exceptions import ObjectDoesNotExist
from src.ticket_app.models import Ticket
from typing import Iterable
import json

def get_all_tickets() -> Iterable[Ticket]:
    return Ticket.objects.all()

def get_tickets_by_filter(params) -> Iterable[Ticket]:
    params_filter = {}
    if params:
        params_filter = json.loads(params["filter_by"])
    return Ticket.objects.filter(**params_filter)

def get_ticket(ticket_id: int) -> Ticket | None:
    try:
        return Ticket.objects.get(id=ticket_id)
    except ObjectDoesNotExist:
        return None
