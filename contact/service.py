from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписаны на рассылку',
        'Будет очень много спама',
        'djangosc876@gmail.com',
        [user_email],
        fail_silently=False,
    )
