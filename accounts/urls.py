from django.urls import path, include
from .views import RegisterView, MyTokenObtainPairView # Importe ta nouvelle vue ici
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    # On remplace TokenObtainPairView par MyTokenObtainPairView
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Remplace la ligne password_reset par celle-ci :
    path('forgot-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
