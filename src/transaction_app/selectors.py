from django.core.exceptions import ObjectDoesNotExist
from src.transaction_app.models import Transaction
from typing import Iterable
import json

def get_all_transactions() -> Iterable[Transaction]:
    return Transaction.objects.all()

def get_transactions_by_filter(params) -> Iterable[Transaction]:
    params_filter = {}
    if params:
        params_filter = json.loads(params["filter_by"])
    return Transaction.objects.filter(**params_filter)

def get_transaction(transaction_id: int) -> Transaction | None:
    try:
        return Transaction.objects.get(id=transaction_id)
    except ObjectDoesNotExist:
        return None
