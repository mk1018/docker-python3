import sys
import time
import daemon
import api_test as test

def count_up():
    count = 0
    while True:
        print(count)
        count += 1
        time.sleep(5)

dc = daemon.DaemonContext(stdout=sys.stdout)

with dc:
    count_up()