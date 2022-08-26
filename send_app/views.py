from django.shortcuts import render
from send_app import models
from send_app import my_schedule
# Create your views here.


# TODO 这里 run 调度方法

def index(request):
    data = models.task_info.objects.all()
    return render(request, 'index.html', {'data': data,"data2": [1,2,3,4,5,6]})


def add_task(request):
    return render(request, 'add_task.html')

def submit_task(request):
    try:
        print(request.POST.get("run_date"))
        models.task_info.objects.create(
            ip='123',
            task_name = request.POST.get("task_name"),
            run_date = request.POST.get("run_date"),
            run_code = request.POST.get("run_code"),
            send_person = request.POST.get("send_person"),
            send_room = request.POST.get("send_room")
        )
    except Exception as e:
        print(e)
        return render(request, 'submit_task.html', {"meg": e})
    return render(request, 'submit_task.html', {'meg': "上传成功"})