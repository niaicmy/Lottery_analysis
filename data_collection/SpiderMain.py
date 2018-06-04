from . import DownLoader
from . import HtmlParser
from . import HtmlOutputer
from . import UrlManage

from ssq_analysis.models import *


class SpiderMain(object):
    def __init__(self, url):
        self.target_url = url
        urlmanage = UrlManage.UrlManage()
        downloader = DownLoader.DownLoader()
        htmlparser = HtmlParser.HtmlParser()
        htmloutputer = HtmlOutputer.HtmlOutputer()
