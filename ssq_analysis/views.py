from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from data_collection.SpiderMain import parser
from .models import SsqInfo, SsqNum

# Create your views here.
lt10 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
red = [str(i) for i in range(10, 34)]
blue = [str(i) for i in range(10, 17)]


def index(request):
    return render(request, "index.html")


def update(request):
    # 17155 -- 18001
    message = "Update fail !"
    # 最先更新 proxy
    parser("proxy", 1)
    ssq_num = SsqNum.objects.values("number").last()
    # print(ssq_num)
    num = dict(ssq_num)["number"]
    # count 是计算 lottery 失败次数
    count = 0
    # ssq_info = list(SsqInfo.objects.all().values_list())
    # print(ssq_info)

    while num:
        num += 1
        lottery = parser("lottery", num)

        # +++++++++++
        # 测试用
        # print(num)
        if num == 17005:
            break
        # +++++++++++++

        # ==========解析数据内容============
        if lottery:
            # print("data coming ...")
            # SsqNum 数据表的更新
            dic = {'number': num, 'red1': lottery[0], 'red2': lottery[1], 'red3': lottery[2], 'red4': lottery[3],
                   'red5': lottery[4], 'red6': lottery[5], 'blue': lottery[6]}
            SsqNum.objects.create(**dic)
            # =================================================
            # SsqInfo 数据表的更新
            # 构造一个dic2 存放 SsqInfo 一行的数据
            dic2 = {"number": num}
            # 取出最新的SsqInfo
            ssq_info = list(SsqInfo.objects.all().values_list().last())
            # print(ssq_info)
            # 更新红球计数
            ind = 1
            for x in (lt10 + red):
                if x in lottery[0:6]:
                    dic2["red" + x] = 0
                else:
                    dic2["red" + x] = ssq_info[ind] + 1
                ind += 1

            # 更新蓝球计数
            ind = 1
            for x in (lt10 + blue):
                if x == lottery[6]:
                    dic2["blue" + x] = 0
                else:
                    dic2["blue" + x] = ssq_info[33 + ind] + 1
                ind += 1

            # print(dic2)
            SsqInfo.objects.create(**dic2)

        else:
            count += 1
            if count == 2:
                num = (num - (num % 1000)) + 1000
            elif count == 3:
                message = "The data is the latest !"
                break

    # 跳转加反向解析
    # https://docs.djangoproject.com/zh-hans/2.0/ref/contrib/messages/
    # 底层调用 add_message(request, constants.SUCCESS, message, extra_tags=extra_tags,fail_silently=fail_silently)
    # messages.success(request, "Your data has been saved!")
    messages.success(request, message, extra_tags="text-danger")
    return HttpResponseRedirect(reverse("ssq", args=["red"]))


# 设置 model 来切换显示
def ssq(request, model, page):
    data = dict()
    data["num"] = None
    # type 设置显示红球还是篮球
    # data["type"] = True
    # print(model)
    # red 1-33 [1:34]
    # (17001, 6, 2, 5, 4, 4, 3, 1, 2, 1, 10, 0, 9, 4, 0, 8, 1, 8, 7, 9, 0, 4, 2, 5, 1, 0, 0, 10, 7, 1, 6, 7, 5, 3,
    # blue 34-49 [34:50]
    # 24, 23, 15, 35, 4, 1, 2, 32, 33, 8, 51, 7, 11, 17, 0, 27)
    info = list(SsqInfo.objects.all().values_list())
    # print(info)
    # print(type(info))
    data["records"] = []
    # data["records"] = [("18001", 1, 2, 3, 6, 9), ("18002", 0, 3, 0), ("18003", 11, 3, 0)]
    # tempinfo = []
    if "blue" == model:
        data["num"] = lt10 + blue
        for i in info:
            # print(type(i[0]))
            # 注意这个元组的坑 int TypeError: 'int' object is not iterable
            t = (i[0],) + i[34:50]
            data["records"].append(t)

    elif "red" == model:
        data["num"] = lt10 + red
        for p in info:
            # print(type(p[0]))
            t2 = (p[0],) + p[1:34]
            data["records"].append(t2)

    # print(tempinfo)
    # data["records"] = tempinfo
    # =======================以下是显示原始数据======================================
    # sp = SsqNum.objects.all().values_list()
    # print(sp)
    return render(request, "ssq.html", context=data)
    # return render(request, "ssq.html", {
    #     "records": "",
    #     "num": "",
    # })


def search(request):
    return HttpResponse(None)
