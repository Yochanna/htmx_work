from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("greeting/", views.greeting, name="greeting"),
    path("quote/", views.quote, name="quote"),
]
