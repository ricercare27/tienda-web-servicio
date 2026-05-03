from django.urls import path
from .views import productos, producto_detalle, vista_catalogo, home, detalle_producto

urlpatterns = [
    path('', home),
    path('productos/', productos),
    path('productos/<int:producto_id>/', producto_detalle),
    path('catalogo/', vista_catalogo),
    path('productos/<int:producto_id>/', detalle_producto),
]
