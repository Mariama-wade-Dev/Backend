from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# 1. Serializer pour l'Inscription (Register)
class UserSerializer(serializers.ModelSerializer):
    # On définit 'name' pour matcher ton "setName" du frontend
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # On utilise 'name' du front comme 'username' pour Django
        user = User.objects.create_user(
            username=validated_data['name'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # ÉTAPE 1 : On déclare explicitement le champ email pour que le serializer l'accepte
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ÉTAPE 2 : On supprime le champ username automatique
        if 'username' in self.fields:
            self.fields.pop('username')

    def validate(self, attrs):
        # ÉTAPE 3 : On prend la valeur de l'email et on la met dans 'username'
        # pour que le backend d'authentification (EmailBackend) puisse travailler
        attrs['username'] = attrs.get('email')
        
        # On appelle la validation parente qui va utiliser notre EmailBackend
        data = super().validate(attrs)
        return data
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token