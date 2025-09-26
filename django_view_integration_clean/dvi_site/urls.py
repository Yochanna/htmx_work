from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("admin/", admin.site.urls),
    # Clean root: redirect to /items/
    path("", RedirectView.as_view(url="/items/", permanent=False)),
    # Favicon to avoid noisy 404s
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"), permanent=False)),
    path("", include("pages.urls")),
]
