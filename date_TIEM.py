import datetime
import time

print(datetime.datetime.now())
x = int(input('enter the time you would like to start heating. EG. yyyy,m,d,h,m'))
target_time = datetime.datetime(x)

while datetime.datetime.now() < target_time:
    time.sleep(10)
print('working')