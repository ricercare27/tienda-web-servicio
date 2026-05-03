from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json
from django.shortcuts import render


@csrf_exempt
def productos(request):
    if request.method == 'GET':
        productos = list(Producto.objects.all().values())
        return JsonResponse(productos, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        producto = Producto.objects.create(
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            existencia=data['existencia']
        )
        return JsonResponse(
            {"mensaje": "Producto creado", "id": producto.id},
            status=201
        )

    return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def producto_detalle(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        return JsonResponse({"error": "Producto no encontrado"}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        producto.nombre = data.get('nombre', producto.nombre)
        producto.descripcion = data.get('descripcion', producto.descripcion)
        producto.precio = data.get('precio', producto.precio)
        producto.existencia = data.get('existencia', producto.existencia)
        producto.save()
        return JsonResponse({"mensaje": "Producto actualizado"})

    if request.method == 'DELETE':
        producto.delete()
        return JsonResponse({"mensaje": "Producto eliminado"})

    return HttpResponseNotAllowed(['PUT', 'DELETE'])


def vista_catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/lista.html', {'productos': productos})


def home(request):
    return render(request, 'catalogo/home.html')


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'catalogo/detalle.html', {'producto': producto})
