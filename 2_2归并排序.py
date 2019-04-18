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
    # n = len(left) + len(right)
    # for k in range(n):
    #     if left[i] <= right[j]:
    #         result.append(left[i])
    #         i = i + 1
    #     else:
    #         result.append(right[j])
    #         j = j+1
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    # 如果左分支计数器i，因为需要当下标使用，所以从0开始
    # 判断语句，若未抵达最后，那么后续的都是较大的数，直接接在result结果列表后即可。
    # 因为每次添加一个值到result列表后进行了自增操作：i = i + 1，那么程序执行到这一步时，i和j就不是下标了，而是单边已经添加到result列表的计数 
    if i < len(left): 
        result += left[i:]
    else:
        if j < len(right): 
            result += right[j:]
    return result


def merge_Sort(aList):
    # function info:
    # 归并递归，先将列表进行拆分，构建归并树，直到只剩叶子，然后递归
    if len(aList)<2 : return aList
    else:
        mid  = len(aList)//2    # '//'表示地板除，向下取整，而'/'表示浮点除法
        left, right = None, None
        left = merge_Sort(aList[0:mid])
        # print(left)
        right = merge_Sort(aList[mid:])
        # print(right)
        return merge_Sorting(left, right)


if __name__ == "__main__":
    # 测试列表
    test_list = [2, 3, 45, 234, 5, 8, 4, 55, 0, 7, 1, 9]

    # 测试合并函数
    # print(merge_Sorting(test_list[:5],test_list[5:]))
    
    # 测试归并函数
    print(merge_Sort(test_list))