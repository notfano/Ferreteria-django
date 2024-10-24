from django.shortcuts import render
from .models import producto

# Create your views here.
def pagina_principal(request):
    return render(request, 'home.html')  # Reemplaza con el nombre de tu archivo HTML

def productos_electrodomesticos(request):
    productos = producto.objects.filter(categoria='electrodomesticos')  # Filtrar por categoría
    return render(request, 'home.html', {'productos': productos})