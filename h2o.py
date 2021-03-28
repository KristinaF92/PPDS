from time import sleep
from random import choice, randint

from fei.ppds import Mutex, Semaphore, print, Thread
from barrier import Barrier



class Shared(object):
    def __init__(self):
        self.oxygen = 0
        self.hydrogen = 0
        self.mutex = Mutex()
        self.oxyQueue = Semaphore(0)
        self.hydroQueue = Semaphore(0)
        self.barrier = Barrier(3)


def bond(name):
    print(f"bond {name}")


def oxygen(shared):
    shared.mutex.lock()
    shared.oxygen += 1
    '''nie je dost vodikov nemoze vytvorit molekulu tak odomnkne mutex a caka'''
    if shared.hydrogen < 2:
        shared.mutex.unlock()
    else:
        shared.oxygen -= 1
        shared.hydrogen -= 2
        shared.oxyQueue.signal(1)
        shared.hydroQueue.signal(2)

    shared.oxyQueue.wait()
    bond(oxygen.name)
    shared.barrier.wait()
    '''mutex musi byt tu kvoli 2 vodikom'''
    shared.mutex.unlock()


def hydrogen(shared):
    shared.mutex.lock()
    shared.hydrogen += 1
    '''nie je dost O a H nemoze vytvorit molekulu tak odomnkne mutex a caka'''
    if shared.oxygen < 1 or shared.hydrogen < 2:
        shared.mutex.unlock()
    else:
        shared.oxygen -= 1
        shared.hydrogen -= 2
        shared.oxyQueue.signal(1)
        '''vodiky cakaju na kyslik'''
        shared.hydroQueue.signal(2)

    shared.hydroQueue.wait()
    bond(hydrogen.name)
    shared.barrier.wait()



def test():
    oxygen.name = 'O'
    hydrogen.name = 'H'
    shared = Shared()

    while True:
        Thread(choice([oxygen, hydrogen]), shared)
        sleep(randint(0, 3) / 100)


if __name__ == "__main__":
    test()

