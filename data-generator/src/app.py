from flask import Flask
import socket
import math
import time

app = Flask(__name__)


@app.route("/metrics")
def metrics():
    print(math.pi)
    print(math.sin(math.pi/2.0))
    T = 5.0
    t = time.time()
    v = math.sin(2*math.pi/T*t)

    T1 = 2.0
    v2 = math.sin(2*math.pi/T1*t)
    return """
bb_no_bb {v}
xbb {v2}
    """.format(
        v=v,
        v2=v2
    )


@app.route('/')
def hello_world():
    return 'ass hole!'


if __name__ == '__main__':
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    print(myname)
    print(myaddr)
    app.run(
        host='0.0.0.0',
        port=5656,
        debug=True
    )
