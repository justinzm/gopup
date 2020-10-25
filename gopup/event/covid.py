#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 0021
# @Author  : justin.郑 3907721@qq.com
# @File    : covid.py
# @Desc    : 获取疫情数据
 
import json
import time
import demjson
import jsonpath
import requests
import pandas as pd
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup


def covid_163(indicator="实时"):
    """
    网易-新冠状病毒
    https://news.163.com/special/epidemic/?spssid=93326430940df93a37229666dfbc4b96&spsw=4&spss=other&#map_block
    https://news.163.com/special/epidemic/?spssid=93326430940df93a37229666dfbc4b96&spsw=4&spss=other&
    :return: 返回指定 indicator 的数据
    :rtype: pandas.DataFrame
    """
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    }
    payload = {
        "t": int(time.time() * 1000),
    }
    r = requests.get(url, params=payload, headers=headers)
    data_json = r.json()
    # data info
    url = "https://news.163.com/special/epidemic/"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    data_info_df = pd.DataFrame(
        [
            item.text.strip().split(".")[1]
            for item in soup.find("div", attrs={"class": "data_tip_pop_text"}).find_all(
                "p"
            )
        ]
    )
    data_info_df.columns = ["info"]

    # 中国历史时点数据
    hist_today_df = pd.DataFrame(
        [item["today"] for item in data_json["data"]["chinaDayList"]],
        index=[item["date"] for item in data_json["data"]["chinaDayList"]],
    )

    # 中国历史累计数据
    hist_total_df = pd.DataFrame(
        [item["total"] for item in data_json["data"]["chinaDayList"]],
        index=[item["date"] for item in data_json["data"]["chinaDayList"]],
    )

    # 中国实时数据
    current_df = pd.DataFrame.from_dict(data_json["data"]["chinaTotal"])

    # 世界历史时点数据
    outside_today_df = pd.DataFrame(
        [item["today"] for item in data_json["data"]["areaTree"]],
        index=[item["name"] for item in data_json["data"]["areaTree"]],
    )

    # 世界历史累计数据
    outside_total_df = pd.DataFrame(
        [item["total"] for item in data_json["data"]["areaTree"]],
        index=[item["name"] for item in data_json["data"]["areaTree"]],
    )

    # 全球所有国家及地区时点数据
    all_world_today_df = pd.DataFrame(
        jsonpath.jsonpath(data_json["data"]["areaTree"], "$..today"),
        index=jsonpath.jsonpath(data_json["data"]["areaTree"], "$..name"),
    )

    # 全球所有国家及地区累计数据
    all_world_total_df = pd.DataFrame(
        jsonpath.jsonpath(data_json["data"]["areaTree"], "$..total"),
        index=jsonpath.jsonpath(data_json["data"]["areaTree"], "$..name"),
    )

    # 中国各地区时点数据
    area_total_df = pd.DataFrame(
        [item["total"] for item in data_json["data"]["areaTree"][0]["children"]],
        index=[item["name"] for item in data_json["data"]["areaTree"][0]["children"]],
    )

    # 中国各地区累计数据
    area_today_df = pd.DataFrame(
        [item["today"] for item in data_json["data"]["areaTree"][0]["children"]],
        index=[item["name"] for item in data_json["data"]["areaTree"][0]["children"]],
    )

    # 疫情学术进展
    url_article = "https://vip.open.163.com/api/cms/topic/list"
    payload_article = {
        "topicid": "00019NGQ",
        "listnum": "1000",
        "liststart": "0",
        "pointstart": "0",
        "pointend": "255",
        "useproperty": "true",
    }
    r_article = requests.get(url_article, params=payload_article)
    article_df = pd.DataFrame(r_article.json()["data"]).iloc[:, 1:]

    # 咨询
    url_info = "https://ent.163.com/special/00035080/virus_report_data.js"
    payload_info = {
        "_": int(time.time() * 1000),
        "callback": "callback",
    }
    r_info = requests.get(url_info, params=payload_info, headers=headers)
    data_info_text = r_info.text
    data_info_json = demjson.decode(data_info_text.strip(" callback(")[:-1])

    if indicator == "数据说明":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return data_info_df

    if indicator == "中国实时数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return current_df

    if indicator == "中国历史时点数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return hist_today_df

    if indicator == "中国历史累计数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return hist_total_df

    if indicator == "世界历史时点数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return outside_today_df

    if indicator == "世界历史累计数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return outside_total_df

    if indicator == "全球所有国家及地区时点数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return all_world_today_df

    elif indicator == "全球所有国家及地区累计数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return all_world_total_df

    elif indicator == "中国各地区时点数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return area_today_df

    elif indicator == "中国各地区累计数据":
        print(f"数据更新时间: {data_json['data']['lastUpdateTime']}")
        return area_total_df

    elif indicator == "疫情学术进展":
        return article_df

    elif indicator == "实时资讯新闻播报":
        return pd.DataFrame(data_info_json["list"])

    elif indicator == "实时医院新闻播报":
        return pd.DataFrame(data_info_json["hospital"])

    elif indicator == "前沿知识":
        return pd.DataFrame(data_info_json["papers"])

    elif indicator == "权威发布":
        return pd.DataFrame(data_info_json["power"])

    elif indicator == "滚动新闻":
        return pd.DataFrame(data_info_json["scrollNews"])


def covid_dxy(indicator="湖北"):
    """
    20200315-丁香园接口更新分为国内和国外
    丁香园-全国统计-info
    丁香园-分地区统计-data
    丁香园-全国发热门诊一览表-hospital
    丁香园-全国新闻-news
    :param indicator: ["info", "data", "hospital", "news"]
    :type indicator: str
    :return: 返回指定 indicator 的数据
    :rtype: pandas.DataFrame
    """
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "lxml")
    # news-china
    text_data_news = str(
        soup.find_all("script", attrs={"id": "getTimelineServiceundefined"})
    )
    temp_json = text_data_news[
        text_data_news.find("= [{") + 2 : text_data_news.rfind("}catch")
    ]
    json_data = pd.DataFrame(json.loads(temp_json))
    chinese_news = json_data[
        ["title", "summary", "infoSource", "provinceName", "sourceUrl"]
    ]

    # news-foreign
    text_data_news = str(soup.find_all("script", attrs={"id": "getTimelineService2"}))
    temp_json = text_data_news[
        text_data_news.find("= [{") + 2 : text_data_news.rfind("}catch")
    ]
    json_data = pd.DataFrame(json.loads(temp_json))
    foreign_news = json_data

    # data-domestic
    data_text = str(soup.find("script", attrs={"id": "getAreaStat"}))
    data_text_json = json.loads(
        data_text[data_text.find("= [{") + 2 : data_text.rfind("catch") - 1]
    )
    big_df = pd.DataFrame()
    for i, p in enumerate(jsonpath.jsonpath(data_text_json, "$..provinceName")):
        temp_df = pd.DataFrame(jsonpath.jsonpath(data_text_json, "$..cities")[i])
        temp_df["province"] = p
        big_df = big_df.append(temp_df, ignore_index=True)
    domestic_city_df = big_df

    data_df = pd.DataFrame(data_text_json).iloc[:, :7]
    data_df.columns = ["地区", "地区简称", "现存确诊", "累计确诊", "-", "治愈", "死亡"]
    domestic_province_df = data_df[["地区", "地区简称", "现存确诊", "累计确诊", "治愈", "死亡"]]
    # data-global
    data_text = str(
        soup.find("script", attrs={"id": "getListByCountryTypeService2true"})
    )
    data_text_json = json.loads(
        data_text[data_text.find("= [{") + 2: data_text.rfind("catch") - 1]
    )
    global_df = pd.DataFrame(data_text_json)

    # info
    dxy_static = soup.find(attrs={"id": "getStatisticsService"}).get_text()
    data_json = json.loads(
        dxy_static[dxy_static.find("= {") + 2 : dxy_static.rfind("}c")]
    )
    china_statistics = pd.DataFrame(
        [
            time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(data_json["modifyTime"] / 1000)
            ),
            data_json["currentConfirmedCount"],
            data_json["confirmedCount"],
            data_json["suspectedCount"],
            data_json["curedCount"],
            data_json["deadCount"],
            data_json["seriousCount"],
            data_json["suspectedIncr"],
            data_json["currentConfirmedIncr"],
            data_json["confirmedIncr"],
            data_json["curedIncr"],
            data_json["deadIncr"],
            data_json["seriousIncr"],
        ],
        index=[
            "数据发布时间",
            "现存确诊",
            "累计确诊",
            "境外输入",
            "累计治愈",
            "累计死亡",
            "现存重症",
            "境外输入较昨日",
            "现存确诊较昨日",
            "累计确诊较昨日",
            "累计治愈较昨日",
            "累计死亡较昨日",
            "现存重症较昨日",
        ],
        columns=["info"],
    )
    foreign_statistics = pd.DataFrame.from_dict(
        data_json["foreignStatistics"], orient="index"
    )
    global_statistics = pd.DataFrame.from_dict(
        data_json["globalStatistics"], orient="index"
    )
    # hospital
    url = (
        "https://assets.dxycdn.com/gitrepo/tod-assets/output/default/pneumonia/index.js"
    )
    payload = {"t": str(int(time.time()))}
    r = requests.get(url, params=payload)
    hospital_df = pd.read_html(r.text)[0].iloc[:, :-1]

    if indicator == "中国疫情分省统计详情":
        return domestic_province_df
    if indicator == "中国疫情分市统计详情":
        return domestic_city_df
    elif indicator == "全球疫情分国家统计详情":
        return global_df
    elif indicator == "中国疫情实时统计":
        return china_statistics
    elif indicator == "国外疫情实时统计":
        return foreign_statistics
    elif indicator == "全球疫情实时统计":
        return global_statistics
    elif indicator == "中国疫情防控医院":
        return hospital_df
    elif indicator == "实时播报":
        return chinese_news

    elif indicator == "中国-新增疑似-新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["quanguoTrendChart"][0]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-现存确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["quanguoTrendChart"][1]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-现存疑似-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["quanguoTrendChart"][2]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-治愈-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["quanguoTrendChart"][3]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-死亡-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["quanguoTrendChart"][4]["imgUrl"]).content)
        )
        img_file.show()

    elif indicator == "中国-非湖北新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["hbFeiHbTrendChart"][0]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-湖北新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["hbFeiHbTrendChart"][1]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-湖北现存确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["hbFeiHbTrendChart"][2]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-非湖北现存确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["hbFeiHbTrendChart"][3]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "中国-治愈-死亡-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["hbFeiHbTrendChart"][4]["imgUrl"]).content)
        )
        img_file.show()

    elif indicator == "国外-国外新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["foreignTrendChart"][0]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "国外-国外累计确诊-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["foreignTrendChart"][1]["imgUrl"]).content)
        )
        img_file.show()
    elif indicator == "国外-国外死亡-趋势图":
        img_file = Image.open(
            BytesIO(requests.get(data_json["foreignTrendChart"][2]["imgUrl"]).content)
        )
        img_file.show()

    elif indicator == "国外-重点国家新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][0]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-日本新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][1]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-意大利新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][2]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-伊朗新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][3]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-美国新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][4]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-法国新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][5]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-德国新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][6]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-西班牙新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][7]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    elif indicator == "国外-韩国新增确诊-趋势图":
        img_file = Image.open(
            BytesIO(
                requests.get(
                    data_json["importantForeignTrendChart"][8]["imgUrl"]
                ).content
            )
        )
        img_file.show()
    else:
        try:
            data_text = str(soup.find("script", attrs={"id": "getAreaStat"}))
            data_text_json = json.loads(
                data_text[data_text.find("= [{") + 2 : data_text.rfind("catch") - 1]
            )
            data_df = pd.DataFrame(data_text_json)
            sub_area = pd.DataFrame(
                data_df[data_df["provinceName"] == indicator]["cities"].values[0]
            )
            if sub_area.empty:
                return print("暂无分区域数据")
            sub_area.columns = ["区域", "现在确诊人数", "确诊人数", "疑似人数", "治愈人数", "死亡人数", "id"]
            sub_area = sub_area[["区域", "现在确诊人数", "确诊人数", "疑似人数", "治愈人数", "死亡人数"]]
            return sub_area
        except IndexError as e:
            print("请输入省/市的全称, 如: 浙江省/上海市 等")


def covid_baidu(indicator="湖北"):
    """
    百度-新型冠状病毒肺炎-疫情实时大数据报告
    https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1
    :param indicator: 看说明文档
    :type indicator: str
    :return: 指定 indicator 的数据
    :rtype: pandas.DataFrame
    """
    url = "https://huiyan.baidu.com/openapi/v1/migration/rank"
    payload = {
        "type": "move",
        "ak": "kgD2HiDnLdUhwzd3CLuG5AWNfX3fhLYe",
        "adminType": "country",
        "name": "全国",
    }
    r = requests.get(url, params=payload)
    move_in_df = pd.DataFrame(r.json()["result"]["moveInList"])
    move_out_df = pd.DataFrame(r.json()["result"]["moveOutList"])

    url = "https://opendata.baidu.com/api.php"
    payload = {
        "query": "全国",
        "resource_id": "39258",
        "tn": "wisetpl",
        "format": "json",
        "cb": "jsonp_1580470773343_11183",
    }
    r = requests.get(url, params=payload)
    text_data = r.text
    json_data_news = json.loads(
        text_data.strip("/**/jsonp_1580470773343_11183(").rstrip(");")
    )

    url = "https://opendata.baidu.com/data/inner"
    payload = {
        "tn": "reserved_all_res_tn",
        "dspName": "iphone",
        "from_sf": "1",
        "dsp": "iphone",
        "resource_id": "28565",
        "alr": "1",
        "query": "肺炎",
        "cb": "jsonp_1580470773344_83572",
    }
    r = requests.get(url, params=payload)
    json_data = json.loads(r.text[r.text.find("({") + 1 : r.text.rfind(");")])
    spot_report = pd.DataFrame(json_data["Result"][0]["DisplayData"]["result"]["items"])

    # domestic-city
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    data_json = demjson.decode(soup.find(attrs={"id": "captain-config"}).text)

    big_df = pd.DataFrame()
    for i, p in enumerate(
        jsonpath.jsonpath(data_json["component"][0]["caseList"], "$..area")
    ):
        temp_df = pd.DataFrame(
            jsonpath.jsonpath(data_json["component"][0]["caseList"], "$..subList")[i]
        )
        temp_df["province"] = p
        big_df = big_df.append(temp_df, ignore_index=True)
    domestic_city_df = big_df

    domestic_province_df = pd.DataFrame(data_json["component"][0]["caseList"]).iloc[
        :, :-2
    ]

    big_df = pd.DataFrame()
    for i, p in enumerate(
        jsonpath.jsonpath(data_json["component"][0]["caseOutsideList"], "$..area")
    ):
        temp_df = pd.DataFrame(
            jsonpath.jsonpath(
                data_json["component"][0]["caseOutsideList"], "$..subList"
            )[i]
        )
        temp_df["province"] = p
        big_df = big_df.append(temp_df, ignore_index=True)
    outside_city_df = big_df

    outside_country_df = pd.DataFrame(
        data_json["component"][0]["caseOutsideList"]
    ).iloc[:, :-1]

    big_df = pd.DataFrame()
    for i, p in enumerate(
        jsonpath.jsonpath(data_json["component"][0]["globalList"], "$..area")
    ):
        temp_df = pd.DataFrame(
            jsonpath.jsonpath(data_json["component"][0]["globalList"], "$..subList")[i]
        )
        temp_df["province"] = p
        big_df = big_df.append(temp_df, ignore_index=True)
    global_country_df = big_df

    global_continent_df = pd.DataFrame(data_json["component"][0]["globalList"])[
        ["area", "died", "crued", "confirmed", "confirmedRelative"]
    ]

    if indicator == "热门迁入地":
        return move_in_df
    elif indicator == "热门迁出地":
        return move_out_df
    elif indicator == "今日疫情热搜":
        return pd.DataFrame(json_data_news["data"][0]["list"][0]["item"])
    elif indicator == "防疫知识热搜":
        return pd.DataFrame(json_data_news["data"][0]["list"][1]["item"])
    elif indicator == "热搜谣言粉碎":
        return pd.DataFrame(json_data_news["data"][0]["list"][2]["item"])
    elif indicator == "复工复课热搜":
        return pd.DataFrame(json_data_news["data"][0]["list"][3]["item"])
    elif indicator == "热门人物榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][4]["item"])
    elif indicator == "历史疫情热搜":
        return pd.DataFrame(json_data_news["data"][0]["list"][5]["item"])
    elif indicator == "搜索正能量榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][6]["item"])
    elif indicator == "游戏榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][7]["item"])
    elif indicator == "影视榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][8]["item"])
    elif indicator == "小说榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][9]["item"])
    elif indicator == "疫期飙升榜":
        return pd.DataFrame(json_data_news["data"][0]["list"][10]["item"])
    elif indicator == "实时播报":
        return spot_report
    elif indicator == "中国分省份详情":
        return domestic_province_df
    elif indicator == "中国分城市详情":
        return domestic_city_df
    elif indicator == "国外分国详情":
        return outside_country_df
    elif indicator == "国外分城市详情":
        return outside_city_df
    elif indicator == "全球分洲详情":
        return global_continent_df
    elif indicator == "全球分洲国家详情":
        return global_country_df


def covid_hist_city(city="武汉市"):
    """
    疫情历史数据 城市
    https://github.com/canghailan/Wuhan-2019-nCoV
    2019-12-01开始
    :return: 具体城市的疫情数据
    :rtype: pandas.DataFrame
    """
    url = "https://raw.githubusercontent.com/canghailan/Wuhan-2019-nCoV/master/Wuhan-2019-nCoV.json"
    r = requests.get(url)
    data_json = r.json()
    data_df = pd.DataFrame(data_json)
    return data_df[data_df["city"] == city]


def covid_hist_province(province="湖北省"):
    """
    疫情历史数据 省份
    https://github.com/canghailan/Wuhan-2019-nCoV
    2019-12-01开始
    :return: 具体省份的疫情数据
    :rtype: pandas.DataFrame
    """
    url = "https://raw.githubusercontent.com/canghailan/Wuhan-2019-nCoV/master/Wuhan-2019-nCoV.json"
    r = requests.get(url)
    data_json = r.json()
    data_df = pd.DataFrame(data_json)
    return data_df[data_df["province"] == province]


if __name__ == "__main__":
    # 历史数据
    # epidemic_hist_city_df = covid_hist_province()
    # print(epidemic_hist_city_df)
    # epidemic_hist_province_df = covid_hist_province(province="湖北省")
    # print(epidemic_hist_province_df)

    covid_dxy_df = covid_dxy(indicator="湖北省")
    print(covid_dxy_df)