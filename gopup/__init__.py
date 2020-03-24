"""
GoPup 是基于 Python 的开源金融数据接口库, 目的是实现对金融产品和另类数据从数据采集, 数据清洗到数据下载的工具, 满足金融数据科学家, 数据科学爱好者在数据获取方面的需求.
它的特点是利用 GoPup 获取的是基于可信任数据源发布的原始数据, 广大数据科学家可以利用原始数据进行再加工, 从而得出科学的结论.
"""


"""
谷歌指数
"""
# from gopup.index.index_google import google_index

"""
百度指数
"""
from gopup.index.index_baidu import (
    baidu_search_index,
    baidu_info_index,
    baidu_media_index,
)

"""
微博指数
"""
from gopup.index.index_weibo import weibo_index


"""
百度迁徙地图接口
"""
from gopup.event.area_baidu import migration_area_baidu


"""
新型冠状病毒接口
"""
from gopup.event.covid import (
    covid_163,
    covid_dxy,
    covid_baidu,
    covid_hist_city,
    covid_hist_province,
)

"""
中国宏观数据
"""
from gopup.economic.marco_cn import marco_cmlrd

# from gopup.my_fun import (gopup_test, add_sum)
