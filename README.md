Run scheduled task

`celery -A dj_scraper worker -B -l info` // if we don't use database scheduler

To run schedules task from database
`celery -A dj_scraper worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

To get celery results, after installing package
create the cache table
`python manage.py createcachetable`
