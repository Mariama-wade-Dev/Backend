# from django.shortcuts import render

# # Create your views here.





from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer # Importe le nouveau serializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView # Importe la vue JWT

# Vue pour l'inscription (déjà existante, on la garde)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

# Nouvelle vue pour la connexion (Login)
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer # Utilise notre serializer personnalisé