from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.user_app.models import User
from src.user_app.serializers import UserSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_view(request):
    try:
        if request.method == 'GET':
            user = User.objects.get(pk=request.query_params.get('id'))
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)

        elif request.method == 'POST':
            user_data = request.data

            new_user = User.objects.create(
                username=user_data.get('username'),
                email=user_data.get('email'),
                is_active=user_data.get('is_active'),
                date_joined=user_data.get('date_joined')
            )

            serializer = UserSerializer(new_user)

            return Response(serializer.data, status=201)

        elif request.method == 'PUT':
            user_data = request.data

            user = User.objects.get(pk=user_data.get('id'))

            if "username" in user_data:
                user.username = user_data.get('username')
            if "email" in user_data:
                user.email = user_data.get('email')
            if "is_active" in user_data:
                user.is_active = user_data.get('is_active')
            if "date_joined" in user_data:
                user.date_joined = user_data.get('date_joined')

            user.save()
            return Response(status=200)

        elif request.method == 'DELETE':
            user_data = request.data

            user = User.objects.get(pk=user_data.get('id'))

            if user.is_active:
                user.is_active = False
                user.save()

            return Response(status=200)

    except ObjectDoesNotExist:
        return Response(status=400)

    except Exception as e:
        return Response({'error': str(e)}, status=500)