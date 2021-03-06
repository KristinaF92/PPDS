from fei.ppds import Thread, Semaphore
from time import sleep


class Shared:
    def __init__(self):
        self.room_empty = Semaphore(1)

    def read(self, thread_id):
        print(f'{thread_id} reading')
        sleep(0.1)

    def write(self,thread_id):
        print(f'{thread_id} writing')
        sleep(0.2)

    def reader_thread(self, thread_id):
        self.read(thread_id)

    def writer_thread(self, thread_id):
        self.write(thread_id)


shared = Shared()
threads = []

for i in range(10):
    t = Thread(shared.writer_thread, f"Writer {i}")
    threads.append(t)


for i in range(10):
    t = Thread(shared.reader_thread, f"Reader {i}")
    threads.append(t)

for t in threads:
    t.join()