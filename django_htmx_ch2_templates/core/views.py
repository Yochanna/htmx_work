from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def greeting(request):
    if request.headers.get("HX-Request"):
        return render(request, "partials/greeting.html")
    return render(request, "home.html")

def quote(request):
    if request.headers.get("HX-Request"):
        return render(request, "partials/quote.html")
    return render(request, "about.html")
