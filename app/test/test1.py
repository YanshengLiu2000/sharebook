import threading
import time


def worker():
    print('i am thread')
    t=threading.current_thread()
    time.sleep(10)
    print('This is worker: ',t.getName())



new_t=threading.Thread(target=worker, name='zhazha')
new_t.start()
t=threading.current_thread()
print('Main:',t.getName())
"""
    
"""