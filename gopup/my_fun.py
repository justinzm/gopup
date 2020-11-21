#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : my_fun.py
# @Desc    : 

import pandas as pd

def gopup_test():
    result = [1,23,4,5,66,78,9,0,22,33]
    res = pd.DataFrame(
        [pd.date_range(start="2020-11-01", end="2020-11-10"), result],
        index=["date", "999"],
    ).T
    return res


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
    tmp = gopup_test()
    print(tmp)

