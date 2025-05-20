from django.db import models
from .constants import BATCH_STATUS
from src.event_app.models import Event

class Batch(models.Model):

    name = models.CharField(
        max_length=128
    )

    description = models.TextField(
        blank=True, 
        verbose_name='Description'
    )

    limit = models.IntegerField(
        default=0, 
        verbose_name='Limit'
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At'
    )

    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Updated At'
    )

    end_date = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name='End Date'
    )

    start_date = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name='Start Date'
    )

    # status = models.PositiveSmallIntegerField(
    #     choices=BATCH_STATUS,
    #     default=0,
    #     verbose_name='Status'
    # )
    
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='batches',
        verbose_name='Event'
    )

    class Meta:
        db_table = 'db_batches'