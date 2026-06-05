import threading
import time 

class MyThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print('Starting ' + self.name + '\n')
        with threadLock:
            print_time(self.name, self.count, 5)

        print('Exiting ' + self.name + '\n')

def print_time(threadName, delay, count):
    while count:
        time.sleep(delay)
        print('%s %s %s' % (threadName, time.ctime(time.time()), count) + '\n')
        count -= 1

threadLock = threading.Lock()

# create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 1.5)

# start new threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exiting Main Thread")
 