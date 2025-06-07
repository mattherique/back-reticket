from rest_framework import serializers
from .models import Ticket
from src.event_app.models import Event
from src.user_app.models import User

class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Ticket
        fields = '__all__'
