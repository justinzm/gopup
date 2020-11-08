#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 19:42
# @Author  : justin.郑 3907721@qq.com
# @File    : client.py
# @Desc    : 专业版 数据接口

import pandas as pd
import json
from functools import partial
import requests


class DataApi:
    def __init__(self, token, timeout=15):
        """
        API接口TOKEN，用于用户认证
        :param token:
        :param timeout:
        """
        self._token = token
        self._timeout = timeout
        self._http_url = 'http://www.gopup.cn/api/v1'

    def query(self, api_name, fields=None, **kwargs):
        """
        # api_name，接口名称；
        # token，用于识别唯一用户的标识；
        # params，接口参数，如daily接口中start_date和end_date；
        # fields，字段列表，用于接口获取指定的字段，以逗号分隔，如"open,high,low,close"；

        :param api_name:
        :param fields:
        :param kwargs:
        :return:
        """
        req_params = {
            'api_name': api_name,
            'token': self._token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self._http_url, json=req_params, timeout=self._timeout, headers={'Connection': 'close'})
        if res is not None:
            result = json.loads(res.text)
            if result['error_code'] != 200:
                raise Exception(result['msg'])
            data = result['data']
            columns = data['fields']
            items = data['items']
            return pd.DataFrame(items, columns=columns)
        else:
            return pd.DataFrame()

    def __getattr__(self, name):
        return partial(self.query, name)
