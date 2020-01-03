from prometheus_client import Gauge,start_http_server
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import random

sigma = Gauge('sigma', 'Description of gauge')
sigma.set(random.random()) #value自己定义,但是一定要为 整数或者浮点数

start_http_server(9527)


# 输出时间
def job():
    sigma.set(random.random())

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, "interval", seconds=2)
scheduler.start()


