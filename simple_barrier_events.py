from fei.ppds import *
from random import randint
from time import sleep

# vypisovat na monitor budeme pomocou funkcie 'print'
# importovanej z modulu 'ppds'
# to kvoli tomu, aby neboli 'rozbite' vypisy

class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.semaphore_barrier = Semaphore(0)
        self.event_barrier = Event()

    def wait_semaphore(self):
        self.mutex.lock()
        self.counter = self.counter + 1
        if self.counter == self.N:
            self.semaphore_barrier.signal()
        self.mutex.unlock()
        self.semaphore_barrier.wait()
        self.semaphore_barrier.signal()

    def wait_events(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.N:
            self.event_barrier.signal()  # pusti vsetky cakajuce vlakna
        self.mutex.unlock()
        self.event_barrier.wait()


def barrier_example(barrier, thread_id):
    """Predpokladajme, ze nas program vytvara a spusta 5 vlakien,
    ktore vykonavaju nasledovnu funkciu, ktorej argumentom je
    zdielany objekt jednoduchej bariery
    """
    sleep(randint(1, 10) / 10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait_events()
    print("vlakno %d po bariere" % thread_id)


# priklad pouzitia ADT SimpleBarrier
sb = SimpleBarrier(5)

# doplnit kod, v ktorom sa vytvara a spusta 5 vlakien
threads = list()
for i in range(5):
    t = Thread(barrier_example,sb,i)
    threads.append(t)

for t in threads:
    t.join()