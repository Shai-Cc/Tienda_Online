from rest_framework import serializers
from .models import Insumo, Productos, Pedido

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ['id', 'nombre', 'slug', 'tipo', 'unidad', 'color', 'marca', 'cantidad']

class DetallePedidoSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(source='producto_requerido.nombre', read_only=True)
    slug_producto = serializers.CharField(source='producto_requerido.slug', read_only=True)
    precio_base_producto = serializers.IntegerField(source='producto_requerido.precio_base', read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id',
            'token_seguimiento',  
            'fecha_pedido',
            'nombre_cliente',
            'correo_cliente',
            'telefono_cliente',

            'producto_requerido',
            'nombre_producto',
            'slug_producto',
            'precio_base_producto',
            'cantidad_producto',

            'pedido_img_1',
            'pedido_img_2',
            'pedido_img_3',

            'plataforma',
            'estado_pedido_actual',
            'estado_pago_actual',
            'fecha_entrega',
            'notas_adicionales',
        ]
        read_only_fields = ['id', 'token_seguimiento', 'fecha_pedido']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'nombre_cliente',
            'correo_cliente',
            'telefono_cliente',

            'producto_requerido', 
            'cantidad_producto', 
            
            'pedido_img_1', 
            'pedido_img_2', 
            'pedido_img_3',

            'plataforma', 
            'estado_pedido_actual', 
            'estado_pago_actual', 
            'fecha_entrega', 
            'notas_adicionales']
        
    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        estado_pedido = attrs.get('estado_pedido_actual', getattr(instance, 'estado_pedido_actual', None))
        estado_pago = attrs.get('estado_pago_actual', getattr(instance, 'estado_pago_actual', None))
        plataforma = attrs.get('plataforma', getattr(instance, 'plataforma', None))
        producto = attrs.get('producto_requerido', getattr(instance, 'producto_requerido', None))

        if estado_pedido == 'finalizada' and estado_pago != 'pagado':
            raise serializers.ValidationError("No se puede marcar un pedido como finalizado si no está pagado el total.")
            

        if plataforma == 'web' and not producto:
            raise serializers.ValidationError("Para pedidos realizados en nuestra web, debe seleccionar un producto de nuestro catálogo.")
        
        return attrs