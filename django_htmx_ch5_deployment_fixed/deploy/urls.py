
from django.urls import path
from . import views

app_name = 'deploy'

urlpatterns = [
    path('', views.home, name='home'),
    path('messages/', views.messages, name='messages'),
    path('about/', views.about, name='about'),
    path('env/', views.env_check, name='env_check'),
    path('static-test/', views.static_test, name='static_test'),
    path('health/', views.health, name='health'),
]
