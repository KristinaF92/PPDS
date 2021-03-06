from fei.ppds import Thread, Semaphore, Mutex, print
from time import sleep
from random import randint
from lightswitch import LightSwitch


class Shared:
    def __init__(self):
        self.mutex = Mutex()
        self.read_LS = LightSwitch()
        """spociatku mame otvorenu miestnost"""
        self.room_empty = Semaphore(1)
        """pridanie silneho semaforu (turniketu) fifo fronta pre citatelov"""
        self.turn = Semaphore(1, 'fifo')

    def read(self, thread_id):
        print(f'{thread_id} reading')
        sleep(0.3 + randint(0, 4) / 10)

    def write(self,thread_id):
        print(f'{thread_id} writing')
        sleep(0.3 + randint(0, 4) / 10)

    def reader_thread(self, thread_id):
        while True:
            sleep(randint(0, 10) / 10)
            """citatelia musia chodit za sebou"""
            self.turn.wait()
            """preto dalsi citatel musi odomknut turniket tomu za sebou"""
            self.turn.signal()
            self.read_LS.lock(self.room_empty)
            self.read(thread_id)
            self.read_LS.unlock(self.room_empty)
            print(f'{thread_id} leaving')

    def writer_thread(self, thread_id):
        while True:
            """zapisovatelia si uzamknu turniket aby sa predislo vyhladoveniu"""
            self.turn.wait()
            self.room_empty.wait()
            self.write(thread_id)
            self.room_empty.signal()
            self.turn.signal()
            """
            turniket sa odomyka az po opusteni miestnosti, 
            v tomto momente je miestnost prazdna,
            citatel moze prejst turniketom
            """
            print(f'{thread_id} leaving')


shared = Shared()
threads = []

for i in range(3):
    t = Thread(shared.writer_thread, f"Writer {i}")
    threads.append(t)


for i in range(5):
    t = Thread(shared.reader_thread, f"Reader {i}")
    threads.append(t)

for t in threads:
    t.join()