
from django.shortcuts import render

def home(request):
    return render(request, 'style/home.html')

def card(request):
    return render(request, 'style/partials/card.html')

def alert(request):
    return render(request, 'style/partials/alert.html')
