from fei.ppds import *
from random import randint
from time import sleep

class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.turniket_nabitie = Semaphore(0)
        self.turniket1 = Semaphore(0)
        self.turniket2 = Semaphore(1)

    def wait_1(self):
        self.mutex.lock()
        self.counter = self.counter + 1
        if self.counter == self.N:
            self.turniket2.wait()
            self.turniket1.signal()
        self.mutex.unlock()
        self.turniket1.wait()
        self.turniket1.signal()

    def wait_2(self):
        self.mutex.lock()
        self.counter = self.counter - 1
        if self.counter == 0:
            self.turniket1.wait()
            self.turniket2.signal()
        self.mutex.unlock()
        self.turniket2.wait()
        self.turniket2.signal()


def rendezvous(thread_name):
    sleep(randint(1,10)/10)
    print('rendezvous: %s' % thread_name)

def ko(thread_name):
    print('ko: %s' % thread_name)
    sleep(randint(1,10)/10)

"""
Kazde vlakno vykonava kod funkcie 'barrier'.
Doplnte synchronizaciu tak, aby sa vsetky vlakna pockali
nielen pred vykonanim funkcie 'ko', ale aj
*vzdy* pred zacatim vykonavania funkcie 'rendezvous'.
"""

simpleBarrier = SimpleBarrier(10)



def barrier_example(thread_name,barrier):

    while True:
        # ...
        rendezvous(thread_name)
        # ...
        barrier.wait_1()
        ko(thread_name)
        barrier.wait_2()
        # ...


threads = list()
for i in range(10):
    t = Thread(barrier_example, 'Thread %d' % i,simpleBarrier)
    threads.append(t)

for t in threads:
    t.join()