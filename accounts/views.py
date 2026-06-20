from rest_framework import generics, status
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

# 1. Vue pour la connexion (Login) - OK
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# 2. Vue pour l'inscription (Register) - VERSION CORRIGÉE
class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Veuillez remplir tous les champs (email, password)"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=email).exists():
            return Response({"error": "Cet utilisateur existe déjà"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            return Response({
                "message": "Utilisateur créé avec succès !",
                "user": {"username": user.username, "email": user.email}
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Création sécurisée
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({
                "message": "Utilisateur créé avec succès !",
                "user": {"username": user.username, "email": user.email}
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)