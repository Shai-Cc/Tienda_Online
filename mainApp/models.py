from django.db import models
import uuid
from django.core.exceptions import ValidationError

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=130, unique=True, null=True)
    descripcion = models.TextField (blank=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length= 120)
    slug = models.SlugField(unique=True, max_length=130, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio_base = models.PositiveIntegerField()
    imagen1 = models.ImageField(upload_to='productos/')
    imagen2 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='productos/', null=True, blank=True)
    es_destacado = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=120)
    tipo_insumo = [
        ("textil", "Textil"),
        ("taza", "Taza"),
        ("filamento", "Filamento 3D"),
        ("vinilo", "Vinilo"),
        ("tinta", "Tinta"),
        ("papeleria", "Papelería"),
        ("empaque", "Cajas"),
        ("otro", "Otro"),
    ]
    unidad_insumo = [
        ("mts", "Metros"),
        ("cms", "Centímetros"),
        ("kg", "Kilogramos"),
        ("gr", "Gramos"),
        ("Lts", "Litros"),
        ("pliegos", "Pliegos"),
        ("cc", "Centímetros Cúbicos"),
        ("ml", "Mililitros"),
        ("unidades", "Unidades"),
        ("otro", "Otro"),
    ]

    color_insumo = [
        ("negro", "Negro"),
        ("amarillo", "Amarillo"),
        ("azul", "Azul"),
        ("blanco", "Bolanco"),
        ("verde", "Verde"),
        ("rojo", "Rojo"),
        ("naranja", "Naranja"),
        ("morado", "Morado"),
        ("otro", "Otro"),
    ]
    slug = models.SlugField(max_length=130, unique=True, null=True)
    tipo = models.CharField(max_length=30, choices=tipo_insumo)
    cantidad = models.PositiveIntegerField()
    unidad = models.CharField(max_length= 30, choices=unidad_insumo, blank=True)
    marca = models.CharField(max_length=100, )
    color = models.CharField(max_length=20, choices=color_insumo)

    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=120)
    correo_cliente = models.EmailField(blank=True, null=True)
    telefono_cliente = models.CharField(max_length=20, blank=True, null=True)
    producto_requerido = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad_producto = models.PositiveIntegerField()
    pedido_img_1 = models.ImageField(upload_to='pedidos/', null=True, blank=True)
    pedido_img_2 = models.ImageField(upload_to='pedidos/', null=True, blank=True)
    pedido_img_3 = models.ImageField(upload_to='pedidos/', null=True, blank=True)
    
    plataforma_pedido = [
        ("whatsapp", "WhatsApp"),
        ("instagram","Instagram"),
        ("facebook", "Facebook"),
        ("presencial", "Presencial"),
        ("web", "Página Web"),
        ("otro", "Otro")
    ]

    estado_pedido = [
        ("solicitado", "Solicitado"),
        ("aprobado", "Aprobado"),
        ("en_proceso", "En proceso"),
        ("realizada", "Realizada"),
        ("entregada", "Entregada"),
        ("finalizada", "Finalizada"),
        ("cancelada", "Cancelada"),
    ]

    estado_pago = [
        ("pendiente", "Pendiente"),
        ("parcial", "Parcial"),
        ("pagado", "Pagado")
    ]

    plataforma = models.CharField(choices= plataforma_pedido, max_length= 30)
    estado_pedido_actual = models.CharField (choices= estado_pedido, max_length= 30, default="solicitado")
    estado_pago_actual = models.CharField(choices=estado_pago, max_length=30, default="pendiente")
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    notas_adicionales = models.TextField(blank=True, null=True)
    
    token_seguimiento = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True)

    def __str__(self):
        if self.producto_requerido:
            producto = self.producto_requerido.nombre
        else:
            producto = "Sin producto"
        return f"Pedido #{self.id} de {self.nombre_cliente} - {producto} - (Origen: {self.plataforma})"
    
    def puede_finalizar(self):
        return (
            self.estado_pedido_actual == 'entregada' and 
            self.estado_pago_actual == 'pagado'
        )

    def marcar_finalizado(self):
        if not self.puede_finalizar():
            raise ValidationError("El pedido no cumple con los requisitos para ser finalizado.")
        self.estado_pedido_actual = 'finalizada'
        self.save()