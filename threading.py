import time
from threading import Thread


def funktion_1():
    while True:
        print("Funktion 1 läuft")
        time.sleep(1)


def funktion_2():
    while True:
        print("Funktion 2 läuft")
        time.sleep(1)


thread_1 = Thread(target=funktion_1)
thread_2 = Thread(target=funktion_2)

thread_1.start()
thread_2.start()
