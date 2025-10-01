
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'deploy/home.html')

def messages(request):
    return render(request, 'deploy/partials/messages.html')

def about(request):
    return render(request, 'deploy/partials/about.html')

def env_check(request):
    context = {
        'debug': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'static_url': settings.STATIC_URL,
    }
    return render(request, 'deploy/partials/env_check.html', context)

def static_test(request):
    return render(request, 'deploy/partials/static_test.html')

def health(request):
    return JsonResponse({'status': 'ok'})
