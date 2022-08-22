from django.db import models

# Create your models here.
class task_info(models.Model):
    ip = models.CharField(max_length=32)
    task_name = models.CharField(max_length=32, default='')
    run_date = models.CharField(max_length=32)
    run_code = models.CharField(max_length=32)
    run_frequency = models.CharField(max_length=32)
    send_person = models.CharField(max_length=32)
    send_room = models.CharField(max_length=32)
    last_result = models.CharField(max_length=32, default='')
    last_run_time = models.CharField(max_length=32, default='')


