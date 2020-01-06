import time
import threading

def f0():
    while True:
        print("f0")
        time.sleep(2)

t = threading.Thread(target=f0)
t.start()
print("end")
