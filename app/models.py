from django.db import models


class Categoria(models.Model):
  nombre = models.CharField(max_length=50,verbose_name='Nombre')

  class Meta:
    db_table = 'categoria'
  
  def __str__(self):
    return self.nombre

class Producto(models.Model):
  nombre = models.CharField(max_length=50,verbose_name='Nombre',null=True, blank=True)
  categoria = models.ForeignKey(Categoria,verbose_name='Categoria',on_delete=models.CASCADE,null=True, blank=True)
  cantidad = models.IntegerField()
  precioU = models.DecimalField(decimal_places=2, max_digits=9,verbose_name='Precio unidad')

  class Meta:
    db_table = 'producto'
  
  def __str__(self):
    return self.nombre