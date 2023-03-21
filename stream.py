import threading
import queue
from time import sleep

class Stream ():
    def __init__ (self):
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        self.f = None
    
    def run (self):
        while True:
            try:
                x = self.queue.get(timeout=0.3)
                self.f(x)
            except queue.Empty:
                break
        if queue.Empty:
            sleep(0.1)

    def stop (self):
        self.thread.join()
    
    def add (self, x):
        self.queue.put(x)
    
    def forEach(self, f):
        self.f = f

    def apply(self, f):
        newStream = Stream()
        def g(x):
            if (f(x) is True):
                newStream.add(x)
            else:
                y = f(x)
                if (type(y) is int):
                    newStream.add(y)
        self.forEach(g)
        return newStream


    

        
