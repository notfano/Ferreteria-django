from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    oferta = models.BooleanField(default=False)
    codigo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    
class admin_web (models.Model):
    fondo = models.ImageField(upload_to='web/', null=True, blank=True)

