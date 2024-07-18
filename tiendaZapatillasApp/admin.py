from django.contrib import admin
from .models import Cliente, Zapatilla, Marca, Modelo_zapatilla, Compra, DetalleCompra

from contacto.models import Contacto

from carrito.models import Producto
# Register your models here.

# Modelos de la app principal
admin.site.register(Cliente)
admin.site.register(Zapatilla)
admin.site.register(Marca)
admin.site.register(Modelo_zapatilla)
admin.site.register(Compra)
admin.site.register(DetalleCompra)

# Modelos de la app contacto
admin.site.register(Contacto)

#Modelos del carrito
admin.site.register(Producto)
