from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from send_app.models import task_info

scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
scheduler.add_jobstore(DjangoJobStore(), 'default')


def get_args():
    for i in task_info.objects.all():
        print(i.task_name)

@register_job(scheduler, 'interval',id='123', )
#TODO 读数据库 然后run
# 任务在2022-04-14 18:50:00 仅执行一次
@register_job(scheduler, "date", id="timed_task1", run_date="2022-08-26 11:16:30" )
def timed_task1():
    # 编写你的定时逻辑
    print('=====this is a schedule task ')
    print('hhhhh')


scheduler.start()