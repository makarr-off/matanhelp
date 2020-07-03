from django.urls import path

from apps.about import views

urlpatterns = [
    path("", views.about, name="about"),
]
