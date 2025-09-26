from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    if getattr(request, "htmx", False):
        return render(request, "pages/partials/item_list.html", {"items": items})
    return render(request, "pages/items.html", {"items": items})

def item_fragment(request):
    items = Item.objects.all()
    return render(request, "pages/partials/item_list.html", {"items": items})
