from django.shortcuts import render
from django.db.models import Q

from mainApp.models import Categoria, Productos, Insumo, Pedido
from mainApp.forms import FormularioPedido

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos,
    }
    return render(request, 'home.html', data)

def catalogo(request):
    categorias = Categoria.objects.all()
    productos = Productos.objects.all()

    categoria_slug = request.GET.get('categoria')
    busqueda = request.GET.get('q')
    if categoria_slug:
        productos = productos.filter(categoria__slug=categoria_slug)
    if busqueda:
        productos = productos.filter(Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda))

    data = {
        'categorias': categorias,
        'productos': productos,
        'categoria_seleccionada': categoria_slug,
        'busqueda': busqueda,
    }
    return render(request, 'catalogo.html', data)

def detalle_producto(request, slug):
    producto = Productos.objects.get(slug=slug)
    data = {
        'producto': producto,
    }
    return render(request, 'detalle_producto.html', data)

def realizar_pedido(request):
    if request.method == 'POST':
        form = FormularioPedido(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.plataforma = 'Web'
            pedido.estado_pedido_actual = 'solicitado'
            pedido.estado_pago_actual = 'pendiente'
            pedido.save()

            return render(request, 'confirmacion_pedido.html', {'pedido': pedido})
        
    else:
        form = FormularioPedido()

    return render(request, 'pedido_web.html', {'form': form})
            