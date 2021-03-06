from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.home.urls")),
    path("admin/", admin.site.urls),
    path("Comments/", include("apps.comments.urls")),
    path("About/", include("apps.about.urls")),
]
