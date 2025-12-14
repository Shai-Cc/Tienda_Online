from django.shortcuts import render
from django.db.models import Q

from mainApp.models import Categoria, Productos, Insumo, Pedido
from mainApp.forms import FormularioPedido, SeguimientoPedidoForm

# Create your views here.

def home(request):
    destacados = Productos.objects.filter(es_destacado=True)[:8]
    return render(request, "home.html", {"destacados": destacados})


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

def seguimiento_pedido(request):
    pedido = None
    token_ingresado = None
    error = None

    if request.method == 'POST':
        form = SeguimientoPedidoForm(request.POST)
        if form.is_valid():
            token_ingresado = form.cleaned_data['token_seguimiento']
            try:
                pedido = Pedido.objects.get(token_seguimiento=token_ingresado)
            except Pedido.DoesNotExist:
                error = "No se encontró ningún pedido con ese número de seguimiento."

    else:
            form = SeguimientoPedidoForm()

    data = {
        'form': form,
        'pedido': pedido,
        'token_ingresado': token_ingresado,
        'error': error,
    }
    return render(request, 'seguimiento_pedido.html', data)
            