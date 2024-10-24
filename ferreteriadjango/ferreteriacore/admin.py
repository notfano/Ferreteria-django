from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'disponible')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'codigo')  # Campos que se pueden buscar

admin.site.register(Producto, ProductoAdmin)