from django.urls import path
from . import views

urlpatterns = [
    path('', views.dynamic_form_view, name="dynamic-form"),
    path('load-form/', views.load_form_fields, name="load-form"),
    path('load-topics/', views.load_topics, name="load-topics"),
    path('submit-form/', views.submit_form, name="submit-form"),
]
