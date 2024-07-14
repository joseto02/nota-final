from django.shortcuts import render

# Create your views here.

def productos(request):
    context ={}
    return render(request, 'productos/productos.html', context)


def marca_adidas(request):
    context = {}
    return render(request, "productos/marca_adidas.html", context)

def nike(request):
    context = {}
    return render(request, "productos/nike.html", context)

def puma(request):
    context = {}
    return render(request, "productos/puma.html", context)