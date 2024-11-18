from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSerializer(data=data)
    
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(data['password'])  # Паролду хэш кылып сактоо
        user.save()
        
        token, created = Token.objects.get_or_create(user=user)  # Токенди алуу же түзүү
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)  # Успешный жооп
    
    return Response({'message': 'ERROR', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  # Ката жөнүндө маалымат