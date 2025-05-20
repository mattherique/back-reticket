from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=[
        ('open', 'Open'), 
        ('closed', 'Closed')
    ], default='open')
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'db_events'