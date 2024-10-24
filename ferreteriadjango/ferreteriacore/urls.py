from django.urls import path
from .views import pagina_principal
from .views import productos_electrodomesticos

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('productos/electrodomesticos/', productos_electrodomesticos, name='productos_electrodomesticos'),  
]
