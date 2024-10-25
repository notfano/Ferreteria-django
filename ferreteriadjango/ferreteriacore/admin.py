from django.contrib import admin
from .models import producto
from .models import admin_web
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'disponible','categoria')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'codigo', 'categoria')  # Campos que se pueden buscar

admin.site.register(producto, ProductoAdmin)



    


admin.site.register(admin_web)