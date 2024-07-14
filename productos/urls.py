from django.urls import path
from . import views

urlpatterns = [
    path("productos", views.productos, name="productos"),
    path("marca_adidas", views.marca_adidas, name="marca_adidas"),
    path("nike", views.nike, name="nike"),
    path("puma", views.puma, name="puma"),
]
