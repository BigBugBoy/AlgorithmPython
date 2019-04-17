# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.12


def merge(A, p, q, r):
    # 归并排序，“合并”的伪代码
    n1 = q - p + 1
    n2 = r - q
    # let L[1,n1 + 1] and R[1, n2 + 1] be new arrays
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n2):
        R[j] = A[q + j]
    L[n1 + 1] = upKey
    R[n2 + 1] = upKey
    i = 1
    j = 1
    for k in range(r,p): # p to r
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def Merge_sort(A,p,r):
    if p < r:
        q = [(p + r) / 2] # 向下取整
        Merge_sort(A, p, q)
        Merge_sort(A, q+1, r)
        merge(A, p, q, r)

if __name__ == "__main__":
    A = [2,5,6,7,9,3,1,4]
    merge(A,2,4,5)
    print(A)

