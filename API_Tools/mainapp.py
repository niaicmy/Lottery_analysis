

Prompt = r'''
==================================================

   A ：  统计数据 -->>>统计每个数出数的间隔, 和值的出数规律
   B ：  数据筛选 -->>>输入要选的数据,和值范围,然后根据要求输出排列的数据集
   Q ：  退出应用
==================================================
'''

def count_num():
    print('in cunt_num')
    pass

def filter_num():
    print('in filter_num')
    pass

def mainapp():

    while True:
        print(Prompt)
        cho = input('输入要选取的功能字母 A/B/Q : ')
        if cho.upper() == 'A':
            count_num()
        elif cho.upper() == 'B':
            filter_num()
        elif cho.upper() == 'Q':
            break
        else :
            print("未找到相应指令！")
            
            
if __name__ == '__main__':
    mainapp()
