from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@shared_task
def send_verification_email(name, email, otp, subject, message, template_name):
    try:
        from_email = settings.EMAIL_HOST_USER

        template_path = f'mail/{template_name}.html'
        context = {
            'name': name,
            'otp': otp,
            'message': message,
            'email': email,
        }

        html_message = render_to_string(template_path, context)

        to = email  # Send to actual user, not hardcoded
        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(html_message, 'text/html')

        msg.send()
    except Exception as e:
        print("Error sending email:", e)
        raise e
