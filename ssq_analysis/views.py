from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def ssq(request):
    return render(request, "ssq.html")
