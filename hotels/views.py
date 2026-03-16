# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Hotel
# from .serializers import HotelSerializer
# from rest_framework.permissions import IsAuthenticated

# class HotelViewSet(viewsets.ModelViewSet):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer
#     # On protège la route : il faut être connecté pour voir/créer des hôtels
#     permission_classes = [IsAuthenticated]

from rest_framework import viewsets, permissions
from .models import Hotel
from .serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    # On s'assure que seul un utilisateur connecté peut accéder aux hôtels
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Cette méthode filtre les hôtels. 
        L'utilisateur ne verra que les hôtels qu'il a créés.
        """
        user = self.request.user
        return Hotel.objects.filter(owner=user)

    def perform_create(self, serializer):
        """
        Cette méthode s'exécute lors de la création (POST).
        Elle définit l'owner comme étant l'utilisateur actuellement connecté.
        """
        serializer.save(owner=self.request.user)