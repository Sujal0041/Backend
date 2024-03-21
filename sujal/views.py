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
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions


      
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
    try:
        # permission_classes = (permissions.AllowAny,)
        data = request.data
        email = data.get('email')
        password = data.get('password')

        print("Email:", email)
        print("Password", password)

        print("Email type:", type(email))
        print("Password type:", type(password))

        print(request)

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        print("Authenticated User", user)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        # Log other exceptions for debugging purposes
        print("Unexpected error:", e)
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)