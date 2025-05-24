from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from src.ticket_app.models import Ticket
from src.ticket_app.selectors import get_all_tickets, get_ticket, get_tickets_by_filter
from src.ticket_app.services import create_ticket, update_ticket
from src.ticket_app.serializers import TicketSerializer

class ListTicketsView(APIView):
    class_model = Ticket
    serializer_class = TicketSerializer

    def get(self, request):
        tickets = get_all_tickets()
        serializer = TicketSerializer(tickets, many=True)
        return Response({"Ticket": serializer.data})

class ListTicketsByView(APIView):
    class_model = Ticket
    serializer_class = TicketSerializer

    def get(self, request):
        tickets = get_tickets_by_filter(request.query_params)
        serializer = TicketSerializer(tickets, many=True)
        return Response({
            "count": len(tickets),
            "Ticket": serializer.data
        })

class SingleTicketView(APIView):
    class_model = Ticket
    serializer_class = TicketSerializer

    def get(self, request, pk):
        try:
            ticket = get_ticket(pk)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Ticket not found"}, status=404)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_ticket(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            serializer = TicketSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            update_ticket(pk, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Ticket not found"}, status=404)
