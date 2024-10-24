from django.shortcuts import render

# Create your views here.
def pagina_principal(request):
    return render(request, 'home.html')  # Reemplaza con el nombre de tu archivo HTML