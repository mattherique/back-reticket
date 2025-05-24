from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from src.transaction_app.models import Transaction
from src.transaction_app.selectors import get_all_transactions, get_transaction, get_transactions_by_filter
from src.transaction_app.services import create_transaction, update_transaction
from src.transaction_app.serializers import TransactionSerializer

class ListTransactionsView(APIView):
    class_model = Transaction
    serializer_class = TransactionSerializer

    def get(self, request):
        transactions = get_all_transactions()
        serializer = TransactionSerializer(transactions, many=True)
        return Response({"Transaction": serializer.data})

class ListTransactionsByView(APIView):
    class_model = Transaction
    serializer_class = TransactionSerializer

    def get(self, request):
        transactions = get_transactions_by_filter(request.query_params)
        serializer = TransactionSerializer(transactions, many=True)
        return Response({
            "count": len(transactions),
            "Transaction": serializer.data
        })

class SingleTransactionView(APIView):
    class_model = Transaction
    serializer_class = TransactionSerializer

    def get(self, request, pk):
        try:
            transaction = get_transaction(pk)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Transaction not found"}, status=404)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_transaction(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            update_transaction(pk, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Transaction not found"}, status=404)
