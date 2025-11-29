from django.contrib import admin
from .models import Categoria, Productos

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ["nombre",]

@admin.register(Productos)
class ProductosAdmin (admin.ModelAdmin):
    list_display = ["nombre",]