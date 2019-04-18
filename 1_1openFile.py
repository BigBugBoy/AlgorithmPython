# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2019.4.15


def open_File():
    # 提示用户输入文件名，打开文件夹，将内容显示到屏幕上
    fileName = input("Enter file name :")
    fobj = open(fileName,'r')
    for eachLine in fobj:
        print(eachLine)
    fobj.close()

# 文件名需要输入全路径，否则报错，找不到文件
if __name__ == '__main__':
    open_File()