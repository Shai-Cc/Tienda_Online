from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import get_object_or_404


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
        if self.action in ['retrieve', 'list', 'seguimiento']:
            return DetallePedidoSerializer
        return PedidoSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        
        if self.action == 'seguimiento':
            return [AllowAny()] 
        
        return [IsAdminUser()]
    
    @action(detail=False, methods=['get'], url_path='seguimiento/(?P<token>[^/.]+)')
    def seguimiento(self, request, token=None):
        pedido = get_object_or_404(Pedido, token_seguimiento=token)
        serializer = self.get_serializer(pedido)
        return Response(serializer.data, status=status.HTTP_200_OK)