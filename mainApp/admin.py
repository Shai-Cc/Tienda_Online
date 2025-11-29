from django.contrib import admin
from .models import Categoria, Productos, Insumo

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