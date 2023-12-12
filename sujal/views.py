from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

      
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    data = request.data

    print('Request Data:', data)


    # Validate and save user data
    try:
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValueError('Email and password are required.')

        user = User.objects.create(
            email=email,
            password=make_password(password),  # Hashing the password before saving
        )

        return Response({'message': 'User registered successfully'})
    except Exception as e:
        print('Error in registration:', str(e))  # Print the detailed error
        return Response({'error': str(e)}, status=400)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    print('Login Request Data:', data)

    # Authenticate user
    user = authenticate(email=data['email'].lower(), password=data['password'])

    print('Authenticated User:', user)


    print('HashedD:', User.objects.get(email=data['email']).password)


    print('Email:', data['email'])
    print('Password:', data['password'])



    if user is not None:
        print('Email in database:', User.objects.get(email=data['email']).email)
        print('Hashed Password in database:', User.objects.get(email=data['email']).password)

        if user.check_password(data['password']):
            print('Password is correct.')

        # If user is valid, generate and return an authentication token
        token, created = Token.objects.get_or_create(user=user)
        print('Generated Token:', token.key)
        return Response({'token': token.key})
    else:
        # If user is not valid, return an error message
        return Response({'error': 'Invalid credentials'}, status=401)