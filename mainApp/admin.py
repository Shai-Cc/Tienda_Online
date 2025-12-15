from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from .models import Categoria, Productos, Insumo, Pedido, Contacto
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
    list_display = ["es_destacado", "nombre","slug", "categoria", "descripcion", "precio_base", "vista_imagen1", "vista_imagen2", "vista_imagen3"]
    prepopulated_fields = {"slug": ["nombre"]}
    list_filter = ["categoria", "es_destacado"]
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

    @admin.action(description="Marcar productos seleccionados como Destacados")
    def marcar_destacado(self, request, queryset):
        queryset.update(es_destacado=True)

    @admin.action(description="Desmarcar productos seleccionados como Destacados")
    def desmarcar_destacado(self, request, queryset):
        queryset.update(es_destacado=False)

@admin.register(Insumo)
class InsumoAdmin (admin.ModelAdmin):
    list_display = ["nombre", "marca", "color", "cantidad", "unidad"]
    prepopulated_fields = {"slug": ["nombre"]}
    list_filter = ["tipo", "color",]
    search_fields = ["nombre", "marca"]


@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):
    list_display = ["id","fecha_pedido", "nombre_cliente", "producto_requerido", "cantidad_producto", "plataforma", "estado_pedido_actual", "estado_pago_actual",  "fecha_entrega"]
    list_filter = ["plataforma", "estado_pedido_actual", "estado_pago_actual"]
    search_fields = ["nombre_cliente", "producto_requerido", "fecha_pedido", "token_seguimiento"]
    readonly_fields = ["token_seguimiento", "fecha_pedido", "id"]
    ordering = ["-fecha_pedido"]

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
            "fields": ("producto_requerido", "cantidad_producto", "plataforma", "fecha_pedido", "fecha_entrega", "notas_adicionales"),
        }),
        ("Imágenes del Pedido", {
            "fields": ("pedido_img_1", "pedido_img_2", "pedido_img_3"),
        }),
        ('Estados del Pedido y Pago', {
            "fields": ("estado_pedido_actual", "estado_pago_actual",),
        }),
        ("Seguimiento", {
            "fields": ("token_seguimiento",),
        }),
    )
    @admin.action(description="Marcar pedidos seleccionados como En Proceso")
    def marcar_en_proceso(self, request, queryset):
        queryset.update(estado_pedido_actual='en_proceso')

    @admin.action(description="Marcar pedidos seleccionados como Aprobdado")
    def marcar_aprobado(self, request, queryset):
        queryset.update(estado_pedido_actual='aprobado')

    @admin.action(description="Marcar pedidos seleccionados como Realizada")
    def marcar_realizada(self, request, queryset):
        queryset.update(estado_pedido_actual='realizada')

    @admin.action(description="Marcar pedidos seleccionados como Entregados")
    def marcar_entregada(self, request, queryset):
        queryset.update(estado_pedido_actual='entregada')

    @admin.action(description="Marcar pedidos seleccionados como Pagados")
    def marcar_pagado(self, request, queryset):
        queryset.update(estado_pago_actual='pagado')

    @admin.action(description="Marcar pedidos seleccionados como Parcialmente Pagados")
    def marcar_parcial(self, request, queryset):
        queryset.update(estado_pago_actual='parcial')

    @admin.action(description="Marcar pedidos seleccionados como Pagado")
    def marcar_pagado(self, request, queryset):
        queryset.update(estado_pago_actual='pagado')

    @admin.action(description="Marcar pedidos seleccionados como Finalizado")
    def marcar_finalizado(self, request, queryset):
        ok = 0
        errores = 0
        for pedido in queryset:
            try:
                pedido.marcar_finalizado()
                ok += 1
            except ValidationError:
                errores += 1

        if ok:
            self.message_user(request, f"{ok} pedido(s) marcado(s) como finalizado(s).", messages.SUCCESS)

        if errores:
            self.message_user(request, f"{errores} pedido(s) no pudieron ser marcados como finalizado(s) debido a que no cumplen los requisitos.", messages.WARNING)
    
    actions = [marcar_en_proceso, marcar_aprobado, marcar_realizada, marcar_entregada, marcar_finalizado, marcar_parcial, marcar_pagado]

    bloquear_campos = ('nombre_cliente', 'correo_cliente', 'telefono_cliente', 'producto_requerido', 'cantidad_producto', 'plataforma', 'fecha_pedido', 'token_seguimiento')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.estado_pedido_actual in ['finalizada', 'cancelada']:
            return self.readonly_fields + self.bloquear_campos
        return self.readonly_fields
@admin.register(Contacto)    
class ContactoAdmin (admin.ModelAdmin):
    list_display = ["nombre", "correo", "telefono", "asunto", "fecha_envio", "respondido"]
    list_filter = ["respondido", "asunto"]
    search_fields = ["nombre", "correo", "mensaje", "fecha_envio"]
    readonly_fields = ["nombre", "correo", "telefono", "asunto", "mensaje", "fecha_envio"]
    ordering = ["-fecha_envio"]

    fieldsets = (
        ("Remitente", {
            "fields": ("nombre", "correo", "telefono"),
        }),
        ("Contenido", {
            "fields": ("asunto", "mensaje"),
        }),
        ("Estado", {
            "fields": ("fecha_envio", "respondido"),
        }),
    )     