
from django.urls import path
from . import views

app_name = 'style'

urlpatterns = [
    path('', views.home, name='home'),
    path('card/', views.card, name='card'),
    path('alert/', views.alert, name='alert'),
]
