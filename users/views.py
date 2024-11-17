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
        serializers.save()
        user = User.objects.get(username=data['username'])
        user.set_password(data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
     
    return Response({'message':  'ERROR' })




@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    
    user = User.objects.get(username=username)
    if not user.check_password(password):
        return Response({'message': 'Wrong Password!'}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key})





@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    print('Dostup')
    return Response({'message': 'SUCCESS'})