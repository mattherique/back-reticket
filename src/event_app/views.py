from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from src.event_app.models import Event
from src.event_app.selectors import get_all_events, get_event
from src.event_app.services import create_event, update_event
from src.event_app.serializers import EventSerializer
from rest_framework import viewsets

class ListEvents(APIView):

    class_model = Event
    serializer_class = EventSerializer
    
    def get(self, request):
        events = get_all_events()
        serializer = EventSerializer(events, many=True)
        return Response({"events": serializer.data})

class SingleEventView(APIView):

    class_model = Event
    serializer_class = EventSerializer

    def get(self, request, pk):
        try:
            event = get_event(pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event not found"}, status=404)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_event(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            serializer = EventSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            update_event(pk, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Event not found"}, status=404)