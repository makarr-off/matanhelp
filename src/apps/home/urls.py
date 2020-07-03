from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Topics/", views.topics, name="topics"),
    path("Online/", views.online, name="online"),
]
