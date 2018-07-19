import requests
# import aiohttp
from lxml import etree
import json
import random
import os


# mode默认false 表示读取文件 更新文件时 update 设置为更新的json 对象
def openconfig(path, update=None):
    if update:
        try:
            with open(file=path, mode=r"w+", encoding=r"utf-8") as fp:
                # indent 表示json 文件 格式化输出  数字代表格式的缩进 2 比较漂亮
                json.dump(update, fp, indent=2)
                fp.close()
                # print(path + " : update done")
        except IOError:
            print(path + " : update file fail !")
    else:
        try:
            with open(file=path, mode=r"r", encoding=r"utf-8") as fp:
                mycon = json.load(fp)
                fp.close()
                # print(path + " : open done")
        except IOError:
            print(path + " : open file fail !")
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
        proxy[str(t["mold"]).lower()] = str(t["mold"]).lower() + r"://" + t["user"] + t["pwd"] \
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
def parser(who, num):
    """
    who: 解析那一个数据
    con: 附加参数 与 who 相关联
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(base_dir)
    abs_dir = base_dir + r"\data_handle\Httpconfig.json"
    # print(abs_dir)
    config = openconfig(abs_dir)
    par = get_parser(config, who)
    # print(par)

    if "lottery" == who:
        # 表示取的期数
        try:
            # req = requests.get(par["url"].format(num), timeout=5, headers=get_header(config),
            # proxies=get_proxy(config))
            # 去除代理
            req = requests.get(par["url"].format(num), timeout=5, headers=get_header(config))
        except requests.exceptions.Timeout:
            return None
        except requests.exceptions.ConnectionError:
            return None
        else:
            if req.ok:
                html = etree.HTML(req.text)
                # print(html.xpath(tem["path"]))
                # ['01', '08', '11', '26', '28', '31', '04']
                li = html.xpath(par["path"])
                # print(li)
                if '{Result2}' == li[0]:
                    # print("ssq No data ! or The data is the latest !")
                    # 可以这样 检查2-4 次 返回 None 的结果来判断 期数是不是最新 当然可以同步数据库 只检测最新期数
                    # req.close()
                    return None
                else:
                    # req.close()
                    return li
            elif req.status_code == 404:  # 返回404
                # req.close()
                return None

    elif "proxy" == who:
        # 这里是表示第几页
        try:
            req = requests.get(par["url"].format(num), timeout=10, headers=get_header(config),
                               proxies=get_proxy(config))
        except requests.exceptions.Timeout:
            return None
        except requests.exceptions.ConnectionError:
            return None
        else:
            if req.ok:
                tem = list()
                html = etree.HTML(req.text)
                # print(html.xpath(tem["path"]))
                # 表示取第几个数据 一页共15个
                # ['125.117.120.229', '9000', '高匿名', 'HTTP', '浙江省金华市  电信', '3秒', '2018-06-25 15:30:46']
                # 取网页数据
                for i in range(1, 16):
                    pro = html.xpath(par["path"].format(i))
                    pro = pro[1::2]
                    # print(pro)
                    # print(pro[5][0])
                    if int(pro[5][0]) <= 3:
                        tem.append(pro)
                    if len(tem) >= 5:
                        break
                # 更新 proxy
                if tem[0]:
                    # print(tem)
                    count = 0
                    for p in tem:
                        config["proxy"][count]["host"] = p[0]
                        config["proxy"][count]["port"] = p[1]
                        config["proxy"][count]["mold"] = p[3]
                        count += 1
                        # config["proxy"][count]["user"] = p[0]
                        # config["proxy"][count]["pwd"] = p[0]

            openconfig(abs_dir, config)

    # elif "proxy2" == who:
    #     print("proxy2")
    #     try:
    #         req = requests.get(par["url"], timeout=10, headers=get_header(config),
    #                            proxies=get_proxy(config))
    #     except requests.exceptions.Timeout:
    #         return None
    #     except requests.exceptions.ConnectionError:
    #         return None
    #     else:
    #         if req.ok:
    #             tem = list()
    #             html = etree.HTML(req.text)
    #
    #             for i in range(2, 16):
    #                 pro = html.xpath(par["path"].format(num, i))
    #                 print(pro)
    #                 if int(pro[5][0]) <= 3:
    #                     tem.append(pro)
    #                 if len(tem) >= 5:
    #                     break
    #             # 更新 proxy
    #             if tem[0]:
    #                 # print(tem)
    #                 count = 0
    #                 for p in tem:
    #                     config["proxy"][count]["host"] = p[0]
    #                     config["proxy"][count]["port"] = p[1]
    #                     config["proxy"][count]["mold"] = p[3]
    #                     count += 1
    #                     # config["proxy"][count]["user"] = p[0]
    #                     # config["proxy"][count]["pwd"] = p[0]
    #
    #         openconfig(abs_dir, config)


if __name__ == '__main__':
    print(parser("lottery", 18001))
    # print(parser("proxy", 1))
    # print(parser("proxy2", 1))
    # 打开配置文件
