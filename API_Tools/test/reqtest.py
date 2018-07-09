import requests
import os
import re
import pymysql

req = requests.get("http://kaijiang.500.com/shtml/ssq/18028.shtml")

#print('url  is : {}'.format(req.url))
#print('url encoding is : {}'.format(req.encoding))
#print(u'url text is : {}'.format(req.text))
req.encoding = 'utf-8'


#f = open(r"C:\Users\niaic\Desktop\te.txt",'wb+')
#f.write(req.content)
#f.close()

re_red = re.compile('<li class\="ball_red">(\d+?)</li>')
re_blue = re.compile('<li class\="ball_blue">(\d+?)</li>')

sea_red = re_red.findall(req.text)
sea_blue = re_blue.findall(req.text)

print (sea_red, sea_blue)

