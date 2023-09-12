import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

RUNNING_ENVIRONMENT = os.environ.get('RUNNING_ENVIRONMENT')
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'app.settings.{RUNNING_ENVIRONMENT}')


app = Celery('app')
app.conf.enable_utc = False
app.conf.timezone = os.environ.get('TIME_ZONE')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



app.conf.beat_schedule ={
    'db-backup':{
        'task':'core.tasks.db_backup_task',
        'schedule':crontab(minute=3,hour=5), # works every day 15 min
    },
 

}
