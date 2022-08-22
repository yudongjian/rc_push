from django.test import TestCase

# Create your tests here.

# TODO 思路： 从数据库表中读取数据 

import schedule
import time
import threading

def job():
    print("I'm working... in job1  start")
    time.sleep(15)
    print("I'm working... in job1  end")

def job2():
    print("I'm working... in job2")

def run_threaded(job_func):
     job_thread = threading.Thread(target=job_func)
     job_thread.start()

schedule.every(10).seconds.do(run_threaded,job)
schedule.every(10).seconds.do(run_threaded,job2)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# 每隔十分钟执行一次任务
#
# 每隔一小时执行一次任务
#
# 每天的10:30执行一次任务
#
# 每隔5到10天执行一次任务
#
# 每周一的这个时候执行一次任务
#
# 每周三13:15执行一次任务


while True:
    schedule.run_pending()
    time.sleep(1)