'''
处理开奖数据连接地址的模块
build data : 20180321  in  CD

url  = http://kaijiang.500.com/shtml/ssq/18031.shtml

<li class="ball_red">02</li>       <li class="ball_red">(\d+?)</li>

<li class="ball_blue">14</li>      <li class="ball_blue">(\d+?)</li>

<strong>18031</strong></font>			
'''
#构造全局的开奖类型的参数字典
_lottery_dic = {
      'ssq_dic' :{
            #'ssq_url' : 'http://kaijiang.500.com/shtml/ssq/18031.shtml'
            'ssq_year_l' : 14000,
            'ssq_year_m' : 16000,
            #'ssq_year_m' : 100000
            'ssq_year_step'  : 1000,
            #'ssq_max_term' : 156
            'ssq_max_term' : 6
            },
      'qlc_dic':{
           # 'qlc_url' : 'http://kaijiang.500.com/shtml/qlc/18031.shtml'
            'qlc_year_l' : 14000,
            #'qlc_year_m' : 100000,
            'qlc_year_m' : 16000,
            'qlc_year_step'  : 1000,
            #'qlc_max_term' : 156
            'qlc_max_term' : 6
            }
      }

#目标网站的地址构造
__target = r'http://kaijiang.500.com/shtml/{0}/{1}.shtml'

''' 
#从2014年开始
ssq_year_l = 14000
#构造到2099年
ssq_year_m = 100000
#双色球年份的步进
ssq_year_step = 1000
#双色球最大期数
ssq_max = 156
'''
#默认开奖类型
#def_typ = ssq

def  _lottery_term(typ):
      '''
      传入开奖的类型 参数类型为str 
      构造开奖期数，返回开奖期数的列表
      '''
      ret = [ ]
      for year in range(_lottery_dic[typ + '_dic'][typ + '_year_l'], _lottery_dic[typ + '_dic'][typ + '_year_m'], _lottery_dic[typ + '_dic'][typ + '_year_step']) :
            for te in range(1, _lottery_dic[typ + '_dic'][typ + '_max_term']) :
                  term = year + te
                  ret.append(term)
      #返回期数的列表
      return ret

      '''
      for year in range(ssq_year_l, ssq_year_m, ssq_year_step):
            for x in range(1, ssq_max):
                  term = year + x
                  ret.append(term)        
      #返回期数的列表
      return ret
      '''
      
#传入开奖的类型与开奖的期数列表
def  get_data_url(typ) :
      '''
      传入开奖的类型 typ (str)  开奖期数的列表 (list)
      构造开奖数据的url,返回构造好的url 列表
      '''
      ret =  _lottery_term(typ)
      url = [ ]
      #构造url
      for  term in ret :
            url.append(__target.format(typ, term))
      #返回构造好的url      
      return url

if __name__ == "__main__" :
      test = get_data_url('ssq')
      print(test)
      test = get_data_url('qlc')
      print(test)
      
