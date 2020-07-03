from django.urls import path

from apps.comments import views

urlpatterns = [
    path("", views.comments, name="comments"),
]
