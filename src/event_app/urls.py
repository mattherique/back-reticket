from django.urls import path
from rest_framework.routers import DefaultRouter

from src.event_app.views import ListEvents, SingleEventView

router_list = DefaultRouter()
router_list.register(
    prefix=r'list-events', 
    viewset=ListEvents, 
    basename='list-events'
)
router_list.register(
    prefix=r'event-detail(/(?P<pk>[^/.]+))?', 
    viewset=SingleEventView, 
    basename='event-detail'
)

urlpatterns = [
    path('events', ListEvents.as_view(), name='list-events'),
    path('event', SingleEventView.as_view(), name='single-event'),
]