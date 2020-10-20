#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : pro_data.py
# @Desc    :

from gopup.pro import client
from gopup.utils import utils_pass


def pro_api(token='', timeout=30):
    """
    初始化pro API,
    第一次可以通过gp.set_token('your token')来记录自己的token凭证，
    临时token可以通过本参数传入
    """
    if token == '' or token is None:
        token = utils_pass.get_token()
    if token is not None and token != '':
        pro = client.DataApi(token=token, timeout=timeout)
        return pro
    else:
        raise Exception('api init error.')


