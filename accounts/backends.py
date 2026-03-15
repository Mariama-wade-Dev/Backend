from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # On utilise .filter().first() au lieu de .get() pour éviter le crash 
            # si plusieurs utilisateurs ont été créés par erreur avec le même email.
            user = User.objects.filter(Q(username=username) | Q(email=username)).first()
            
            if user is None:
                return None
                
            if user.check_password(password):
                return user
        except Exception:
            return None
        return None