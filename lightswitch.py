from fei.ppds import Mutex


class LightSwitch:
    def __init__(self):
        self.counter = 0
        self.mutex = Mutex()

    def lock(self, sem):
        self.mutex.lock()
        self.counter += 1
        if self.counter == 1:
            sem.wait()
        self.mutex.unlock()

    def unlock(self, sem):
        self.mutex.lock()
        self.counter -= 1
        if self.counter == 0:
            sem.signal()
        self.mutex.unlock()
