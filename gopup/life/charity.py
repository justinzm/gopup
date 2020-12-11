#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 0010
# @Author  : justin.郑 3907721@qq.com
# @File    : charity.py
# @Desc    : 慈善中国

import pandas as pd
import requests
from tqdm import tqdm
from pyquery import PyQuery as pq


def _get_page_num_charity_organization():
    """
    慈善中国-慈善组织查询-总页数
    :return: 总页数
    """
    url = "http://cishan.chinanpo.gov.cn/biz/ma/csmh/a/csmhaDoSort.html"
    payload_params = {
        "aaee0102_03": "",
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    }
    payload_data = {"pageNo": "1"}
    r = requests.post(url, params=payload_params, data=payload_data)
    pages = r.text[r.text.find("第1页/共") + 5: r.text.rfind("页</font>")]
    return int(pages)


def charity_organization():
    """
    慈善中国-慈善组织查询
    http://cishan.chinanpo.gov.cn/biz/ma/csmh/a/csmhaindex.html
    :return: 慈善中国-慈善组织查询
    :rtype: pandas.DataFrame
    """
    page_num = _get_page_num_charity_organization()
    url = "http://cishan.chinanpo.gov.cn/biz/ma/csmh/a/csmhaDoSort.html"
    params = {
        "field": "aaex0131",
        "sort": "desc",
        "flag": "0",
    }
    outer_df = pd.DataFrame()
    for page in tqdm(range(1, page_num+1)):
        # page = 1
        params["pageNo"] = str(page)

        r = requests.post(url, params=params)
        inner_df = pd.read_html(r.text)[0]
        outer_df = outer_df.append(inner_df, ignore_index=True)
    return outer_df


if __name__ == "__main__":
    tmp = charity_organization()
    print(tmp)

