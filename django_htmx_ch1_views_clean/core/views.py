from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest):
    return render(request, "home.html")

def hello(request: HttpRequest):
    if request.headers.get("HX-Request"):
        return render(request, "partials/hello.html")
    return render(request, "home.html")

def bye(request: HttpRequest):
    if request.headers.get("HX-Request"):
        return render(request, "partials/bye.html")
    return render(request, "home.html")
