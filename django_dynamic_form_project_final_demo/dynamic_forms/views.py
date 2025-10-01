from django.shortcuts import render
from django.http import HttpResponse
from .forms import RoleForm, StudentForm, TeacherForm, TopicForm
from .models import Student, Teacher, TopicSubmission


def dynamic_form_view(request):
    return render(request, "dynamic_forms/dynamic_form.html", {"form": RoleForm()})


def load_form_fields(request):
    role = request.GET.get("role")
    form = None
    if role == "student":
        form = StudentForm()
    elif role == "teacher":
        form = TeacherForm()
    return render(request, "dynamic_forms/partial_form.html", {"form": form, "role": role})


def load_topics(request):
    subject = request.GET.get("subject")
    form = TopicForm(subject=subject)
    return render(request, "dynamic_forms/partial_topics.html", {
        "form": form,
        "subject": subject
    })


def submit_form(request):
    if request.method == "POST":
        role = request.POST.get("role")
        form = None

        if role == "student":
            form = StudentForm(request.POST)
            if form.is_valid():
                Student.objects.create(
                    name=form.cleaned_data["name"],
                    student_id=form.cleaned_data["student_id"]
                )
                return HttpResponse("<div class='alert alert-success'>✅ Student saved successfully!</div>")

        elif role == "teacher":
            if "topic" in request.POST:
                subject = request.POST.get("subject")
                form = TopicForm(subject=subject, data=request.POST)
                if form.is_valid():
                    teacher = Teacher.objects.create(
                        name=request.POST.get("name"),
                        subject=request.POST.get("subject")
                    )
                    TopicSubmission.objects.create(
                        teacher=teacher,
                        topic=form.cleaned_data["topic"]
                    )
                    return HttpResponse("<div class='alert alert-success'>✅ Teacher & Topic saved successfully!</div>")
            else:
                form = TeacherForm(request.POST)

        return render(request, "dynamic_forms/partial_form.html", {"form": form, "role": role})
