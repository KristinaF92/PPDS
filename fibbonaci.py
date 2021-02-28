# nacitame modul 'ppds', v ktorom mame definovanu triedu 'Thread'
from fei.ppds import *
from fei.ppds import Mutex, Thread, Semaphore

import time


class Shared():
    def __init__(self,n):
        self.counter = 0
        self.N = n
        self.mutex = Mutex()
        self.fib_seq = [0, 1] + [0] * n
        self.threads = [0] * (n + 2)
        for i in range(n + 2):
            self.threads[i] = Semaphore(0)
        self.threads[0].signal(1)
        self.threads[1].signal(2)

    # naive
    def fibonacci(self,i):
        i += 2
        self.threads[i - 1].wait()
        self.threads[i - 2].wait()
        self.fib_seq[i] = self.fib_seq[i - 1] + self.fib_seq[i - 2]
        self.threads[i].signal(2)


def compute_fibonnaci(thread_id, shared):
    shared.fibonacci(thread_id)


# vytvorenie instancie triedy 'Shared'

shared = Shared(20)

threads = list()

for i in range(shared.N):
    t = Thread(compute_fibonnaci, i , shared)
    threads.append(t)
print(shared.fib_seq)
for t in threads:
    t.join()