from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate


      
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = serializer.instance

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'message': 'User registered successfully', 'token': access_token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    print("Email:", email)
    print("Password", password)

    # Authenticate user
    user = authenticate(request, email=email, password=password)
    print("Authenticated User", user)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'token': access_token}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)