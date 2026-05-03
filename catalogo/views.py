from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json
from django.shortcuts import render
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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


@login_required
def admin_lista_productos(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    productos = Producto.objects.all()
    return render(request, 'catalogo/admin_lista.html', {'productos': productos})


@login_required
def admin_producto_form(request, producto_id=None):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if producto_id:
        producto = Producto.objects.get(id=producto_id)
    else:
        producto = None

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/admin/productos/')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'catalogo/admin_form.html', {'form': form})


@login_required
def admin_borrar_producto(request, producto_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('/admin/productos/')

    return render(request, 'catalogo/admin_confirmar_borrado.html', {'producto': producto})
