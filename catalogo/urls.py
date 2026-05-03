from django.urls import path
from .views import productos, producto_detalle, vista_catalogo, home, detalle_producto, admin_lista_productos, admin_producto_form, admin_borrar_producto
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home),
    path('productos/', productos),
    path('productos/<int:producto_id>/', producto_detalle),
    path('catalogo/', vista_catalogo),
    path('productos/<int:producto_id>/', detalle_producto),
    path('gestion/productos/', admin_lista_productos),
    path('gestion/productos/nuevo/', admin_producto_form),
    path('gestion/productos/editar/<int:producto_id>/', admin_producto_form),
    path('gestion/productos/borrar/<int:producto_id>/', admin_borrar_producto),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
