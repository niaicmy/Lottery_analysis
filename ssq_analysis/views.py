from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


lt10 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
red = [str(i) for i in range(10, 34)]
blue = [str(i) for i in range(10, 17)]


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


def search(request):
    return HttpResponse(None)
