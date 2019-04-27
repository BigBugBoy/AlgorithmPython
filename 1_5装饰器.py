# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.27


import time
from functools import reduce

def performance(f):
    def fn(x):
        print('call ' + f.__name__ + '() ' + str(time.time()))
        return f(x)
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))