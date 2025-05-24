from django.urls import path
from src.ticket_app.views import ListTicketsView, SingleTicketView, ListTicketsByView

urlpatterns = [
    path('tickets', ListTicketsView.as_view(), name='list-tickets'),
    path('ticket', SingleTicketView.as_view(), name='single-ticket'),
    path('tickets/by/', ListTicketsByView.as_view(), name='single-ticket-with-id'),
]
