from django.dispatch import receiver
from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Lien qui pointe vers ta page React
    reset_url = f"http://localhost:3000/reset-password?token={reset_password_token.key}"

    message = f"""
    Bonjour,
    
    Vous avez demandé un nouveau mot de passe pour Red Product.
    Utilisez le code suivant : {reset_password_token.key}
    Ou cliquez sur ce lien : {reset_url}
    """

    send_mail(
        "Réinitialisation de mot de passe - Red Product",
        message,
        "noreply@redproduct.com",
        [reset_password_token.user.email],
        fail_silently=False,
    )