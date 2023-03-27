import os


from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie.settings')

app = Celery('movie')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run_movie_rating_avg_every_30": {
        'task': "task_update_movie_ratings",
        'schedule': 30 * 60,
    },
    "run_rating_export_every_hour": {
        'task': 'export_rating_dataset',
        'schedule': 60 * 60, # 1 hr,
    }
    
}