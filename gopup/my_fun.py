#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : my_fun.py
# @Desc    : 
 

def gopup_test():
    return "测试成功"


def add_sum(a):
    '''
    计算从1+到a
    :param a:
    :return:
    '''
    res = False
    if type(a) == int:
        sum = 0
        for i in range(a + 1):  # 实际遍历到n
            sum += i
        res = True
    else:
        sum = '{0}不是整型，无法计算'.format(a)
    return res, sum


if __name__ == "__main__":
    tmp = add_sum(12)
    print(tmp)

