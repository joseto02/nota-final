from django.shortcuts import render, redirect

from tiendaZapatillasApp.models import Zapatilla

# Create your views here.

def gestion(request):
    listaZapatillas = Zapatilla.objects.all()
    
    return render(
        request, "administrador/gestion.html", {"zapatillas": listaZapatillas}
    )

def resgistrarZapatilla(request):
    marca = request.POST["txtMarca"]
    modelo = request.POST["txtModelo"]
    precio = request.POST["numPrecio"]

    zapatilla = Zapatilla.objects.create(
        marca=marca, modelo=modelo, precio=precio
    )

    return redirect("gestion")

def editarZapatilla(request, id_zapatilla):
    zapatilla = Zapatilla.objects.get(id_zapatilla=id_zapatilla)
    return render(request, "administrador/edicionZapatilla.html", {"zapatilla": zapatilla})


def edicionZapatilla(request):
    id_zapatilla = request.POST.get("id_zapatilla") 
    modelo = request.POST["txtModelo"]
    precio = request.POST["numPrecio"]

    zapatilla = Zapatilla.objects.get(id_zapatilla=id_zapatilla)
    zapatilla.modelo = modelo
    zapatilla.precio = precio
    zapatilla.save()
    return redirect("gestion")


def eliminarZapatilla(request, id_zapatilla):
    zapatilla = Zapatilla.objects.get(id_zapatilla = id_zapatilla )
    zapatilla.delete()

    return redirect("gestion")
