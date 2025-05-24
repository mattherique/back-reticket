from django.core.exceptions import ObjectDoesNotExist
from src.user_app.models import User
from typing import Iterable
import json

def get_all_users(params) -> Iterable[User]:
    """
    Get all users from the database.
    Returns:
        Iterable[User]: An iterable of User objects.
    """
    params_filter = {}
    if params:
        params_filter = params
    return User.objects.filter(**params_filter)

def get_users_by_filter(params) -> Iterable[User]:
    """
    Get users by filter from the database.
    Args:
        params (dict): The filter parameters.
    Returns:
        Iterable[User]: An iterable of User objects.
    """
    params_filter = {}
    if params:
        params_filter = json.loads(params["filter_by"])
    return User.objects.filter(**params_filter)

def get_user(user_id: int) -> User | None:
    """
    Get a user by its ID.
    Args:
        user_id (int): The ID of the user.
    Returns:
        User: The User object with the given ID.
    """
    try:
        return User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return None
