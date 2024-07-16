from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tiendaZapatillasApp.urls")),
    path("productos/", include("productos.urls")),
    path("autenticacion/", include("autenticacion.urls")),
    path("contacto/", include("contacto.urls")),
]
