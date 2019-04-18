# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.9


def insertion_Sort(aArray):
    # 1.插入排序，实现伪代码
    for j in range(1,len(aArray)):
        key = aArray[j]
        i = j - 1
        while (i >0 or i == 0) and aArray[i] > key:
            aArray[i+1] = aArray [i]
            i = i - 1
        aArray[i +1] = key
    print(aArray)


def insertion_Sort_dec(aArray):
    # 2.重写函数insertion-sort，使之按非升序（而不是非降序)排序
    for j in range(1,len(aArray)):
        key = aArray[j]
        i = j - 1
        while (i >0 or i == 0) and aArray[i] < key:
            aArray[i+1] = aArray [i]
            i = i - 1
        aArray[i +1] = key
    print(aArray)


def search_Value(aArray, aValue):
    # 3.线性查找，输入n个数的一个序列A和一个值v，输出i，要求i为v在序列地下表，不存在是为NULL
    for i in range(len(aArray)):
        if aValue == aArray[i]:
            print(i)
            return i
    print("NULL")

# 4.两个n位二进制整数相加的问题，两个整数分别存储在两个n元数组A和B中
# 这两个数的和按照二进制形式存储在一个（n+1）元数组C中。
# TODO 没看懂这个跟插入排序有什么关系

if __name__ == "__main__":
    # 测试列表
    test_Array = [31, 41, 59, 26, 41, 58]

    # 测试1，实现伪代码
    insertion_Sort(test_Array)

    # 测试2，降序
    insertion_Sort_dec(test_Array)

    # 测试3，查找值
    search_Value(test_Array, 26)
