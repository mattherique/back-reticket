from src.transaction_app.models import Transaction
from src.transaction_app.serializers import TransactionSerializer

def create_transaction(data: dict) -> Transaction:
    serializer = TransactionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_transaction(transaction: Transaction, data: dict) -> Transaction:
    serializer = TransactionSerializer(transaction, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
