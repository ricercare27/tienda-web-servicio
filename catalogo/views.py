from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all()
    data = list(productos.values())
    return JsonResponse(data, safe=False)
