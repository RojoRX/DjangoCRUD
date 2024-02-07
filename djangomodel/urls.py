from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedido/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedido/new/', views.pedido_new, name='pedido_new'),
    path('pedido/<int:pk>/edit/', views.pedido_edit, name='pedido_edit'),
    path('pedido/<int:pk>/delete/', views.pedido_delete, name='pedido_delete'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    path('productos/', views.producto_list, name='producto_list'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('producto/new/', views.producto_new, name='producto_new'),
    path('producto/<int:pk>/edit/', views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
]