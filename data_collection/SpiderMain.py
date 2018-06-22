import requests
import aiohttp
import json
import random
from ssq_analysis.models import SsqInfo

with open(file="Httpconfig.json", mode="r", encoding="utf-8") as fp:
    config = json.load(fp)
    fp.close()


# 动态生成requests 的 headers参数
def get_header():
    # 随机一个拼凑 header
    headers = {'User-Agent': random.choice(config["headers"])}
    # print(headers)
    return headers


# 动态生成requests 的 proxy参数
def get_proxy():
    # proxy = "http://user:pass@some.proxy.com"
    t = random.choice(config["proxy"])
    if "" == t["user"]:
        proxy = str(t["mold"]).lower() + r"://" + t["host"] + ":" + t["port"]
    else:
        proxy = str(t["mold"]).lower() + r"://" + t["user"] + t["pwd"] + "@" + t["host"] + ":" + t["port"]
    # print(proxy)
    return proxy


class DownLoader(object):
    def __init__(self, url=None):
        if url:
            super().__init__()
            self.url = url
        else:
            print('downloader url 错误！')

    def down(self):
        req = requests.get(url=self.url, headers=get_header())
        if req.ok:
            req.encoding = req.apparent_encoding
            return req.text
        else:
            req.raise_for_status()


class AsyncDownLoader(object):
    def __init__(self, url=None):
        if url:
            super().__init__()
            self.url = url
        else:
            print('downloader url 错误！')

    async def down(self):
        async with aiohttp.ClientSession as session:
            async with session.get(url=self.url, headers=get_header()) as req:
                if req.ok:
                    req.encoding = req.apparent_encoding
                    return await req.text()
                else:
                    req.raise_for_status()

# 自动更新 Http config proxy
# with open(file="Httpconfig.json", mode="a+", encoding="utf-8") as fp:
#     json.dump(config, fp)
#     fp.close()


if __name__ == '__main__':
    get_header()
    get_proxy()
