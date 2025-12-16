from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import InsumoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'insumos', InsumoViewSet, basename='insumo')
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
]