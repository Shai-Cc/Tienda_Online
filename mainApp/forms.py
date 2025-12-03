from django import forms
from .models import Pedido

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nombre_cliente',
            'correo_cliente',
            'telefono_cliente',
            'producto_requerido',
            'cantidad_producto',
            'fecha_entrega',
            'pedido_img_1',
            'pedido_img_2',
            'pedido_img_3',
            "notas_adicionales",
        ]

        widgets = {
            "nombre_cliente": forms.TextInput(attrs={'class': 'form-control'}),
            "correo_cliente": forms.EmailInput(attrs={'class': 'form-control'}),
            "telefono_cliente": forms.TextInput(attrs={'class': 'form-control'}),
            "cantidad_producto": forms.NumberInput(attrs={'class': 'form-control'}),
            "notas_adicionales": forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }