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
            "notas_adicionales",
        ]