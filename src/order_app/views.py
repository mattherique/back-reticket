from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from src.order_app.models import Order
from src.order_app.selectors import get_all_orders, get_order, get_orders_by_filter
from src.order_app.services import create_order, update_order
from src.order_app.serializers import OrderSerializer

class ListOrdersView(APIView):
    class_model = Order
    serializer_class = OrderSerializer

    def get(self, request):
        orders = get_all_orders(request.query_params)
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "orders": serializer.data,
            "count": len(orders)
        })

class ListOrdersByView(APIView):
    class_model = Order
    serializer_class = OrderSerializer

    def get(self, request):
        orders = get_orders_by_filter(request.query_params)
        serializer = OrderSerializer(orders, many=True)
        return Response({
            "count": len(orders),
            "orders": serializer.data
        })

class SingleOrderView(APIView):
    class_model = Order
    serializer_class = OrderSerializer

    def get(self, request, pk):
        try:
            order = get_order(pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Order not found"}, status=404)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_order(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            update_order(pk, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Order not found"}, status=404)
