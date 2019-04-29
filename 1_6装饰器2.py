# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.29


import time
from functools import reduce

def performance(unit):
    def fn(f):
        #@functools.wraps(f)
        # 赋值原函数f的属性到新的函数
        def perf(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = t2 - t1
            if unit == 'ms':
                t = t*1000
            print('call ' + f.__name__ + '()  in ' + str(t))
            return r
        return perf
    return fn

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))