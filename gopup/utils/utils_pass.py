#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : utils_pass.py
# @Desc    : 验证通过工具

import os
import pandas as pd


def set_token(token):
    df = pd.DataFrame([token], columns=['token'])
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, 'gp.csv')
    df.to_csv(fp, index=False)


def get_token():
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, 'gp.csv')
    if os.path.exists(fp):
        df = pd.read_csv(fp)
        return str(df.loc[0]['token'])
    else:
        print('请设置gopup的token凭证码，如果没有请访问http://www.gopup.cn注册申请')
        return None

