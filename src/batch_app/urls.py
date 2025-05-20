from django.urls import path
from rest_framework.routers import DefaultRouter

from src.batch_app.views import ListBatches, SingleBatchView

router_list = DefaultRouter()

router_list.register(
    prefix=r'list-events', 
    viewset=ListBatches, 
    basename='list-events'
)

router_list.register(
    prefix=r'event-detail(/(?P<pk>[^/.]+))?', 
    viewset=SingleBatchView, 
    basename='event-detail'
)

urlpatterns = [
    path('batches', ListBatches.as_view(), name='list-batches'),
    path('batch', SingleBatchView.as_view(), name='single-batch'),
]