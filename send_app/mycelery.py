from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

app = Celery('demo')                                # 创建 Celery 实例
app.config_from_object('celery_app.celeryconfig')   # 通过 Celery 实例加载配置模块

app.conf.update(
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },

    # Executes every Monday morning at 7:30 A.M
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
)
