from prometheus_client import Gauge,start_http_server
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from flask import Flask
import random

app = Flask(__name__)

sigma = Gauge('sigma', 'Description of gauge')
sigma.set(100.5) #value自己定义,但是一定要为 整数或者浮点数


@app.route('/bad')
def bad():
    sigma.set(-100)
    return 'ass hole!'


@app.route('/good')
def good():
    sigma.set(200)
    return 'ass hole!'

start_http_server(9527)


app.run(
        host='0.0.0.0',
        port=5656,
        threaded=True
)


