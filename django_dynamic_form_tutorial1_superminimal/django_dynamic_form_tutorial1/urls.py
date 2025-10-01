from django.contrib import admin
from django.urls import path
from formsdemo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
]
