from src.user_app.models import User
from src.user_app.serializers import UserSerializer

def create_user(data: dict) -> User:
    """
    Create a new user in the database.
    Args:
        data (dict): The data for the new user.
    Returns:
        User: The created User object.
    """
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def update_user(user: User, data: dict) -> User:
    """
    Update an existing user in the database.
    Args:
        user (User): The user to update.
        data (dict): The new data for the user.
    Returns:
        User: The updated User object.
    """
    serializer = UserSerializer(user, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
