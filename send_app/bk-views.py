# from django.shortcuts import render
# from send_app import models
# from send_app import my_schedule
# # Create your views here.
# from send_app import my_schedule
# import traceback
# import time
# # TODO 这里 run 调度方法
#
# def index(request):
#     data = models.task_info.objects.all()
#     return render(request, 'index.html', {'data': data,"data2": [1,2,3,4,5,6]})
#
#
# def add_task(request):
#     return render(request, 'add_task.html')
#
# def submit_task(request):
#
#     print(request.POST.get("run_date"))
#
#     post_run_code = request.POST.get("run_code")
#     post_run_date = request.POST.get("run_date")
#     info = models.task_info.objects.create(
#         ip='123',
#         task_name = request.POST.get("task_name"),
#         run_date = post_run_date,
#         run_code = post_run_code,
#         send_person = request.POST.get("send_person"),
#         send_room = request.POST.get("send_room"),
#         status = 1
#     )
#     print(info.id)
#     print(post_run_code)
#
#     my_schedule.create_task(task_id=str(info.id), fun_name=post_run_code, my_week='0,1,2,3,4',run_date = request.POST.get("run_date"))
#
#
#     return render(request, 'submit_task.html', {'meg': "上传成功"})
#
# def del_task(request):
#     # TODO 删除任务  前端调用js  把id传到url，返回响应值即可
#     pass
#
# def close_task(request):
#     # TODO 暂停任务  前端调用js  把id传到url，返回响应值即可
#     pass


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

print('django-apscheduler')

def job2(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


def job3(name):
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))


# 实例化调度器
scheduler = BackgroundScheduler(timezone='Asia/Shanghai') # 这个地方要加上时间，不然他有时间的警告

# 调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")


# 添加任务1
# 每隔5s执行这个任务，这个就是装饰器的玩法
# @register_job(scheduler, "interval", seconds=5, args=['老K'], id='job1', replace_existing=True)

def job1(name):
    # 具体要执行的代码
    print('{} 任务运行成功！{}'.format(name, time.strftime("%Y-%m-%d %H:%M:%S")))

# 下面这就是add_job的方式 interval
scheduler.add_job(job1, "interval", seconds=10, args=['老Y'], id="12345678", replace_existing=True)

# 下面这就是add_job的方式 crontab  16点 38分  40分执行
# scheduler.add_job(job3, 'cron', hour='16', minute='38,40', args=['鬼人'], id='job3', replace_existing=True)

"""
20220408更新 
id可以不加,如果不加ID是这个应用view下的函数名字

replace_existing=True 这个东西不加的话，他会提示ID冲突了,我查了好多文章，把这答案找出来了 。
"""
# 监控任务
# register_events(scheduler) # 这个event 这个会有已经被废弃的用法删除线，我不知道这个删除了 ，还会不会好用
# 调度器开始运行
scheduler.start()


def index(request):
    return HttpResponse('ok')
