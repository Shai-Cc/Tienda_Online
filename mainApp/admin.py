from django.contrib import admin
from .models import Categoria, Productos, Insumo, Pedido

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    prepopulated_fields = {"slug": ["nombre"]}

@admin.register(Productos)
class ProductosAdmin (admin.ModelAdmin):
    list_display = ["nombre","slug", "categoria", "descripcion", "precio_base", "imagen1", "imagen2", "imagen3"]
    prepopulated_fields = {"slug": ["nombre"]}

@admin.register(Insumo)
class InsumoAdmin (admin.ModelAdmin):
    list_display = ["nombre", "marca", "color", "cantidad", "unidad"]

@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):
    list_display = ["nombre_cliente", "producto_requerido", "cantidad_producto", "plataforma", "estado_pedido_actual", "estado_pago_actual", "fecha_pedido", "fecha_entrega"]
    