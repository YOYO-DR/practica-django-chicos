from django.urls import path
from .views import *

urlpatterns = [
    path('',principal,name='principal'),
    path('inventario/',vistaInventario,name='inventario'),
    path('agregarproducto/',agregarProducto,name='agregar'),
    path('borrar/<int:id_produ>/',borrar,name='borrar')
]
