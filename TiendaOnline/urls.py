"""
URL configuration for TiendaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainApp import login_views
from rest_framework.routers import DefaultRouter
from mainApp.api_views import InsumoViewSet

from mainApp import views

router = DefaultRouter()
router.register(r'insumos', InsumoViewSet, basename='insumo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('pedidoWeb/', views.realizar_pedido, name='pedido_web'),
    path('seguimientoPedido/', views.seguimiento_pedido, name='seguimiento_pedido'),
    path('login/', login_views.login_view, name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('registro/', login_views.registro_view, name='registro'),
    path('contacto/', views.contacto, name='contacto'),
    path('api/', include('mainApp.api_urls')),
    path('reporteSistema/', views.reporte_sistema, name='reporte_sistema'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)