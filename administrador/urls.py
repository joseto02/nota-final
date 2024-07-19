from django.urls import path
from . import views

urlpatterns = [
    path("gestion", views.gestion, name="gestion"),
    path("resgistrarZapatilla/", views.resgistrarZapatilla, name="registrar_zapatilla"),
    path("eliminarZapatilla/<id_zapatilla>", views.eliminarZapatilla, name="eliminar_zapatilla"),
    path("editarZapatilla/<id_zapatilla>", views.editarZapatilla, name="editar_zapatilla"),
    path("edicionZapatilla/", views.edicionZapatilla, name="edicion_zapatilla"),
]
