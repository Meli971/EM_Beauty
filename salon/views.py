from django.shortcuts import render
from .models import Servicio, Estilista, Producto, Sucursal


def inicio(request):
    return render(request, 'salon/inicio.html')


def nosotros(request):
    return render(request, 'salon/nosotros.html')


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'salon/servicios.html', {'servicios': servicios})


def estilistas(request):
    estilistas = Estilista.objects.all()
    return render(request, 'salon/estilistas.html', {'estilistas': estilistas})


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'salon/productos.html', {'productos': productos})


def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'salon/sucursales.html', {'sucursales': sucursales})
# Create your views here.
