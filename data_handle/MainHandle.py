"""
构造输出要求的组合队列

"""


# 只是挑选红球的组合
def main_handle(red_list, blue_list, sum_list, model=6):
    """
    传入参数red_list blue_list sum_list是list  model 是int 代表红球个数
    返回值是个list
    函数作用是从一个列表选取 任意不重复的组合 并作为结果
    函数的默认值只解释一次 再次调用就会消除默认值
    """
    if (red_list is None) or (blue_list is None):
        return None

    red_list.sort()
    red_result = []
    i = 0

    while (i + model) <= len(red_list):

        # 构造最后项的index
        j = i + model - 1
        # 取固定长度的list
        tem = red_list[i:i + model]

        while j < len(red_list):
            # 拼接要选取的list
            tem = tem[:-1] + [red_list[j]]
            red_result.append(tem)
            j += 1

        i += 1

    # 上面是构造红球的组合放入 red_result 中

    # 构造输入红球、蓝球的所有组合 放入 match_last 中
    match_last = []
    blue_list.sort()

    for blue in blue_list:
        for red in red_result:
            match_last.append(red + [blue])

    # 计算奇偶比 和值 放入  result_list 中

    result_list = []

    # 计算全部的 奇偶比  和值

    for group in match_last:
        m_odd = 0
        m_even = 0
        m_sum = 0

        for i in group:
            m_sum += i
            if i % 2 == 0:
                m_even += 1
            else:
                m_odd += 1

        if sum_list[0] <= m_sum <= sum_list[1]:
            result_list.append(group + [str(m_odd) + ":" + str(m_even)] + [m_sum])

    if result_list:
        return result_list
    else:
        return None


# # 构造输入红球、蓝球的所有组合
# def last_list(red_list, blue_list):
#     last = []
#     blue_list.sort()
#
#     for blue in blue_list:
#         for red in red_list:
#             last.append(red + [blue])
#
#     return last


# # 返回符合要求的组合
# def demand_num(lt, su):
#     last = []
#
#     for item in lt:
#         if su[0] <= item[1] <= su[1]:
#             last.append(item)
#
#     return last


if __name__ == "__main__":
    red_li = [1, 3, 5, 7, 9, 13, 16, 18]
    blue_li = [5, 11, 16]
    kind = 6
    result = main_handle(red_li, blue_li, kind)

    print(result)

    # t = [sum(x) for x in Resu]  # 每一组数据求和,列表生成式
    # te = list(zip(Resu, t))  # zip返回的一组一组的元组
