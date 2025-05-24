from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from src.batch_app.models import Batch
from src.batch_app.selectors import get_all_batches, get_batch, get_batches_by_filter
from src.batch_app.services import create_batch, update_batch
from src.batch_app.serializers import BatchSerializer
from rest_framework import viewsets

class ListBatchesView(APIView):

    class_model = Batch
    serializer_class = BatchSerializer

    def get(self, request):
        batch = get_all_batches()
        serializer = BatchSerializer(batch, many=True)
        return Response({"Batch": serializer.data})
    
class ListBatchesByView(APIView):
    class_model = Batch
    serializer_class = BatchSerializer

    def get(self, request):
        batch = get_batches_by_filter(request.query_params)
        serializer = BatchSerializer(batch, many=True)
        return Response({
            "count": len(batch),
            "Batch": serializer.data
        })

class SingleBatchView(APIView):

    class_model = Batch
    serializer_class = BatchSerializer

    def get(self, request, pk):
        try:
            Batch = get_batch(pk)
            serializer = BatchSerializer(Batch)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Batch not found"}, status=404)

    def post(self, request):
        serializer = BatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_batch(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            serializer = BatchSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            update_batch(pk, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Batch not found"}, status=404)