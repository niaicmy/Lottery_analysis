import requests
from .HttpConfig import get_header


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
