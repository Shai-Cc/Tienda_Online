from django import forms
from .models import Pedido, Contacto

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

class SeguimientoPedidoForm(forms.Form):
    token_seguimiento = forms.UUIDField(
        label='Número de pedido',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de pedido'})
    )

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'correo',
            'telefono',
            'asunto',
            'mensaje',
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "correo": forms.EmailInput(attrs={'class': 'form-control'}),
            "telefono": forms.TextInput(attrs={'class': 'form-control'}),
            "asunto": forms.Select(attrs={'class': 'form-control'}),
            "mensaje": forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }