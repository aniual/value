from multiprocessing import Value, Process
import time
import random


def a(money):
    for i in range(100):
        time.sleep(0.02)
        money.value += random.randint(1, 200)


def b(money):
    for i in range(100):
        time.sleep(0.05)
        money.value -= random.randint(1, 150)


money = Value('i', 2000)
p = Process(target=a, args=(money,))
p1 = Process(target=b, args=(money,))

p.start()
p1.start()

p.join()
p1.join()
print(money.value)
