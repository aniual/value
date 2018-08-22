from multiprocessing import Process, Array
import time


def fun(s):

    for i in s:
        print(i)
        s[0] = 10


# 第一种用法
# s = Array('i', [1, 2, 3, 4, 5])
# 第二种用法
s = Array('i', 6)

p = Process(target=fun, args=(s,))
p.start()
p.join()

for i in s:
    print(i)
