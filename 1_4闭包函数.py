# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.27


def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                print("g")
                print(i)
                return i*i
            print("f")
            print(i)
            return g
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())