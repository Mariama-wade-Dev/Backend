from django.urls import path, include
from .views import RegisterView, MyTokenObtainPairView # Importe ta nouvelle vue ici
from rest_framework_simplejwt.views import TokenRefreshView
from django_rest_passwordreset.views import ResetPasswordConfirm # Ajoute cet import

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Pour le bouton "Mot de passe oublié" (Demander le lien)
    path('forgot-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    # Pour le formulaire "Réinitialiser" (Changer le mot de passe)
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset_confirm')),
]
