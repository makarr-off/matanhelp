from django.shortcuts import render

from apps.about.models import Technology


def about(request):
    return render(request, "about/index.html", context={
        "technologies": Technology.objects.all(),
    })
