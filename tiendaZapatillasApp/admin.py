from django.contrib import admin
from .models import Cliente, Zapatilla, Marca, Modelo_zapatilla, Compra, DetalleCompra

from contacto.models import Contacto
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Zapatilla)
admin.site.register(Marca)

admin.site.register(Contacto)
