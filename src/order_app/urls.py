from django.urls import path
from src.order_app.views import ListOrdersView, SingleOrderView, ListOrdersByView

urlpatterns = [
    path('orders', ListOrdersView.as_view(), name='list-orders'),
    path('order', SingleOrderView.as_view(), name='single-order'),
    path('orders/by/', ListOrdersByView.as_view(), name='single-order-with-id'),
]
