from fei.ppds import Mutex, Semaphore


class Barrier(object):
    def __init__(self, N):
        self.N = N
        self.counter = 0
        self.mutex = Mutex()
        self.turn1 = Semaphore(0)
        self.turn2 = Semaphore(0)

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.N:
            self.turn1.signal(self.N)
        self.mutex.unlock()
        self.turn1.wait()

        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            self.turn2.signal(self.N)
        self.mutex.unlock()
        self.turn2.wait()