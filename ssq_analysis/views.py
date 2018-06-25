from django.shortcuts import render, HttpResponse
from data_collection.SpiderMain import parser
from .models import SsqInfo, SsqNum
# Create your views here.


def index(request):
    return render(request, "index.html")


lt10 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
red = [str(i) for i in range(10, 34)]
blue = [str(i) for i in range(10, 17)]


def update(request):
    # todo: update data 不知道取的值是不是最新的
    # 17155 -- 18001
    num = SsqNum.objects.order_by("number")[0] + 1
    count = 0
    print(num)

    while num:
        lottery = parser("Httpconfig.json", "lottery", num)
        if lottery:
            ssqtem = SsqNum()
            ssqtem.number = num
            ssqtem.red1 = lottery[0]
            ssqtem.red2 = lottery[1]
            ssqtem.red3 = lottery[2]
            ssqtem.red4 = lottery[3]
            ssqtem.red5 = lottery[4]
            ssqtem.red6 = lottery[5]
            ssqtem.red7 = lottery[6]
            ssqtem.save()
        else:
            count += 1
            if count == 2:
                num = (num - (num % 1000)) + 1000
                count += 1
            elif count == 3:
                break

            num += 1

    proxy = parser("Httpconfig.json", "proxy", 1)


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
