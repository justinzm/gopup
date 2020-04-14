#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 17:51
# @Author  : justin.郑 3907721@qq.com
# @File    : xx.py
# @Desc    :
import pandas._testing as tm
import numpy as np
import pandas as pd
data = {'Item1':pd.DataFrame(np.random.randn(4,3)),
       'Item2':pd.DataFrame(np.random.randn(4,2))}

pn = tm.makePanel(np.random.randn(2, 5, 4))
pass