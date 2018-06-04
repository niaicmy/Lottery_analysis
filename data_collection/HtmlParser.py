import re
from bs4 import BeautifulSoup as BS4


class HtmlParser(object):
    def __init__(self, content=None):
        if content:
            super().__init__()
            self.content = content
        else:
            print('网页内容出错！')

    def parser(self):
        pass
