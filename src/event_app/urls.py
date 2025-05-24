from django.urls import path
from src.event_app.views import ListEventsView, SingleEventView, ListEventsByView

urlpatterns = [
    path('events', ListEventsView.as_view(), name='list-events'),
    path('event', SingleEventView.as_view(), name='single-event'),
    path('events/by/', ListEventsByView.as_view(), name='single-event-with-id'),
]