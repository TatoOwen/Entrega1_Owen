from django.urls import path
from Application import views

urlpatterns = [
    path('',views.inicio, nombre = "Inicio"),
    path('Producto',views.producto, nombre = "Producto"),
    path('Vendedor',views.vendedor, nombre = "Vendedor"),
    path('Cliente',views.cliente, nombre = "Cliente"),
    path('Buscador',views.buscador),
]


    