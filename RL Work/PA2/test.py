import threading
import queue
import time

my_queue = queue.Queue()

def storeInQueue(f):
    def wrapper(*args):
        my_queue.put(f(*args))
    return wrapper


@storeInQueue
def nameit(num):
    time.sleep(4-num)
    return num

for i in range(3):
    t = threading.Thread(target=nameit, args=(i,))
    t.start()
    
for i in range(3):
    print(my_queue.get())