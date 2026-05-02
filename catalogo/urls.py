from django.urls import path
from .views import lista_productos

urlpatterns = [
    path('productos/', lista_productos),
]
