from django.urls import path
from . import views
from apps.home.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("Topics/", views.topics, name="topics"),
    path("Online/", views.online, name="online"),
]
