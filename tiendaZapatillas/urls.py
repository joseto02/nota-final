from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tiendaZapatillasApp.urls")),
    path("sesiones/", include("sesiones.urls")),
    path("productos/", include("productos.urls")),
]
