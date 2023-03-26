from django.db import models
from django.db.models.fields import *

#creo una clase categoria la cual tendra mis categorias para mis productos
class Categoria(models.Model):
   nombre=CharField(max_length=50,verbose_name='Nombre')
   def __str__(self):
    return self.nombre
   class Meta:
      #nombre de como quiero que aparezca la tabla en la base de datos
      db_table = 'categoria'

#creo el modelo mis productos
class Producto(models.Model):
    nombre=CharField(max_length=50,verbose_name='Nombre',null=False,blank=False)
    #en mi atributo categoria, lo relaciono con la clase/modelo categoria con una foreing key, por obligacion debo poner el on_delete y un valor, en este caso models.CASCADE, que significa que si se borra la clase Categoria, se borraran todos los registros que esten relacionados con esa clase
    categoria=models.ForeignKey(Categoria, verbose_name=("Categoria"), on_delete=models.CASCADE,null=False,blank=False)
    cantidad=CharField(max_length=50,verbose_name='Cantidad',null=False,blank=False)
    def __str__(self):
      return self.nombre
    class Meta():
      db_table = 'inventario'