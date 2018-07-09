'''
构造输出要求的组合队列

'''
#只是挑选红球的组合
def cho_red(L, typ):
      '''
      传入参数L 是list  typ 是int 返回值是个list
      函数作用是从一个列表选取 任意不重复的组合 并作为结果
      函数的默认值只解释一次 再次调用就会消除默认值
      '''
      if L == None:
            return None
      
      LL = L[ : ]
      LL.sort( )
      ty = typ
      tt = [ ]
      i = 0
      tem = [ ]#初始化可以放在外面
      
      for x in LL :
            j = i + ty -1 #构造最后项的index

            #初始化再次进入循环的基础list
            #tem = []#初始化可以放在外面
            tem = LL[ i:i + ty ]#取固定长度的list
            
            while j< len( LL ) and ( i + ty ) <=len ( LL ):
                  '''
                  #初始化再次进入循环的基础list
                  tem = [ ]
                  tem = LL[ i:i + ty ]
                  '''
                  #拼接要选取的list
                  tem = tem[ :-1] + [ LL[ j ]]
                  tt.append( tem )
                  j+=1
                  
            i+=1
            
      return tt


#构造输入红球、蓝球的所有组合
def  lastlist(red_list, blue_list):
      last = [ ]
      
      for blue in blue_list:
            for red in red_list:
                  last.append(red + [blue])
                  
      return last


#返回符合要求的组合
def demand_num(lt, su):
      last = []
      
      for item in lt:
            if su[0] <= item[1] <= su[1]:
                  last.append(item)
                  
      return last
                  

      


if __name__ == '__main__':
      '''
      tes = [1,2,3,4,5,6,7]
      t = [sum(x) for x in cho_red(tes, 3)]
      print(cho_red(tes, 3))
      print(t)
      te = list(zip(cho_red(tes, 3), t))
      print(te)
      '''
      Ltr = [1, 3, 5, 7, 9, 13, 16, 18]
      Ltb = [5, 11, 16]
      typt = 6

      Resu = lastlist(cho_red(Ltr, typt), Ltb)
      
      t = [sum(x) for x in Resu] #每一组数据求和,列表生成式 
      te = list(zip(Resu, t)) # zip返回的一组一组的元组
      
      print( te )
      
      #su = (22, 199)
      su = (50, 55)
      last = demand_num(te, su)
      
      print(last)
