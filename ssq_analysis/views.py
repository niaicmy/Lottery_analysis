from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from data_handle.SpiderMain import parser
from data_handle.MainHandle import main_handle
from .models import SsqInfo, SsqOrig

# import time

# Create your views here.
lt10 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
gt10 = [str(i) for i in range(10, 34)]
head = lt10 + gt10
# blue = [str(i) for i in range(10, 17)]

# app 所有的匹配模式
models = ["red", "blue", "orig"]

# 初始化 设置全局的 ssq_info 避免每次调用ssq 需要查询数据库 调用 update 后要更新
# ssq_ info 包括了数据库的全部内容
ssq_info_all = SsqInfo.objects.all().values_list()
# QuerySet [(17001, 6, 2, 5, 4, 4, 3, 1, 2, 1, 10, 0, 9, 4, 0, 8, 1, 8, 7, 9, 0, 4, 2, 5, 1, 0, 0, 10, 7, 1, 6, 7, 5, 3,
# 24, 23, 15, 35, 4, 1, 2, 32, 33, 8, 51, 7, 11, 17, 0, 27), (17002, 7, 3, 6, 5, 5, 4, 2, 3, 2, 11, 1, 10, 5, 1, 0, 2,
# 9, 8,0, 1, 5, 3, 0, 0, 0, 1, 11, 8, 2, 7, 8, 0, 4, 25, 24, 0, 36, 5, 2, 3, 33, 34, 9, 52, 8, 12, 18, 1, 28), .....]
# print("ssq_info_all is :{}".format(ssq_info_all))

# 初始化 设置全局的 ssq_num 避免每次调用ssq 需要查询数据库 调用 update 后要更新
ssq_orig_all = SsqOrig.objects.all().values_list()
# QuerySet [(17001, '09', '11', '14', '20', '25', '26', '15'), (17002, '15', '19', '23', '24', '25', '32', '03'),....]
# print("ssq_num_all is :{}".format(ssq_num_all))
# print("ssq_num_last is :{}".format(ssq_num_all[len(ssq_num_all)-1]))
# print("ssq_num_last_number is :{}".format(ssq_num_all[len(ssq_num_all) - 1][0]))

# 以下是分页机制 ================================================
# page_limit : 每一页显示数据量
page_limit = 15


# page_limit = 2


def get_page_total():
    #  divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
    page_tem = divmod(len(ssq_info_all), page_limit)

    if page_tem[1]:
        _page_total = page_tem[0] + 1
    else:
        _page_total = page_tem[0]

    return list(range(1, _page_total + 1))


# 初始化 设置全局的 page_total
page_total = get_page_total()


# print(page_total)


def show_page(current_page, show_dec=2):
    page_list = list(range(current_page - show_dec, current_page + show_dec + 1))
    # print(page_list)
    # 列表反向遍历 正向 删除有问题
    for p in page_list[::-1]:
        if p not in page_total:
            page_list.remove(p)
    # print(page_list)
    return page_list


# ===========================================================
def index(request):
    return render(request, "index.html")


def update(request):
    global ssq_orig_all, ssq_info_all, page_total
    # 17155 -- 18001
    message = "Update fail !"
    # 最先更新 proxy
    parser("proxy", 1)
    # ssq_num 代表开奖期数
    # ssq_num = ssq_num_all[len(ssq_num_all) - 1][0]
    ssq_num = ssq_orig_all[0][0]
    # print(ssq_num)
    # ssq_num = SsqOrig.objects.values("number").last()
    # print(ssq_num)
    # count 是计算 lottery 失败次数
    count = 0
    # ssq_info = list(SsqInfo.objects.all().values_list())
    # print(ssq_info)

    while ssq_num:
        ssq_num += 1
        lottery = parser("lottery", ssq_num)

        # +++++++++++
        # 测试用
        # print(ssq_num)
        if ssq_num == 17032:
            break
        # +++++++++++++

        # ==========解析数据内容============
        if lottery:
            # print("data coming ...")
            # SsqOrig 数据表的更新
            # 计算全部的 奇偶比  和值
            m_odd = 0
            m_even = 0
            m_sum = 0
            for i in lottery:
                if i in lt10:
                    m_sum += int(i[1])
                    if int(i[1]) % 2 == 0:
                        m_even += 1
                    else:
                        m_odd += 1
                else:
                    m_sum += int(i)
                    if int(i) % 2 == 0:
                        m_even += 1
                    else:
                        m_odd += 1

            dic = {'number': ssq_num, 'red1': lottery[0], 'red2': lottery[1], 'red3': lottery[2], 'red4': lottery[3],
                   'red5': lottery[4], 'red6': lottery[5], 'blue': lottery[6],
                   'mparity': (str(m_odd) + ":" + str(m_even)), 'mtotal': str(m_sum)}

            SsqOrig.objects.create(**dic)

            # =================================================
            # SsqInfo 数据表的更新
            # 构造一个dic2 存放 SsqInfo 一行的数据
            dic2 = {"number": ssq_num}
            # 取出最新的SsqInfo
            ssq_info_last = list(SsqInfo.objects.all().values_list().first())
            # print(ssq_info_last)
            # 更新红球计数
            ind = 1
            for x in head:
                if x in lottery[0:6]:
                    dic2["red" + x] = 0
                else:
                    dic2["red" + x] = ssq_info_last[ind] + 1
                ind += 1

            # 更新蓝球计数
            ind = 1
            for x in head[:16]:
                if x == lottery[6]:
                    dic2["blue" + x] = 0
                else:
                    dic2["blue" + x] = ssq_info_last[33 + ind] + 1
                ind += 1

            # print(dic2)
            SsqInfo.objects.create(**dic2)

        else:
            count += 1
            if count == 2:
                ssq_num = (ssq_num - (ssq_num % 1000)) + 1000
            elif count == 3:
                message = "The data is the latest !"
                break

    # 跳转加反向解析
    # https://docs.djangoproject.com/zh-hans/2.0/ref/contrib/messages/
    # 底层调用 add_message(request, constants.SUCCESS, message, extra_tags=extra_tags,fail_silently=fail_silently)
    # messages.success(request, "Your data has been saved!")
    messages.success(request, message, extra_tags="text-danger")

    # 最后使用最新数据
    # global ssq_num_all, ssq_info_all, page_total
    ssq_info_all = SsqInfo.objects.all().values_list()
    ssq_orig_all = SsqOrig.objects.all().values_list()
    page_total = get_page_total()

    return HttpResponseRedirect(reverse("ssq", args=["red", 1]))


# 设置 model 来切换显示
def ssq(request, model, page):
    # time.sleep(2)

    if page > page_total[-1] or (model not in models):
        # print("page full ...")
        raise Http404("Page Index Out Of Range. !")

    data = dict()
    orig = []
    info = []
    data["head"] = head
    # 设置一个标志位 来分辨 red (1) 或 blue (2)
    data["mark"] = 1
    # data["head"] = []
    data["page_info"] = {"show_page": show_page(page), "current_page": page}
    # data["page_info"] = [show_page(page), page]
    # print(data["page_info"])
    # type 设置显示红球还是篮球
    # data["type"] = True
    # print(model)
    # red 1-33 [1:34]
    # (17001, 6, 2, 5, 4, 4, 3, 1, 2, 1, 10, 0, 9, 4, 0, 8, 1, 8, 7, 9, 0, 4, 2, 5, 1, 0, 0, 10, 7, 1, 6, 7, 5, 3,
    # blue 34-49 [34:50]
    # 24, 23, 15, 35, 4, 1, 2, 32, 33, 8, 51, 7, 11, 17, 0, 27)
    # page * page_limit 不能超过 ssq_info_all 的最大长度
    if "orig" == model:
        if page * page_limit <= len(ssq_orig_all):
            orig = list(ssq_orig_all)[(page - 1) * page_limit:page * page_limit]
        else:
            orig = list(ssq_orig_all)[(page - 1) * page_limit:len(ssq_info_all)]

        # print(orig)
    else:
        if page * page_limit <= len(ssq_info_all):
            info = list(ssq_info_all)[(page - 1) * page_limit:page * page_limit]
        else:
            info = list(ssq_info_all)[(page - 1) * page_limit:len(ssq_info_all)]

    # print(info)
    # print(type(info))
    data["records"] = []
    # data["records"] = [("18001", 1, 2, 3, 6, 9), ("18002", 0, 3, 0), ("18003", 11, 3, 0)]
    # tempinfo = []
    if "blue" == model:
        data["mark"] = 2
        for i in info:
            # print(type(i[0]))
            # 注意这个元组的坑 int TypeError: 'int' object is not iterable
            t = (i[0],) + i[34:50]
            data["records"].append(t)

    elif "red" == model:
        data["mark"] = 1
        for p in info:
            # print(type(p[0]))
            t2 = (p[0],) + p[1:34]
            data["records"].append(t2)

    elif "orig" == model:
        data["mark"] = 3
        data["records"] = orig

    # print(tempinfo)
    # data["records"] = tempinfo
    # =======================以下是显示原始数据======================================
    # sp = SsqOrig.objects.all().values_list()
    # print(sp)
    # print(data)
    return render(request, "ssq.html", context=data)
    # return render(request, "ssq.html", {
    #     "records": "",
    #     "num": "",
    # })


# todo: 显示最后的数据 要 转换字符串 数字
def composite_data(request):
    data = dict(request.POST)
    # print(data)

    result = dict()
    result["head"] = head

    # 取出提交的数据
    red_t = data.get("red", None)
    blue_t = data.get("blue", None)
    s_sum = data.get("ssum", None)
    m_sum = data.get("msum", None)

    red_list = []
    blue_list = []
    # print(red_t)
    # print(blue_t)

    for i in red_t:
        if i in lt10:
            red_list.append(int(i[1]))
        else:
            red_list.append(int(i))

    for i in blue_t:
        if i in lt10:
            blue_list.append(int(i[1]))
        else:
            blue_list.append(int(i))

    handled = main_handle(red_list, blue_list)
    # print(handled)

    result["records"] = handled

    # return HttpResponse(None)
    return render(request, "compdata.html", context=result)


def search(request):
    return HttpResponse(None)


# def page_not_found(request):
#     return render(request, '404.html')
#
#
# def page_error(request):
#     return render(request, '500.html')
#
#
# def permission_denied(request):
#     return render(request, '403.html')
