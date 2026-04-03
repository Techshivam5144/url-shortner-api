from django.urls import path
from .views import ShortenUrlView,RedirectView,UrlView

urlpatterns = [

    path("api/shorten/",ShortenUrlView.as_view()),
    path("api/urls/",UrlView.as_view()),
    path("<str:shortcode>/",RedirectView.as_view()),
]
