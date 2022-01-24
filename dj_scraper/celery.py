import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_scraper.settings')
app = Celery('dj_scraper')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# app.conf.enable_utc = False

# solution for https://stackoverflow.com/a/49448256/5559590
app.conf.update(
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# app.conf.beat_schedule = {
#     'sample-task': {
#         'task': 'scrapers.tasks.sample_task',
#         # 'schedule': crontab(minute="*/1"),
#         'schedule': 30.0,
#         'args': (),
#     },
# }
# app.conf.timezone = 'UTC'
