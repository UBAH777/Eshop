import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eshop.settings')


app = Celery('Eshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


"""
celery beat tasks
"""
app.conf.beat_schedule = {
    'send-spam-every-10-minutes': {
        'task': 'contact.tasks.send_beat_email',
        'schedule': crontab(minute='*/1'),
    },
}
