from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')
    location = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'db_users'