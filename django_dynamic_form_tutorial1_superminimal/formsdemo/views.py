from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, "formsdemo/success.html", {"name": form.cleaned_data["name"]})
        return render(request, "formsdemo/contact_form.html", {"form": form})
    form = ContactForm()
    return render(request, "formsdemo/contact_form.html", {"form": form})
