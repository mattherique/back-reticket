from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from src.user_app.models import User
from src.user_app.selectors import get_all_users, get_user, get_users_by_filter
from src.user_app.services import create_user, update_user
from src.user_app.serializers import UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

class ListUsersView(APIView):
    class_model = User
    serializer_class = UserSerializer

    def get(self, request):
        users = get_all_users(request.query_params)
        serializer = UserSerializer(users, many=True)
        return Response(
            {
                "users": serializer.data,
                "count": len(users),
            }
        )


class ListUsersByView(APIView):
    class_model = User
    serializer_class = UserSerializer

    def get(self, request):
        users = get_users_by_filter(request.query_params)
        serializer = UserSerializer(users, many=True)
        return Response(
            {
                "count": len(users),
                "users": serializer.data,
            }
        )


class SingleUserView(APIView):
    class_model = User
    serializer_class = UserSerializer

    def get(self, request, pk):
        try:
            user = get_user(pk)
            if not user:
                return Response({"error": "User not found"}, status=404)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=404)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_user(data)
        return Response(status=201)

    def put(self, request, pk):
        try:
            user = get_user(pk)
            if not user:
                return Response({"error": "User not found"}, status=404)
            serializer = UserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            update_user(user, serializer.validated_data)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=404)

class UserLoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = authenticate(username=request.data["email"], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        
class UserRegistrationView(CreateAPIView):
    class_model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny]