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
    # df = gp.weibo_index(word="疫情", time_type="1month")
    # print(df)

    # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取微博指数')
    # df = gp.toutiao_index(keyword="python", start_date="20221016", end_date="20221022", app_name="toutiao")
    # print(df)

    # ----------------------------------------------------------------------
    # print('\n' + '-' * 80 + '\n获取百度迁徙数据')
    # df = gp.migration_area_baidu()
    # print(df)

    cookie = '''BIDUPSID=512FE19892358D21D38C8FC50F5F37F7; PSTM=1660901365; BAIDUID=53AD0CE37FCDB36D9D1B39A93FE374F4:SL=0:NR=10:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22334753876%22%2C%22scope%22%3A1%7D%7D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-218%3A; BA_HECTOR=aga0a42lalak218laha5hmc01hi0at619; BAIDUID_BFESS=53AD0CE37FCDB36D9D1B39A93FE374F4:SL=0:NR=10:FG=1; ZFY=aW7:BiB7855FQiPLSOkRbec2PdNcv3rbOnPH5AYTKCqc:C; BDUSS=ZvNlM1RndBRDQ3bko0S0tEOWktVE02Tnd4b0R0dVZ1fmIwLWpPdjNDOWZ4a2RqSVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF85IGNfOSBjfk; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%224028045868%22%2C%22first_id%22%3A%2218335e0347710fc-0e1fee1e643a0f-26021c51-1395396-18335e034789b9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218335e0347710fc-0e1fee1e643a0f-26021c51-1395396-18335e034789b9%22%7D; delPer=0; H_PS_PSSID=37155_36552_36459_37115_37355_37299_36885_36786_37243_37260_26350_22157; PSINO=7; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1661486036,1661564440,1661647128,1663127080; bdindexid=8nktvuic1kuo5dot5pkgo2q9e0; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04131395300fN1KlH2fo%2FP67W6DdexHNNUP3l99gFTlVBT31fwY0AeZ7JgLby0XOquez%2FgS66QIrBdlgN6%2FfxFJhYMdjaOTybrrHdz8W2BqOgOp0hXRAccayXkHgZIlByUaoaQHDKjhnDBipw083eS8hKObXIQXit1ZiFtP6XNWsK5VMlr5qHkt54hAfKRLAlmF9X7hUKZVmrSxcvI%2F2GrPWfIM9YgEajJYRsNeYN7kZiTscF99vZwMkqUipDarRfkpu0eoNbMD0dTj72fsdkmkmj8Ui6eKu8fPOpc5MwWMIPnmJxuqQJ9AHU%2BtsifCssB2AYpE2Ir4gFAg8rWsqmwl9lTmOCWZrw%3D%3D65473314357981690382511504956550; __cas__rn__=413139530; __cas__st__212=fcd26bfe42726771ecac112f095fc17d1f1584e59a13e60a039fc22b264d79132ee080e381ae1c33427295a9; __cas__id__212=42043514; CPID_212=42043514; CPTK_212=684298546; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1663127094; RT="z=1&dm=baidu.com&si=3efb8415-45d4-44df-ba4c-6af9f09d175e&ss=l812x7mj&sl=2&tt=1fw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab_sr=1.0.1_N2RhZWI0OGUyOWQ1MmUwNzExMTUzYmRiMzllN2UxMDFiZGJlNzExZmVlY2IwNjI0YzllZWQwN2I3Mzc5ZDQ2ODlmOGUzNThiMWFlNzcxMzhlZjc5ODUxNjk3YWI3MDJiN2IzNGI1ZjY2NmQzYTg0MmQyMWYxNWMxMzJhZThjZjdiNDFjYjk2MTIzNTg3YTgxYjg4ZTM3YjY3ZmEyZDE3ZQ==; BDUSS_BFESS=ZvNlM1RndBRDQ3bko0S0tEOWktVE02Tnd4b0R0dVZ1fmIwLWpPdjNDOWZ4a2RqSVFBQUFBJCQAAAAAAAAAAAEAAABU8PMTst24-dauw~cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF85IGNfOSBjfk'''
    index_df = gp.baidu_age_index(word="口罩", cookie=cookie)
    print(index_df)


if __name__ == '__main__':
    test()

