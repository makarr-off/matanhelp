from django.urls import path

from apps.onboarding.apps import OnboardingConfig
from apps.onboarding.views import IndexView

app_name = OnboardingConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]