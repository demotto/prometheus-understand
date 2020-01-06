from flask import Flask
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import time

v = None
lock = threading.Lock()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'ass hole!'


@app.route('/normal')
def normal():
    lock.acquire()
    global v
    v = 100
    lock.release()
    return str(v)



@app.route('/abnormal')
def abnormal():
    global v
    lock.acquire()
    v = 250
    lock.release()
    return str(v)


def job():
    lock.acquire()
    print(v)
    lock.release()

def start_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(job, "interval", seconds=2)
    scheduler.start()

if __name__ == '__main__':

    t = threading.Thread(target=start_scheduler)
    t.start()

    app.run(
        host='0.0.0.0',
        port=5656,
        threaded=True
    )



