import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from send_app.models import task_info


def start_all_task():
    # TODO 开启所有任务，项目启动的时候 run
    for info in task_info.objects.all():
        pass


def timedTask(args):
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    print('hello word!!!')
    print(args)
now = datetime.datetime.now()
def create_task(task_id, fun_name, run_date,my_week='0,1,2,3,4,5,6', my_end_date='2100-05-20'):
    """

    :param model: 任务模式
    :param date: 运行时间
    :return:
    """

    scheduler = BackgroundScheduler({
        'apscheduler.jobstores.default': {
            'type': 'sqlalchemy',
            'url': 'mysql+pymysql://root:123456@127.0.0.1:3306/app33?charset=utf8',
            'tablename': 'django_apscheduler_djangojob'
        },
        'apscheduler.executors.default': {
            'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
            'max_workers': '20'
        },
        'apscheduler.executors.processpool': {
            'type': 'processpool',
            'max_workers': '10'
        },
        'apscheduler.job_defaults.coalesce': 'false',
        'apscheduler.job_defaults.max_instances': '10',
        'apscheduler.timezone': 'Asia/Shanghai',
    })

    print(run_date)
    print(type(run_date))
    my_hour = run_date.split("T")[1].split(":")[0]
    my_minute = run_date.split("T")[1].split(":")[1]
    print(my_hour,my_minute)



    # 特定时间周期性地触发

    scheduler.add_job(timedTask,  'cron', id=task_id, day_of_week=my_week, hour=int(my_hour), minute=int(my_minute), jobstore='default', args=[fun_name,])
    # scheduler.add_job(timedTask,  'cron', id=task_id, day_of_week=my_week, hour=21, minute=58, jobstore='default', args=[fun_name])

    scheduler.start()
    print('添加成功')

    # 暂停任务

# 删除任务
# scheduler.remove_job(job_name)
# 暂停任务
# scheduler.pause_job(job_name)
# 开启任务
# scheduler.resume_job(job_name)
# 获取所有任务
# scheduler.get_jobs()
# 修改任务
# scheduler.modify_job(job_name)
# 注：修改任务只能修改参数，如果要修改执行时间的话，有3种方法
# 第一就把任务删了重新创建，
# 第二直接操作数据库，
# 第三用到下面重设任务。




def stop_task(task_id):

    scheduler.pause_job(task_id)

