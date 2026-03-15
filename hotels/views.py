from django.shortcuts import render
from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.permissions import IsAuthenticated

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # On protège la route : il faut être connecté pour voir/créer des hôtels
    permission_classes = [IsAuthenticated]
