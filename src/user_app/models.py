from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_hash = models.CharField(max_length=256)
    # status = models.CharField(max_length=32, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='open')
    sal = models.CharField(max_length=128)

    class Meta:
        db_table = 'db_users'