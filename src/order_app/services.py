from src.order_app.models import Order
from src.order_app.serializers import OrderSerializer

def create_order(data: dict) -> Order:
    serializer = OrderSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_order(order: Order, data: dict) -> Order:
    serializer = OrderSerializer(order, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
