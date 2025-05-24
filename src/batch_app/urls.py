from django.urls import path
from src.batch_app.views import ListBatchesView, SingleBatchView, ListBatchesByView

urlpatterns = [
    path('batches', ListBatchesView.as_view(), name='list-batches'),
    path('batch', SingleBatchView.as_view(), name='single-batch'),
    path('batches/by', ListBatchesByView.as_view(), name='single-batch'),
]