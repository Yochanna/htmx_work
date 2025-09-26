from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("items/", views.item_list, name="item_list"),
    path("items/fragment/", views.item_fragment, name="item_fragment"),
]
