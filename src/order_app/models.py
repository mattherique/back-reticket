from django.db import models
from src.transaction_app.models import Transaction
from src.user_app.models import User

class Order(models.Model):
    total_amount = models.DecimalField(max_digits=16, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Pending'),
        (2, 'Completed'),
        (3, 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(max_length=128)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    class Meta:
        db_table = 'db_orders'
        verbose_name = 'Order'