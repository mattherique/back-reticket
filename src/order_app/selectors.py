from django.core.exceptions import ObjectDoesNotExist
from src.order_app.models import Order
from typing import Iterable
import json

def get_all_orders(params) -> Iterable[Order]:
    params_filter = {}
    if params:
        params_filter = params
    return Order.objects.filter(**params_filter)

def get_orders_by_filter(params) -> Iterable[Order]:
    params_filter = {}
    if params:
        params_filter = json.loads(params["filter_by"])
    return Order.objects.filter(**params_filter)

def get_order(order_id: int) -> Order | None:
    try:
        return Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return None
