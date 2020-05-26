#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 13:09
# @Author  : justin.郑 3907721@qq.com
# @File    : cons.py
# @Desc    : 网红经济行业

STAR_COOKIE = 'gr_user_id=d73ea970-adf9-44f1-ba2f-2b1e49b6d1e7; grwng_uid=ba191569-5bb2-4fe2-b810-bc9e601d05d4; tt_webid=6807980764321318408; csrftoken=oX0pXOTFAOWZzT9F6YiTXl9IaUQRqFzk; odin_tt=8da95c0df1c8b0895664d60f7a0364faae5f7976d37a3ecd8b9c0c0ccaae9fdaa482facc4cc18141b88637b65f1cb5606993458b12f9ebc871e7ca4075c2757c; uid_tt_ss=3c813e052e5e95791768bd4231001b83; sessionid_ss=fc6684106be289e3779f9f42642b6d1d; gftoken=ZmM2Njg0MTA2YnwxNTg1NzA0MzYzNTd8fDAGBgYGBgY; _ga=GA1.2.1344526501.1586990335; 8632e941eb705978_gr_session_id=302d6c66-4b48-46c1-83a4-af955647e153; 8632e941eb705978_gr_session_id_302d6c66-4b48-46c1-83a4-af955647e153=true; s_v_web_id=k99e1ezn_l6N3CQ5r_EWzv_4Mw1_9KWY_F9ONZ8zZJCVC; login_flag=ac43e4155b6a263e3331a583d086d780; sid_tt=5b218149652bc0cc7b4f7e56f2d908a9; uid_tt=f3105a05f7e173962fde7c8e7f647d26fde210733ea4c266a870ee459c772584; sessionid=5b218149652bc0cc7b4f7e56f2d908a9; star_sessionid=5b218149652bc0cc7b4f7e56f2d908a9; sid_guard="5b218149652bc0cc7b4f7e56f2d908a9|1587442099|15552000|Sun\054 18-Oct-2020 04:08:19 GMT"; SLARDAR_WEB_ID=31ed1b8f-dd60-4d2e-ab09-e952113fee1a'


STAR_HOT_URL = {
    "抖音达人热榜-星图指数榜-全部": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=2fed15d4bd4ced9f29081b6636529be3",
    "抖音达人热榜-星图指数榜-颜值达人": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E9%A2%9C%E5%80%BC%E8%BE%BE%E4%BA%BA&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=dd13e4123f98b324a180bab753bc628c",
    "抖音达人热榜-星图指数榜-剧情搞笑": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E5%89%A7%E6%83%85%E6%90%9E%E7%AC%91&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=ad12718bce3776998bb250bc4cd3a6a9",
    "抖音达人热榜-星图指数榜-美妆": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E7%BE%8E%E5%A6%86&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=ff2e737d9008f495347908924878aaaf",
    "抖音达人热榜-星图指数榜-时尚": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%97%B6%E5%B0%9A&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=6f4ba341c3744daabf0456d482d11dc9",
    "抖音达人热榜-星图指数榜-萌宠": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E8%90%8C%E5%AE%A0&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=e42e33dbff38f86e086a92d4a7c701ad",
    "抖音达人热榜-星图指数榜-音乐": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E9%9F%B3%E4%B9%90&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=458e07ea4f387008dc21a4a4321ece76",
    "抖音达人热榜-星图指数榜-舞蹈": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E8%88%9E%E8%B9%88&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=58df0a68bbc790f1f7a72cb366ef774f",
    "抖音达人热榜-星图指数榜-美食": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E7%BE%8E%E9%A3%9F&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=109060a3de7154dfeeb7bbb3d71c815a",
    "抖音达人热榜-星图指数榜-游戏": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%B8%B8%E6%88%8F&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=3c0bbcb5a77af35e89d5a3f4c1f27d6e",
    "抖音达人热榜-星图指数榜-旅行": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%97%85%E8%A1%8C&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=8ad4e0f8d311331679df0ee4ee0e2222",
    "抖音达人热榜-星图指数榜-汽车": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%B1%BD%E8%BD%A6&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=576874d80792429288226e1eeb3d8fe3",
    "抖音达人热榜-星图指数榜-生活": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E7%94%9F%E6%B4%BB&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=f4afdc41eff79a011c15240aafe699ad",
    "抖音达人热榜-星图指数榜-测评": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%B5%8B%E8%AF%84&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=13d3b98b4ed53cd4bd94b484f05f6fb8",
    "抖音达人热榜-星图指数榜-二次元": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E4%BA%8C%E6%AC%A1%E5%85%83&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=94f85ba5e09faa8f44e73281add376dd",
    "抖音达人热榜-星图指数榜-母婴亲子": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%AF%8D%E5%A9%B4%E4%BA%B2%E5%AD%90&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=bbfe3df3e4723905aa1ce85f8d517d92",
    "抖音达人热榜-星图指数榜-科技数码": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E7%A7%91%E6%8A%80%E6%95%B0%E7%A0%81&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=2c5f2fd675f1a2c6b4489753fc19f417",
    "抖音达人热榜-星图指数榜-教育培训": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%95%99%E8%82%B2%E5%9F%B9%E8%AE%AD&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=209545266b0ab86277602f6bf366bffa",
    "抖音达人热榜-星图指数榜-运动健身": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E8%BF%90%E5%8A%A8%E5%81%A5%E8%BA%AB&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=83aed6604a6bd57b8b24b0315e02669a",
    "抖音达人热榜-星图指数榜-家居家装": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E5%AE%B6%E5%B1%85%E5%AE%B6%E8%A3%85&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=253a39d7354fdfeda434b71f521db36c",
    "抖音达人热榜-星图指数榜-才艺技能": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%89%8D%E8%89%BA%E6%8A%80%E8%83%BD&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=2b2635b3697700078a79c716cb019d61",
    "抖音达人热榜-星图指数榜-影视娱乐": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E5%BD%B1%E8%A7%86%E5%A8%B1%E4%B9%90&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=d2b2e189aec4c6349ad2980d0279da6e",
    "抖音达人热榜-星图指数榜-艺术文化": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E8%89%BA%E6%9C%AF%E6%96%87%E5%8C%96&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=4b1191492b150415e331da02c69c0b10",
    "抖音达人热榜-星图指数榜-财经投资": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E8%B4%A2%E7%BB%8F%E6%8A%95%E8%B5%84&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=313239b33b29720e752698033d72e0ce",
    "抖音达人热榜-星图指数榜-情感": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E6%83%85%E6%84%9F&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=be47713df317e09574b0a7e880e3cec2",
    "抖音达人热榜-星图指数榜-三农": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E4%B8%89%E5%86%9C&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=23c34c6b6a480c5a292e76eced7b5252",
    "抖音达人热榜-星图指数榜-园艺": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6766936376500813837&tag=%E5%9B%AD%E8%89%BA&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=929bfc99bbfd53c671e7538a5d0e3951",

    "抖音达人热榜-种草指数榜-全部": "https://star.toutiao.com/h/api/gateway/handler_get/?hot_list_id=6758055829141717005&tag=&service_name=author.AdStarAuthorService&service_method=GetHotListData&sign=e4476e7c0d875d205f6b36b8d3bc2da0",

}

STAR_MARKET_DOUYIN_CATEGORY = [
    {
		"second": [{
				73: "美女"
			},
			{
				74: "帅哥"
			}
		],
		"first": {
			72: "颜值达人"
		}
	},
	{
		"second": [{
				98: "剧情"
			},
			{
				99: "搞笑"
			}
		],
		"first": {
			97: "剧情搞笑"
		}
	},
	{
		"second": [{
				2: "美妆教程"
			},
			{
				3: "妆容展示"
			},
			{
				4: "护肤保养"
			},
			{
				5: "美妆测评种草"
			}
		],
		"first": {
			1: "美妆"
		}
	},
	{
		"second": [{
				7: "穿搭"
			},
			{
				8: "街拍"
			},
			{
				10: "造型"
			}
		],
		"first": {
			6: "时尚"
		}
	},
	{
		"second": [{
				12: "日常宠物"
			},
			{
				13: "特别宠物"
			},
			{
				14: "宠物周边"
			}
		],
		"first": {
			11: "萌宠"
		}
	},
	{
		"second": [{
				42: "歌曲演唱"
			},
			{
				43: "乐器演奏"
			},
			{
				44: "音乐教学"
			},
			{
				45: "音乐其他"
			}
		],
		"first": {
			41: "音乐"
		}
	},
	{
		"second": [],
		"first": {
			46: "舞蹈"
		}
	},
	{
		"second": [{
				49: "美食教程"
			},
			{
				50: "美食探店"
			},
			{
				51: "吃播大胃王"
			},
			{
				52: "美食产品测评"
			},
			{
				53: "乡村野食"
			},
			{
				54: "美食其他"
			}
		],
		"first": {
			48: "美食"
		}
	},
	{
		"second": [{
				119: "真人出镜"
			},
			{
				120: "游戏实况"
			},
			{
				121: "游戏剧情"
			},
			{
				122: "游戏解说"
			},
			{
				123: "游戏资讯"
			}
		],
		"first": {
			23: "游戏"
		}
	},
	{
		"second": [{
				28: "旅行记录"
			},
			{
				29: "旅行攻略"
			},
			{
				30: "旅行推荐"
			}
		],
		"first": {
			27: "旅行"
		}
	},
	{
		"second": [{
				32: "汽车测评"
			},
			{
				33: "汽车知识"
			},
			{
				34: "汽车周边"
			}
		],
		"first": {
			31: "汽车"
		}
	},
	{
		"second": [{
				39: "生活小窍门"
			},
			{
				40: "好物推荐"
			},
			{
				118: "健康养生"
			}
		],
		"first": {
			36: "生活"
		}
	},
	{
		"second": [{
				16: "美妆测评"
			},
			{
				17: "3C数码测评"
			},
			{
				18: "汽车测评"
			},
			{
				19: "美食产品测评"
			},
			{
				20: "母婴产品测评"
			},
			{
				21: "综合测评"
			}
		],
		"first": {
			15: "测评"
		}
	},
	{
		"second": [{
				125: "二次元真人"
			},
			{
				126: "动画漫画"
			},
			{
				127: "配音声优"
			},
			{
				128: "宅物手办"
			}
		],
		"first": {
			25: "二次元"
		}
	},
	{
		"second": [{
				56: "育儿科普"
			},
			{
				57: "萌娃日常"
			},
			{
				58: "亲子互动"
			},
			{
				59: "测评种草"
			}
		],
		"first": {
			55: "母婴亲子"
		}
	},
	{
		"second": [{
				65: "3C数码"
			},
			{
				66: "家居电器"
			}
		],
		"first": {
			64: "科技数码"
		}
	},
	{
		"second": [{
				69: "考学培训"
			},
			{
				70: "语言教学"
			},
			{
				71: "个人管理"
			}
		],
		"first": {
			68: "教育培训"
		}
	},
	{
		"second": [{
				61: "健身"
			},
			{
				62: "竞技体育"
			},
			{
				63: "极限运动"
			}
		],
		"first": {
			60: "运动健身"
		}
	},
	{
		"second": [{
				76: "家装设计"
			},
			{
				77: "装修知识"
			}
		],
		"first": {
			75: "家居家装"
		}
	},
	{
		"second": [{
				80: "创意才能"
			},
			{
				81: "手工"
			},
			{
				82: "摄影"
			},
			{
				83: "绘画"
			},
			{
				84: "其他才艺"
			}
		],
		"first": {
			79: "才艺技能"
		}
	},
	{
		"second": [],
		"first": {
			85: "影视娱乐"
		}
	},
	{
		"second": [{
				88: "传统文化"
			},
			{
				89: "人文科普"
			},
			{
				90: "自然科学"
			}
		],
		"first": {
			87: "艺术文化"
		}
	},
	{
		"second": [{
				92: "传统金融"
			},
			{
				93: "互联网金融"
			},
			{
				94: "财经知识"
			}
		],
		"first": {
			91: "财经投资"
		}
	},
	{
		"second": [],
		"first": {
			100: "情感"
		}
	},
	{
		"second": [],
		"first": {
			95: "三农"
		}
	},
	{
		"second": [],
		"first": {
			102: "园艺"
		}
	}
]