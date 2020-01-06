from prometheus_client import Gauge,start_http_server
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import random


sigma = Gauge('sigma', 'Description of gauge', labelnames=('a1', 'a2'))
sigma.labels("aaaa", "bbb").set(random.random()) #value自己定义,但是一定要为 整数或者浮点数

# sigma.labels("a1", "aaa").inc()
start_http_server(9527)

while True:
    pass
