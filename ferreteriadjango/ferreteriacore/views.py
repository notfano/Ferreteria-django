from django.shortcuts import render
from .models import producto

def pagina_principal(request):
    # Filtrar productos que están en oferta
    productos_en_oferta = producto.objects.filter(oferta=True)
    
    # Obtener categorías distintas y productos por categoría
    categorias = producto.objects.values_list('categoria', flat=True).distinct()
    productos_por_categoria = []

    for categoria in categorias:
        productos = producto.objects.filter(categoria=categoria)
        productos_por_categoria.append((categoria, productos))

    # Pasar ambos contextos a la plantilla
    return render(request, 'home.html', {
        'productos_por_categoria': productos_por_categoria,
        'productos_en_oferta': productos_en_oferta,
    })
