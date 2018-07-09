'''
获取开奖数据的模块
build data : 20180321  in  CD

url  = http://kaijiang.500.com/shtml/ssq/18031.shtml

<li class="ball_red">02</li>       <li class="ball_red">(\d+?)</li>

<li class="ball_blue">14</li>      <li class="ball_blue">(\d+?)</li>

<strong>18031</strong></font>      <strong>(\d+?)</strong></font>
'''

#import lotteryurl
#get_data_url(typ) --->> typ (str) 
from lotteryurl import get_data_url
import requests
import time
import re
import pymysql

#两个球的正则表达式
re_red = re.compile('<li class\="ball_red">(\d+?)</li>')
re_blue = re.compile('<li class\="ball_blue">(\d+?)</li>')
re_term = re.compile('<strong>(\d+?)</strong></font>')

def  get_lottery_data(lottery_url):
      url_data = lottery_url[ : ]
      lottery_data = { }
     # print(url_data)
      for  url in url_data:
            req = requests.get (url)
            req.encoding = 'utf-8'
            sea_blue = re_blue.findall(req.text)
            if sea_blue ==[ ]:
                continue
            sea_red = re_red.findall(req.text)
            #sea_blue = re_blue.findall(req.text)
            sea_term = re_term.findall(req.text)
            
            tem = sea_red + sea_blue
            #注意数据的转换
            lottery_data[sea_term[0]] = tuple(tem)
            #休息1S
            time.sleep(1)
            
      return lottery_data

def  store_lottery_data( data_dic):
      #数据库的储存方法
      baseconfig ={ 'host' : 'localhost',
            'port' : 3306,
            'db' : 'pymysql',
            'user' : 'root',
            'password' : 'admin'
            }
      con = pymysql.connect( **baseconfig);
      cur = con.cursor()
      sql_create = """
              CREATE TABLE IF NOT EXISTS lottery_ssq_data(
              term_id int(8) primary key,
              red1 int(4),
              red2 int(4),
              red3 int(4),
              red4 int(4),
              red5 int(4),
              red6 int(4),
              blue  int(4),
              sum  int(4)
              )
              """
      try:
            cur.execute(sql_create)
            #cur.execute(sqlin)
            cur.execute(sqlup)
            con.commit()
            
      except:
            con.rollback()
            
      cur.close()
      con.close()

if __name__ =="__main__":
    dic = get_lottery_data(get_data_url("ssq"))
    print(dic)
    '''
    dic 的数据格式 ，以双色球为例：键为 期数   键值为开奖号码元组（6个红球+1个篮球）
    {'14001': ('03', '09', '15', '20', '27', '29', '01'), '14002': ('04', '21', '23', '31', '32', '33', '04'), '14003': ('06', '10', '11', '28', '30', '33', '12')}
    '''


