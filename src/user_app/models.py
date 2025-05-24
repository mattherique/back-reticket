from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_hash = models.CharField(max_length=256)
    sal = models.CharField(max_length=128)
    status = models.CharField(max_length=32, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'db_users'