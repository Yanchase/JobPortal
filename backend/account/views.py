from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def register(request):
    user = SignUpSerializer(data=request.data)
    if user.is_valid():
        if not User.objects.filter(username=user.data['email']).exists():
            user = User.objects.create(
                first_name=user.data['first_name'],
                last_name=user.data['last_name'],
                username=user.data['email'],
                email=user.data['email'],
                password=make_password(user.data['password'])
            )
            return Response({'message:':'User registered'}, status=201)
        else:
          return Response({
            'error': 'User already exists with this email. Please login.'}, status=400)
    else:
        return Response({user.errors}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = UserSerializer(request.user)
    return Response(user.data)