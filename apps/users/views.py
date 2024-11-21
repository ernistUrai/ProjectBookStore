from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    data = request.data
    serializers = UserSerializer(data=data)
    if serializers.is_valid():
        user = serializers.save()
        user.set_password(data['password'])
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
     
    return Response({'message': 'Такой имени пользователя уже существует!',
                     'message2': 'Пожалуйста, Попробуйте еще раз!',
                     
                     },
                    status=status.HTTP_400_BAD_REQUEST
                    )

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'Не найден пользователь!'}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response({'message': 'Не верный пароль!'}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'message': 'Успешно!'}, status=status.HTTP_200_OK)

