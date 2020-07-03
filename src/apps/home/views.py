from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def topics(request):
    return render(request, "home/topics.html")


def online(request):
    return render(request, "home/online.html")
