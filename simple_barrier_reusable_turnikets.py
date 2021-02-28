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

    def barrier_nabitie(self):
        self.mutex.lock()
        self.counter = self.counter + 1
        if self.counter == self.N:
            self.counter = 0
            self.turniket_nabitie.signal(self.N)
        self.mutex.unlock()
        self.turniket_nabitie.wait()


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

#instancie pre turnikety s nabitim
simpleBarrier1 = SimpleBarrier(10)
simpleBarrier2 = SimpleBarrier(10)

#instancia pre 2 turnikety
simpleBarrier = SimpleBarrier(10)


def barrier_example(thread_name, barrier):

    while True:
        # ...
        rendezvous(thread_name)
        # ...
        barrier.wait_1()
        ko(thread_name)
        barrier.wait_2()
        # ...


def barrier_example_nabitie(thread_name, barier1, barrier2):

    while True:
        # ...
        rendezvous(thread_name)
        # ...
        barier1.barrier_nabitie()
        ko(thread_name)
        barrier2.barrier_nabitie()
        # ...


threads = list()
for i in range(10):
    # t = Thread(barrier_example, 'Thread %d' % i,simpleBarrier)
    t = Thread(barrier_example_nabitie, 'Thread %d' % i, simpleBarrier1, simpleBarrier2)
    threads.append(t)

for t in threads:
    t.join()