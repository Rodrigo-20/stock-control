from django.forms import ModelForm
from .models import Producto, Proveedor
from django import forms


class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields= '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'

            }),
            'stock': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
            }),
            'precio': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control',
            })
        }


class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedor
        fields= '__all__'
        labels = {
            'nombre': 'Nombre / Denominacion',
            'apellido': 'Apellido / Responsabilidad',
            'numero_dni': 'DNI / CUIL',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'

            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'
            }),
            'numero_dni':forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
            }),
        }
