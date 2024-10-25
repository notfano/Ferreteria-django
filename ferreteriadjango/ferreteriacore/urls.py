from django.urls import path
from .views import pagina_principal
from .views import productos_electrodomesticos



urlpatterns = [
    path('', productos_electrodomesticos, name='productos_electrodomesticos'),
      
]

