from django.shortcuts import render, redirect

from .forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor


def home(request):
    return render(request, 'home.html', {
        'active': request.path
    })


def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {
        'productos': productos,
        'active': request.path

    })


def producto_crear(request):
    form = ProductoForm()

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('productos-lista')

    return render(request, 'create_update_form.html', {
        "form": form,
        "submit_value": "Agregar Producto",
        "on_cancel_link": "productos-lista"
    })


def producto_borrar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()

    return redirect('productos-lista')


def producto_editar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()

            return redirect("productos-lista")

    form = ProductoForm(instance=producto)

    return render(request, 'create_update_form.html', {
        'form': form,
        "submit_value": "Agregar Producto",
        "on_cancel_link": "productos-lista"
    })

def producto_aumentar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.stock += 1
    producto.save()

    return redirect('productos-lista')



def producto_disminuir(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.stock -= 1
    producto.save()

    return redirect('productos-lista')
def proveedor_crear(request):
    form = ProveedorForm()

    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('proveedor-lista')

    return render(request, 'create_update_form.html', {
        "form": form,
        "submit_value": "Agregar Proveedor",
        "on_cancel_link": "proveedor-lista"
    })


def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {
        'proveedores': proveedores,
        'active': request.path
    })


def proveedor_borrar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedor.delete()

    return redirect('proveedor-lista')


def proveedor_editar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()

            return redirect("proveedor-lista")

    form = ProveedorForm(instance=proveedor)

    return render(request, 'create_update_form.html', {
        'form': form,
        "submit_value": "Agregar Proveedor",
        "on_cancel_link": "proveedor-lista"
    })