import datetime
import time

while True:
    hour, minute, second = datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second
    print(f'{bin(hour)[2:]}-{bin(minute)[2:]}-{bin(second)[2:]}')
    time.sleep(1)
