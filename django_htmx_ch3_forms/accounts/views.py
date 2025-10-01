from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignupStepOneForm, SignupStepTwoForm

def signup_step_one(request):
    form = SignupStepOneForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            request.session["signup_data"] = form.cleaned_data
            return render(request, "accounts/signup_step_two.html",
                          {"form": SignupStepTwoForm()})
    return render(request, "accounts/signup_step_one.html", {"form": form})

def signup_step_two(request):
    form = SignupStepTwoForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = request.session.pop("signup_data", {})
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
            )
            return render(request, "accounts/signup_success.html", {"user": user})
    return render(request, "accounts/signup_step_two.html", {"form": form})
