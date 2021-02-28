from fei.ppds import Semaphore, Mutex, print, Thread
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
        self.barrier = Semaphore(0)

    def wait(self):
        self.mutex.lock()
        self.counter = self.counter + 1
        if self.counter == self.N:
            self.barrier.signal()
        self.mutex.unlock()
        self.barrier.wait()
        self.barrier.signal()


def barrier_example(barrier, thread_id):
    """Predpokladajme, ze nas program vytvara a spusta 5 vlakien,
    ktore vykonavaju nasledovnu funkciu, ktorej argumentom je
    zdielany objekt jednoduchej bariery
    """
    sleep(randint(1, 10) / 10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait()
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