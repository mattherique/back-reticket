from src.batch_app.models import Batch
from src.batch_app.serializers import BatchSerializer


def create_batch(data: dict) -> Batch:
    serializer = BatchSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_batch(batch: Batch, data: dict) -> Batch:
    serializer = BatchSerializer(batch, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()