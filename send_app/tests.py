import os

cmd = r'python C:\Users\yudj\PycharmProjects\rc_send\send_app\a.py'
a = os.popen(cmd)
result = a.readlines()
print(result)
send_preson=result[-3].rstrip()
send_room=result[-2].rstrip()
send_msg=result[-1].rstrip()
print(send_preson)
print(send_room)
print(send_msg)
