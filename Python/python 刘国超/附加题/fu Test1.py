# -*- coding: utf-8 -*-
#  @Time    : 2020/10/29 7:59
#  @Author  : Ben
#  @File    : Test2.py
"""
在数学上有一个著名的斐波那契数列，它的规律为：1,1,2,3,5,8,13,21……，
请编程输出其前20个数字，并输出前20项的和。
"""


def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == '__main__':
    num = 0
    for i in range(1, 21):
        num += Fibonacci(i)
        print(Fibonacci(i))
    print("前二十项的和："+str(num))

