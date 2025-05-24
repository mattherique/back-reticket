from django.core.exceptions import ObjectDoesNotExist

from src.batch_app.models import Batch
from typing import Iterable
import json

def get_all_batches() -> Iterable[Batch]:
    return Batch.objects.all()

def get_batches_by_filter(params) -> Iterable[Batch]:
    """
    Get batches by filter from the database.

    Args:
        params (dict): The filter parameters.

    Returns:
        Iterable[Batch]: An iterable of Batch objects.
    """
    params_filter = {}

    if params:
        params_filter = json.loads(params["filter_by"])

    return Batch.objects.filter(**params_filter)

def get_batch(batch_id: int) -> Batch | None:
    try:
        return Batch.objects.get(id=batch_id)
    except ObjectDoesNotExist:
        return None