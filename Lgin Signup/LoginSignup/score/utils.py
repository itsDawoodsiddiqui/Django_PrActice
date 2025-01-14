from django.conf import settings
from django.core.mail import send_mail

def send_mail_token(email, token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/score/{token}/'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_form, recipient_list)
        
    except Exception as e:
        return False
    return True    