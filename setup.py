#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 0020
# @Author  : justin.郑 3907721@qq.com
# @File    : setup.py
# @Desc    :

from setuptools import find_packages, setup
import os

URL = 'https://github.com/justinzm/gopup'
NAME = 'gopup'
VERSION = '0.1.6'
DESCRIPTION = 'GoPUP database'
if os.path.exists('README.md'):
    with open('README.md', encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
else:
    LONG_DESCRIPTION = DESCRIPTION
AUTHOR = 'Justin ZM'
AUTHOR_EMAIL = '3907721@qq.com'
LICENSE = 'MIT'
PLATFORMS = [
    'all',
]
REQUIRES = [
    'requests',
    'pandas',
    'demjson',
    'jsonpath',
    'bs4',
    'Pillow',
    'matplotlib'
]
# CONSOLE_SCRIPT = 'my-cmd=my_pkg.my_cmd:main'
# # 如果想在 pip install 之后自动生成一个可执行命令，就靠它了:
# # <command>=<package_name>.<python_file_name>:<python_function>
# # 值得注意的是：
# # python_file_name 是不能用"-"的，需要用"_"，但 command 可以用"-"
# # my_cmd.py 也很简单，正常写即可，方法名也不一定是 main

# 需要的信息就在 setup() 中加上，不需要的可以不加
setup(
    name=NAME,
    version=VERSION,
    description=(
        DESCRIPTION
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(),
    platforms=PLATFORMS,
    url=URL,
    install_requires=REQUIRES,
    # entry_points={
    #     'console_scripts': [CONSOLE_SCRIPT],
    # }
)