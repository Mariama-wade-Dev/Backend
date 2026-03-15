from django.db import models
from cloudinary.models import CloudinaryField # Ajoute cet import

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='F XOF')
    
    # Utilise CloudinaryField au lieu de ImageField
    image = CloudinaryField('image', null=True, blank=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)

    # Correction du nom de la fonction (enlever le "cl")
    def __str__(self):
        return self.name