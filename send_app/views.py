from django.shortcuts import render
from send_app import models
from django.http import HttpResponse,HttpResponseRedirect
from send_app import my_schedule
import traceback
import time
# TODO 这里 run 调度方法

def index(request):
    data = models.task_info.objects.filter(status__gt=-1)
    return render(request, 'index.html', {'data': data,"data2": [1,2,3,4,5,6]})


def add_task(request):
    return render(request, 'add_task.html')

def submit_task(request):

    print(request.POST.get("run_date"))

    post_run_code = request.POST.get("run_code")
    post_run_date = request.POST.get("run_date")
    info = models.task_info.objects.create(
        ip='123',
        task_name = request.POST.get("task_name"),
        run_date = post_run_date,
        run_code = post_run_code,
        send_person = request.POST.get("send_person"),
        send_room = request.POST.get("send_room"),
        status = 1
    )
    print(info.id)
    print(post_run_code)

    my_schedule.create_task(task_id=str(info.id), fun_name=post_run_code, my_week='0,1,2,3,4',run_date = request.POST.get("run_date"))


    return render(request, 'submit_task.html', {'meg': "上传成功"})

def switch_task(request):
    # 关闭调度器内的任务 即可
    task_id = request.GET.get("task_id")
    task_status = request.GET.get("status")
    if task_status == 1:
        my_schedule.del_task(task_id=str(task_id))
        models.task_info.objects.filter(id=task_id).update(status=0)
        return HttpResponseRedirect('/')

    else:
        models.task_info.objects.
        my_schedule.create_task(task_id=str(task_id))
        my_schedule.create_task(task_id=str(info.id), fun_name=post_run_code, my_week='0,1,2,3,4',
                                run_date=request.POST.get("run_date"))

        models.task_info.objects.filter(id=task_id).update(status=0)
        return HttpResponseRedirect('/')

def del_task(request):
    """
    先把task_info 表中 任务状态设置为 0 ，即失效数据
    然后在关闭 调度器内的任务
    :param request:
    :return:
    """
    task_id = request.GET.get("task_id")
    models.task_info.objects.filter(id=task_id).update(status=-1)
    return HttpResponseRedirect('/')




