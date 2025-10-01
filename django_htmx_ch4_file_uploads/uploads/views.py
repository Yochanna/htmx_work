from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm

def home(request):
    form = UploadForm()
    return render(request, "home.html", {"form": form})

def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            file_url = fs.url(filename)
            return render(request, "partials/upload_success.html", {
                "title": form.cleaned_data['title'],
                "file_url": file_url
            })
        return render(request, "partials/upload_form.html", {"form": form})
    else:
        form = UploadForm()
        return render(request, "partials/upload_form.html", {"form": form})
