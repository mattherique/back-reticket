from django.urls import path
from src.transaction_app.views import ListTransactionsView, SingleTransactionView, ListTransactionsByView

urlpatterns = [
    path('transactions', ListTransactionsView.as_view(), name='list-transactions'),
    path('transaction', SingleTransactionView.as_view(), name='single-transaction'),
    path('transactions/by/', ListTransactionsByView.as_view(), name='single-transaction-with-id'),
]
