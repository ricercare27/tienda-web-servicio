from django.urls import path
from .views import (
    productos,
    producto_detalle,
    vista_catalogo,
    home,
    detalle_producto,
    admin_lista_productos,
    admin_producto_form,
    admin_borrar_producto
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),

    # API
    path('api/productos/', productos),
    path('api/productos/<int:producto_id>/', producto_detalle),

    # Vistas HTML
    path('catalogo/', vista_catalogo, name='lista_productos'),
    path('catalogo/producto/<int:producto_id>/',
         detalle_producto, name='detalle_producto'),

    # Gestión
    path('gestion/productos/', admin_lista_productos),
    path('gestion/productos/nuevo/', admin_producto_form),
    path('gestion/productos/editar/<int:producto_id>/', admin_producto_form),
    path('gestion/productos/borrar/<int:producto_id>/', admin_borrar_producto),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
