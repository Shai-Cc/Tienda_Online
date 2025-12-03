from django.contrib import admin
from .models import Categoria, Productos, Insumo, Pedido
from django.utils.html import format_html


# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    prepopulated_fields = {"slug": ["nombre"]}
    search_fields = ["nombre"]
    fieldsets = (
        ("Información de la Categoría", {
            'fields': ('nombre', 'slug', 'descripcion'),
        }),
    )

@admin.register(Productos)
class ProductosAdmin (admin.ModelAdmin):
    list_display = ["nombre","slug", "categoria", "descripcion", "precio_base", "vista_imagen1", "vista_imagen2", "vista_imagen3"]
    prepopulated_fields = {"slug": ["nombre"]}
    list_filter = ["categoria",]
    search_fields = ["nombre",]

    def vista_imagen1(self, obj):
        if obj.imagen1:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen1.url)
        return "-"
    
    def vista_imagen2(self, obj):
        if obj.imagen2:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen2.url)
        return "-"
    
    def vista_imagen3(self, obj):
        if obj.imagen3:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen3.url)
        return "-"

    fieldsets = (
        ("Información del Producto", {
            'fields': ('nombre', 'slug', 'categoria', 'descripcion', 'precio_base'),
        }),
        ("Imágenes del Producto", {
            'fields': ('imagen1', 'imagen2', 'imagen3'),
        }),
    )

@admin.register(Insumo)
class InsumoAdmin (admin.ModelAdmin):
    list_display = ["nombre", "marca", "color", "cantidad", "unidad"]
    prepopulated_fields = {"slug": ["nombre"]}
    list_filter = ["tipo", "color",]
    search_fields = ["nombre", "marca"]


@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):
    list_display = ["nombre_cliente", "producto_requerido", "cantidad_producto", "plataforma", "estado_pedido_actual", "estado_pago_actual", "fecha_pedido", "fecha_entrega"]
    list_filter = ["plataforma", "estado_pedido_actual", "estado_pago_actual"]
    search_fields = ["nombre_cliente", "producto_requerido", "fecha_pedido"]
    readonly_fields = ["token_seguimiento", "fecha_pedido"]
    order = ["-fecha_pedido"]

    def vista_pedido_img_1(self, obj):
        if obj.pedido_img_1:
            return format_html('<img src="{}" width="100" height="100" />', obj.pedido_img_1.url)
        return "-"
    
    def vista_pedido_img_2(self, obj):
        if obj.pedido_img_2:
            return format_html('<img src="{}" width="100" height="100" />', obj.pedido_img_2.url)
        return "-"
    
    def vista_pedido_img_3(self, obj):
        if obj.pedido_img_3:
            return format_html('<img src="{}" width="100" height="100" />', obj.pedido_img_3.url)
        return "-"

    fieldsets = (
        ("Información del Cliente", {
            "fields": ("nombre_cliente", "correo_cliente", "telefono_cliente"),
        }),
        ("Detalle del Pedido", {
            "fields": ("producto_requerido", "cantidad_producto", "plataforma", "estado_pedido_actual", "estado_pago_actual", "fecha_pedido", "fecha_entrega", "notas_adicionales"),
        }),
        ("Imágenes del Pedido", {
            "fields": ("pedido_img_1", "pedido_img_2", "pedido_img_3"),
        }),
        ("Seguimiento", {
            "fields": ("token_seguimiento",),
        }),
    )

    @admin.action(description="Marcar pedidos seleccionados como En Proceso")
    def marcar_en_proceso(self, request, queryset):
        queryset.update(estado_pedido_actual='en_proceso')

    @admin.action(description="Marcar pedidos seleccionados como Entregados")
    def marcar_entregada(self, request, queryset):
        queryset.update(estado_pedido_actual='entregada')

    @admin.action(description="Marcar pedidos seleccionados como Finalizado")
    def marcar_finalizado(self, request, queryset):
        queryset.update(estado_pedido_actual='finalizado')

    @admin.action(description="Marcar pedidos seleccionados como Pagados")
    def marcar_pagado(self, request, queryset):
        queryset.update(estado_pago_actual='pagado')

    actions = [marcar_en_proceso, marcar_entregada, marcar_finalizado, marcar_pagado]