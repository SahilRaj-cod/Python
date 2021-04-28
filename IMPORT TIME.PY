import time 
import datetime

for i in range(10):
    now = datetime.datetime.now()
    date_time = now.strftime("%D/%m/%y %H:%D:%S")
    print(date_time)
    time.sleep(10)