from rest_framework.permissions import BasePermission
from src.ticket_app.models import Ticket

class IsTicketOwner(BasePermission):
    """
    Allows access only to the owner of the ticket.
    """
    def has_object_permission(self, request, view, obj) -> bool:
        return obj.user == request.user

    def has_permission(self, request, view):
        # Allow permission checks for GET, PUT, etc. (object-level will be checked later)
        return True
