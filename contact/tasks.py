from Eshop.celery import app

from .service import send, send_mail
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписаны на рассылку',
            'Будет очень много спама',
            'djangosc876@gmail.com',
            [contact.email],
            fail_silently=False,
        )
