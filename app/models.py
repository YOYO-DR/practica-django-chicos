from django.db import models
from django.db.models.fields import *

class Categoria(models.Model):
   nombre=CharField(max_length=50,verbose_name='Nombre')
   def __str__(self):
    return self.nombre
   class Meta:
      db_table = 'categoria'

class Producto(models.Model):
    nombre=CharField(max_length=50,verbose_name='Nombre',null=False,blank=False)
    categoria=models.ForeignKey(Categoria, verbose_name=("Categoria"), on_delete=models.CASCADE,null=False,blank=False)
    cantidad=CharField(max_length=50,verbose_name='Cantidad',null=False,blank=False)
    def __str__(self):
      return self.nombre
    class Meta():
      db_table = 'inventario'