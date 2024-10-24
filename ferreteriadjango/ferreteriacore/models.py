from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"