#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    : 测试及功能展示

import time
import gopup as gp
import pandas as pd


def test():
    print('测试及功能展示: ')

    # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取微博指数')
    # df = gp.weibo_index(word="疫情", time_type="1hour")
    # print(df)

    # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取百度迁徙数据')
    # df = gp.migration_area_baidu()
    # print(df)

    # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取实时电影票房数据')
    # df = gp.realtime_boxoffice()
    # print(df)

    # # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取谷歌事实查证')
    #
    # res_pd = pd.DataFrame()
    # for i in range(0, 500):
    #     print(i)
    #     limit = 200
    #     offset = i * limit
    #     df = gp.google_fact_check(keyword="中国", offset=offset, limit=limit, hl="zh")
    #     if df is None:
    #         break
    #     else:
    #         res_pd = res_pd.append(df, ignore_index=True)
    #     time.sleep(3)
    #
    # fileXls = '中国_zh_谷歌事实查证02.xls'
    # res_pd.to_excel(fileXls, encoding='utf-8')
    #
    # print("完成")


if __name__ == '__main__':
    test()

