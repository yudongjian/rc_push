import datetime, os
from apscheduler.schedulers.background import BackgroundScheduler
from send_app.models import task_info
from django_apscheduler.jobstores import DjangoJobStore

scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Shanghai'})
# 调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")

def runTask(args):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    cmd = 'python ' + args
    # cmd = 'python3 ' + args
    a = os.popen(cmd)
    result = a.readlines()
    send_msg = result[-1].rstrip()

    # TODO cmd 运行 curl

    print(args)


def start_all_task():
    # TODO 开启所有任务，项目启动的时候 run
    for info in task_info.objects.filter(status=1):
        pass



now = datetime.datetime.now()
def create_task(task_id, fun_name, run_date,my_week='0,1,2,3,4,5,6', my_end_date='2100-05-20'):
    """
    :param model: 任务模式
    :param date: 运行时间
    :return:
    """


    print(run_date)
    print(type(run_date))
    my_hour = run_date.split("T")[1].split(":")[0]
    my_minute = run_date.split("T")[1].split(":")[1]
    print(my_hour,my_minute)



    # 特定时间周期性地触发

    scheduler.add_job(runTask,  'cron', id=task_id, day_of_week=my_week, hour=int(my_hour), minute=int(my_minute), jobstore='default', args=[fun_name,])
    # scheduler.add_job(timedTask,  'cron', id=task_id, day_of_week=my_week, hour=21, minute=58, jobstore='default', args=[fun_name])

    scheduler.start()
    print('添加成功')

    # 暂停任务

def del_task(task_id):
    scheduler.remove_job(task_id)
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


