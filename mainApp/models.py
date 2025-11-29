from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField (blank=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length= 120)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio_base = models.PositiveIntegerField()
    imagen1 = models.ImageField(upload_to='productos/')
    imagen2 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
