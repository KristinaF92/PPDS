# nacitame modul 'ppds', v ktorom mame definovanu triedu 'Thread'
from fei.ppds import *
import time

def test(shared,tmp):
    time.sleep(1) #vytvareme dojem zloziteho vypoctu, tj realne sa necaka na vypocet v mutex scope a tym dosahujeme paralelizmus vypoctu(zdanie)
    shared.elms[tmp] += 1 #pristup do shared pola pomocou lokalnej premmnej threadu (safe)
    print(f'hodnota: {shared.elms[tmp]} index: {tmp}')
# vytvor a spusti vlakna
# pockaj na ich dokoncenie
# ...

# definicia triedy 'Shared'
class Shared():
    def __init__(self, e):
        self.counter = 0
        self.end = e
        self.elms = [0]*e
        self.mutex = Mutex()
    pass


# definicia funkcie vlakna
def fnc_test(shared):
    while True:

        shared.mutex.lock() #treba chranit integritu pri zapisovani
        print('som locknuty')
        if shared.counter > len(shared.elms) - 1:
            shared.mutex.unlock()
            print('unlocknem sa')
            break

        if shared.elms[shared.counter] > 0:
            print(f'hodnota: {shared.elms[shared.counter]} index: {shared.counter}')
        tmp = shared.counter #ulozenie do lokalnej premennej threadu, zaistenie integrity
        shared.counter += 1
        shared.mutex.unlock() # koniec kritickej oblasti, uz netreba chranit zapis
        test(shared, tmp) #teda aj po unlocku mozeme bezpecne pristupit na index pola kedze sme zaistili hodnotu v scope mutexu

    return


# vytvorenie instancie triedy 'Shared'
shared = Shared(100)

# do 't1' ulozime identifikator pracovneho vlakna
# prvy argument pri vytvarani objektu typu 'Thread' je funkcia, ktoru ma
# vlakno vykonavat
# dalsie argumenty sa predaju funkcii, ktora je definovana prvym argumentom
t1 = Thread(fnc_test, shared)
t2 = Thread(fnc_test, shared)
t3 = Thread(fnc_test, shared)
t4 = Thread(fnc_test, shared)
t5 = Thread(fnc_test, shared)
t6 = Thread(fnc_test, shared)
t7 = Thread(fnc_test, shared)
t8 = Thread(fnc_test, shared)
t9 = Thread(fnc_test, shared)
t10 = Thread(fnc_test, shared)
# pockame na dokoncenie behu vlakna
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()