from django.urls import path
from .views import *

urlpatterns = [
    path('',principal,name='principal'),
    path('inventario/',vistaInventario,name='inventario'),
    path('agregarproducto/',agregarProducto,name='agregar'),
    #para recibir valores por la url debo ponerle <>, decirle el tipo de dato y un nombre
    path('borrar/<int:id_produ>/',borrar,name='borrar'),
    #en el actualizar le pido un valor tambien
    path('actualizar/<int:id_produ>/',actualizar,name='actualizar'),
]
