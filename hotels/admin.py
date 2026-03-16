# from django.contrib import admin
# from .models import Hotel

# @admin.register(Hotel)
# class HotelAdmin(admin.ModelAdmin):
#     # Les colonnes qui s'affichent dans la liste principale
#     list_display = ('id', 'name', 'address', 'price', 'currency')
    
#     # Rendre certains champs cliquables pour ouvrir la fiche
#     list_display_links = ('id', 'name')
    
#     # Ajouter une barre de recherche (pratique quand tu auras beaucoup d'hôtels)
#     search_fields = ('name', 'address')
    
#     # Ajouter des filtres sur le côté droit
#     list_filter = ('currency',)
    
#     # Nombre d'éléments par page
#     list_per_page = 20

# # Si tu as d'autres modèles comme 'Room' ou 'User', tu les ajouteras ici plus tard

from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    # Ajoute 'owner' ici pour voir quel utilisateur a créé quel hôtel
    list_display = ('id', 'name', 'address', 'price', 'currency', 'owner')
    
    list_display_links = ('id', 'name')
    
    # On peut aussi chercher par le nom de l'utilisateur (owner__username)
    search_fields = ('name', 'address', 'owner__username')
    
    # Filtre par devise ET par propriétaire
    list_filter = ('currency', 'owner')
    
    list_per_page = 20