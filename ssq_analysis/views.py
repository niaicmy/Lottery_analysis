from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from data_collection.SpiderMain import parser
from .models import SsqInfo, SsqNum

# Create your views here.


def index(request):
    return render(request, "index.html")


lt10 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
red = [str(i) for i in range(10, 34)]
blue = [str(i) for i in range(10, 17)]


def update(request):
    # 17155 -- 18001
    message = ""
    sp = SsqNum.objects.values("number").last()
    num = dict(sp)["number"]
    count = 0

    while num:
        num += 1
        lottery = parser("lottery", num)
        if lottery:
            # print("data coming ...")
            dic = {'number': num, 'red1': lottery[0], 'red2': lottery[1], 'red3': lottery[2], 'red4': lottery[3],
                   'red5': lottery[4], 'red6': lottery[5], 'blue': lottery[6]}
            SsqNum.objects.create(**dic)
        else:
            count += 1
            if count == 2:
                num = (num - (num % 1000)) + 1000
            elif count == 3:
                message = "The data is the latest !"
                break
    # 更新 proxy
    parser("proxy", 1)
    # 跳转加反向解析
    # todo: https://docs.djangoproject.com/zh-hans/2.0/ref/contrib/messages/
    messages.success(request, "Your data has been saved!")
    messages.success(request, "The data is the latest !")
    return HttpResponseRedirect(reverse("ssq", args=["red"]))


# 设置 model 来切换显示
def ssq(request, model):
    data = dict()
    # type 设置显示红球还是篮球
    data["type"] = True
    data["num"] = None
    # print(model)

    data["records"] = [("18001", 1, 2, 3, 6, 9), ("18002", 0, 3, 0), ("18003", 11, 3, 0)]

    if "blue" == model:
        data["num"] = lt10 + blue
    elif "red" == model:
        data["num"] = lt10 + red

    return render(request, "ssq.html", context=data)
    # return render(request, "ssq.html", {
    #     "records": "",
    #     "num": "",
    # })


def search(request):
    return HttpResponse(None)
