from django.db import models
from src.user_app.models import User

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Pending'),
        (2, 'Completed'),
        (3, 'Failed'),
        (4, 'Refunded'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    payment_method = models.IntegerField(choices=[
        (1, 'Credit Card'),
        (2, 'Debit Card'),
        (3, 'Pix'),
        (4, 'Billet'),
    ], null=True)

    class Meta:
        db_table = 'db_transactions'
        verbose_name = 'Transaction'
