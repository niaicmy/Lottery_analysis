import pymysql

#先实现一种
_lottery_type = {
    0 : 'lottery_data',
    'ssq' : 'lottery_ssq_data',
    'qlc' : 'lottery_qlc_data'
    }

#_data_dic = {'14001': ('03', '09', '15', '20', '27', '29', '01'), '14002': ('04', '21', '23', '31', '32', '33', '04'), '14003': ('06', '10', '11', '28', '30', '33', '12')}
_data_dic = {'14001': ('03', '09', '15', '20', '27', '29', '01','104'), '14002': ('04', '21', '23', '31', '32', '33', '04', '148'), '14003': ('06', '10', '11', '28', '30', '33', '12', '130')}
#打开数据库连接  
#db= pymysql.connect(host="localhost",user="root",  password="123456",db="test",port=3307)

baseconfig ={ 'host' : '127.0.0.1',
            'port' : 3306,
           # 'db' : 'pymysql',
            'user' : 'root',
            'password' : 'admin'
            }
con = pymysql.connect( **baseconfig);
cur = con.cursor()

sql_show_bases = r'''SHOW DATABASES'''
sql_show_tables =r'''SHOW TABLES'''
sql_drop_base = r'''DROP DATABASE {0}'''
sql_drop_table = r'''DROP TABLE {0}'''

# 带参数的都可以for循环来遍历
sql_use_base = r'''USE {0}'''.format(_lottery_type[0])
sql_create_base =r'''CREATE DATABASE IF NOT EXISTS {0}'''.format(_lottery_type[0])
#INSERT INTO  { tablename }    VALUES  { values } 
#sql_insert_values = '''INSERT INTO {0} VALUES ({1}, {2}) '''

#可以用 for  遍历 _lottery_type 来创建数据表
#for term  in _lottery_type.kyes()
#term = 'ssq'
sql_create_table = r'''CREATE TABLE IF NOT EXISTS {0}(
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
                       '''#.format(_lottery_type[term])

cur.execute(sql_show_bases)
#注意fetchall() 函数的额返回值是一个成对的元组 如： (('information_schema',), ('learn',), ('lottery_data',))
values = cur.fetchall( )
#print('databases have : {}'.format(values))

#所以我们的判断是用元组的形式
if (_lottery_type[0], ) not in values:
    cur.execute(sql_create_base.format(_lottery_type[0]))
    con.commit()
else:
    cur.execute(sql_use_base)
    cur.execute(sql_show_tables)
    values = cur.fetchall( )
    
    #print('datatables have : {}'.format(values))
    #if _lottery_type[key] not in values:
    #所以我们的判断是用元组的形式
    
    if (_lottery_type['ssq'], ) not in values:
        cur.execute(sql_create_table.format(_lottery_type['ssq']))
        con.commit()
    else:
        try:
            #print('here is :')
            #_data_dic = {'14001': ('03', '09', '15', '20', '27', '29', '01','104'), '14002': ('04', '21', '23', '31', '32', '33', '04', '148'), '14003': ('06', '10', '11', '28', '30', '33', '12', '130')}
            #INSERT INTO  { tablename }    VALUES  { values }
            #for 遍历字典插入
            #插入字典要注意 判断term_id int(8) primary key, 这个主键是否存在 存在就跳过
            #values = cur.execute(r'''SELECT term_id  FROM {0}  ORDER BY term_id DESC '''.format(_lottery_type['ssq']))
            
            values = cur.execute(r'''SELECT term_id  FROM {0}'''.format(_lottery_type['ssq']))
            
            for k, v in _data_dic.items():
                #判断 K是否在
                if k not in values:
                    sql_insert_values = r'''INSERT INTO {0} VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}) '''.format(_lottery_type['ssq'], k, *v)
                    print(sql_insert_values)
                    cur.execute(sql_insert_values)
                    
            con.commit()
        #下面就是插入数据的操作了
        except:
            #出错就滚回去
            con.rollback()

'''
dic = {'14001': ('03', '09', '15', '20', '27', '29', '01'), '14002': ('04', '21', '23', '31', '32', '33', '04'), '14003': ('06', '10', '11', '28', '30', '33', '12')}
try:
    cur.execute(sql_create_base)
except pymysql.err.Warning as pw:
    pass
    #print(repr(pw))
    
cur.execute(sql_use_base)

try:
    cur.execute(sql_create_table)
except  pymysql.err.Warning as pw:
    pass
    #print(repr(pw))
'''
#con.commit()

cur.close()
con.close()

