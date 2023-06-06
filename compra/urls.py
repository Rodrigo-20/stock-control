from django.urls import path
from .views import home, productos_view, producto_crear, proveedor_crear, proveedores, producto_borrar, \
    proveedor_borrar, producto_editar, proveedor_editar, producto_aumentar, producto_disminuir

urlpatterns = [
    path('', home, name="home"),
    path('producto/lista', productos_view, name="productos-lista"),
    path('producto/nuevo', producto_crear, name="producto-nuevo"),
    path('producto/borrar/<int:producto_id>', producto_borrar, name="producto-borrar"),
    path('producto/editar/<int:producto_id>', producto_editar, name="producto-editar"),
    path('producto/aumentar/<int:producto_id>', producto_aumentar, name="producto-aumentar"),
    path('producto/disminuir/<int:producto_id>', producto_disminuir, name="producto-disminuir"),
    path('proveedor/nuevo', proveedor_crear, name="proveedor-nuevo"),
    path('proveedor/lista', proveedores, name="proveedor-lista"),
    path('proveedor/borrar/<int:proveedor_id>', proveedor_borrar, name="proveedor-borrar"),
    path('proveedor/editar/<int:proveedor_id>', proveedor_editar, name="proveedor-editar"),

]
