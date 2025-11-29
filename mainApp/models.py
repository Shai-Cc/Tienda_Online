from django.db import models

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
    tipo = models.CharField(max_length=30, choices=tipo_insumo)
    cantidad = models.PositiveIntegerField()
    unidad = models.CharField(max_length= 30, choices=unidad_insumo, blank=True)
    marca = models.CharField(max_length=100, )
    color = models.CharField(max_length=20, choices=color_insumo)

    def __str__(self):
        return self.nombre

