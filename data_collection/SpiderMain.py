import requests
# import aiohttp
from lxml import etree
import json
import random


# mode默认false 表示读取文件 更新文件时 update 设置为更新的json 对象
def openconfig(path, update=None):
    if update:
        try:
            with open(file=path, mode=r"w+", encoding=r"utf-8") as fp:
                json.dump(update, fp)
                fp.close()
                # print(path + " : update done")
        except IOError as e:
            print(path + " : update file fail !" + e)
    else:
        try:
            with open(file=path, mode=r"r", encoding=r"utf-8") as fp:
                mycon = json.load(fp)
                fp.close()
                # print(path + " : open done")
        except IOError as e:
            print(path + " : open file fail !" + e)
        else:
            return mycon


# 动态生成requests 的 headers参数
def get_header(config):
    # 随机一个拼凑 header
    headers = {'User-Agent': random.choice(config["headers"])}
    # print(headers)
    return headers


# 动态生成requests 的 proxy参数
def get_proxy(config):
    # proxies = {
    # "http":"http://user:password@127.0.0.1:9999"
    # }
    # t = random.choice(config["proxy"])
    proxy = dict()
    t = random.choice(config["proxy"])
    if "" == t["user"]:
        proxy[str(t["mold"]).lower()] = str(t["mold"]).lower() + r"://" + t["host"] + ":" + t["port"]
    else:
        proxy[str(t["mold"]).lower()] = str(t["mold"]).lower() + r"://" + t["user"] + t["pwd"]\
                                        + "@" + t["host"] + ":" + t["port"]
    # print(proxy)
    return proxy


def get_parser(config, who="lottery"):
    t = dict()
    t["url"] = config["parser"][who]["url"]
    t["path"] = config["parser"][who]["path"]
    return t
# class DownLoader(object):
#     def __init__(self, url=None):
#         if url:
#             super().__init__()
#             self.url = url
#         else:
#             print('downloader url 错误！')
#
#     def down(self):
#         req = requests.get(url=self.url, headers=get_header())
#         if req.ok:
#             req.encoding = req.apparent_encoding
#             return req.text
#         else:
#             req.raise_for_status()
#
#
# class AsyncDownLoader(object):
#     def __init__(self, url=None):
#         if url:
#             super().__init__()
#             self.url = url
#         else:
#             print('downloader url 错误！')
#
#     async def down(self):
#         async with aiohttp.ClientSession as session:
#             async with session.get(url=self.url, headers=get_header()) as req:
#                 if req.ok:
#                     req.encoding = req.apparent_encoding
#                     return await req.text()
#                 else:
#                     req.raise_for_status()

# 自动更新 Http config proxy
# with open(file="Httpconfig.json", mode="a+", encoding="utf-8") as fp:
#     json.dump(config, fp)
#     fp.close()


# p表示要解析的对象 c表示配置文件json对象
def parser(path, who, num):
    """
    path: 配置文件路径
    who: 解析那一个数据
    con: 附加参数 与 who 相关联
    """

    config = openconfig(path)
    par = get_parser(config, who)

    if "lottery" == who:
        # 表示取的期数
        req = requests.get(par["url"].format(num), headers=get_header(config), proxies=get_proxy(config))
        if req.ok:
            html = etree.HTML(req.text)
            # print(html.xpath(tem["path"]))
            # ['01', '08', '11', '26', '28', '31', '04']
            li = html.xpath(par["path"])
            # print(li)
            if '{Result2}' == li[0]:
                # print("ssq No data ! or The data is the latest !")
                # 可以这样 检查2-4 次 返回 None 的结果来判断 期数是不是最新 当然可以同步数据库 只检测最新期数
                return None
            else:
                return li

    elif "proxy" == who:
        # 这里是表示第几页
        req = requests.get(par["url"].format(num), headers=get_header(config), proxies=get_proxy(config))
        if req.ok:
            html = etree.HTML(req.text)
            # print(html.xpath(tem["path"]))
            # 表示取第几个数据 一页共20个
            # ['125.117.120.229', '9000', '高匿名', 'HTTP', '浙江省金华市  电信', '3秒', '2018-06-25 15:30:46']
            tem = list()

            for i in range(1, 21):
                pro = html.xpath(par["path"].format(i))
                if int(pro[5][0]) < 2:
                    tem.append(pro)
                elif len(tem) >= 5:
                    break
            return tem

    # if req.ok:
    #     html = etree.HTML(req.text)
    #     # print(html.xpath(tem["path"]))
    #     return html.xpath(tem["path"])


if __name__ == '__main__':
    print(parser("Httpconfig.json", "lottery", 18001))
    print(parser("Httpconfig.json", "proxy", 1))
    # 打开配置文件
