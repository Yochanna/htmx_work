from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, "home.html", {"tasks": tasks})

def add_task(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")
    title = request.POST.get("title", "").strip()
    if title:
        Task.objects.create(title=title)
    tasks = Task.objects.all().order_by('-id')
    return render(request, "partials/task_list.html", {"tasks": tasks})

def mark_done(request, task_id):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    tasks = Task.objects.all().order_by('-id')
    return render(request, "partials/task_list.html", {"tasks": tasks})
