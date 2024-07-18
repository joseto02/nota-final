from django.shortcuts import render, redirect

from carrito.models import Producto
from carrito.Carrito import Carrito
# Create your views here.

def carro(request):
    productos = Producto.objects.all()
    return render(request, 'carrito/carro.html', {'productos' : productos })

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar(producto)
    return redirect("carro")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.eliminar(producto)
    return redirect("carro")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carro")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro")