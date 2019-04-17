# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.6

import timeit

li1 = [1, 2]
li2 = [23, 5]

def test1():
    li = []
    for i in range(10000):
        # li += [i] 类似extend,尽量不用 +
        li = li + [i]
    # li = li1 + li2

def test2():
    li = [i for i in range(10000)]

def test3():
    li = list(range(10000))

def test4():
    li = []
    for i in range(10000):
        li.append(i)

def test5():
    li=[]
    for i in range(10000):
        li.extend([i])
    # 空间有消耗

def test6():
    li = []
    for i in range(10000):
        li.insert(0,i)

# 构造测算器
timer1 = timeit.Timer("test1()","from __main__ import test1")
print("加法构造列表test1: ", timer1.timeit(1000))

timer2 = timeit.Timer("test2()","from __main__ import test2")
print("列表生成器test2: ", timer2.timeit(1000))

timer3 = timeit.Timer("test3()","from __main__ import test3")
print("利用list转换test3: ", timer3.timeit(1000))

timer4 = timeit.Timer("test4()","from __main__ import test4")
print("append构造列表test4: ", timer4.timeit(1000))

timer5 = timeit.Timer("test5()","from __main__ import test5")
print("尾部添加列表test5: ", timer5.timeit(1000))

timer6 = timeit.Timer("test6()","from __main__ import test6")
print("头部添加列表test6: ", timer6.timeit(1000))

