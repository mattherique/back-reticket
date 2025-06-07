from django.db import models
from src.event_app.models import Event
from src.order_app.models import Order
from src.user_app.models import User

class Ticket(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=[
        (1, 'Used'),
        (2, 'Active'),
        (3, 'Expired'),
        (4, 'Excluded'),
    ])
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets', null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='tickets',
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    price_blocked = models.BooleanField(default=False)
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bought_tickets',
        null=True,
    )
    
    class Meta:
        db_table = 'db_tickets'
        verbose_name = 'Ticket'
