# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.15


def merge_Sorting(left, right):
    # function info：
    # 合并两个已经按照升序排好序的队列，新队列按照升序排列
    if not left or not right:
        return left or right
    result = []
    i,j = 0,0
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    if i < len(left) -1 : 
        result += left[i:]
    else:
        if j < len(right) - 1 : 
            result += right[j:]
    return result


def merge_Sort(aList):
    # function info:
    # 归并递归，先将列表进行拆分，构建归并树，直到只剩叶子，然后递归
    if len(aList)<2 : return aList
    mid  = len(aList)//2    # '//'表示地板除，向下取整，而'/'表示浮点除法
    left, right = None, None
    if aList[:mid] : left = merge_Sort(aList[:mid])
    if aList[mid:] : right = merge_Sort(aList[mid:])
    return merge_Sorting(left, right)


if __name__ == "__main__":
    # 测试列表
    test_list = [2, 3, 45, 234, 5, 8, 4, 55, 15, 0, 1]

    # 测试合并函数
    # print(merge_Sorting(test_list[:5],test_list[5:]))
    
    # 测试归并函数
    merge_Sort(test_list)
    
    print(test_list)