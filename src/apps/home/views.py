from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/index.html"


def topics(request):
    return render(request, "home/topics.html")


def online(request):
    return render(request, "home/online.html")
