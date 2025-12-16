from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter 

from mainApp.models import Insumo, Pedido
from .serializers import InsumoSerializer, DetallePedidoSerializer, PedidoSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by("id")
    serializer_class = InsumoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo', 'unidad', 'color', 'marca']
    search_fields = ['nombre', 'marca', 'slug']
    ordering_fields = ['id', 'nombre', 'cantidad', 'marca']
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['plataforma', 'estado_pedido_actual', 'estado_pago_actual']
    search_fields = ['nombre_cliente', 'producto_requerido__nombre', 'token_seguimiento']
    ordering_fields = ['fecha_pedido', 'nombre_cliente']
    
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return DetallePedidoSerializer
        return PedidoSerializer