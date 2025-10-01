from django.urls import path
from . import views

urlpatterns = [
    path("signup/step-one/", views.signup_step_one, name="signup_step_one"),
    path("signup/step-two/", views.signup_step_two, name="signup_step_two"),
]
