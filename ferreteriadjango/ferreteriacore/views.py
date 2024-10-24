from django.shortcuts import render
from .models import producto

# Create your views here.
def pagina_principal(request):
    return render(request, 'home.html')  # Reemplaza con el nombre de tu archivo HTML

def productos_electrodomesticos(request):
    categorias = producto.objects.values_list('categoria', flat=True).distinct()
    productos_por_categoria = []

    for categoria in categorias:
        productos = producto.objects.filter(categoria=categoria)
        productos_por_categoria.append((categoria, productos))

    return render(request, 'home.html', {'productos_por_categoria': productos_por_categoria})