from django.core.exceptions import ObjectDoesNotExist

from src.batch_app.models import Batch
from typing import Iterable

def get_all_batches() -> Iterable[Batch]:
    return Batch.objects.all()

def get_batch(batch_id: int) -> Batch | None:
    try:
        return Batch.objects.get(id=batch_id)
    except ObjectDoesNotExist:
        return None