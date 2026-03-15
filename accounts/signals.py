from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings 
from django_rest_passwordreset.signals import reset_password_token_created

from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created: 
        subject = "Bienvenue chez Red Product !"
        message = f"""
        Bonjour {instance.username},
        
        Merci d'avoir rejoint Red Product. Votre compte a été créé avec succès.
        Vous pouvez maintenant gérer vos hôtels et suivre vos produits en toute simplicité.
        
        L'équipe Red Product.
        """
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # REMPLACE PAR TON URL VERCEL
    frontend_url = "https://produit-frontend-mariama-wade-devs-projects.vercel.app"
    reset_url = f"{frontend_url}/reset-password?token={reset_password_token.key}"

    message = f"""
    Bonjour,
    
    Vous avez demandé un nouveau mot de passe pour Red Product.
    Utilisez le code suivant : {reset_password_token.key}
    Ou cliquez sur ce lien : {reset_url}
    """
    # ... reste du code send_mail

    send_mail(
        "Réinitialisation de mot de passe - Red Product",
        message,
        settings.EMAIL_HOST_USER,  
        [reset_password_token.user.email],
        fail_silently=False,
    )