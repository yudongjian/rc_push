import datetime

date = "2022-08-27 12:13:30"
print(date)
print(type(date))
date2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(date2)
print(type(date2))

date2 = '2022-08-27 12:13:30'

while(date!=date2):
    print('not same')
print('-----')