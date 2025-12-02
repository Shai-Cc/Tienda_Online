from django.shortcuts import render

from mainApp.models import Categoria, Productos, Insumo, Pedido

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos,
    }
    return render(request, 'home.html', data)

def detalle_producto(request, slug):
    producto = Productos.objects.get(slug=slug)
    data = {
        'producto': producto,
    }
    return render(request, 'detalle_producto.html', data)