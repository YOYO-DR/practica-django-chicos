#importo la clase de django para crear formularios y mis modelos
from django.forms import ModelForm
from .models import *

#creo la clase para mi modelo y lo heredo de ModelForm
class FormInventario(ModelForm):
  #inicializo el metodo init asi
  def __init__(self,*args, **kwargs):
      #llamo la funcion super para traerme el metodo init y todos sus valores
      super().__init__(*args, **kwargs)
      #creo la variable id para poner un id en el for de los label y id de los input
      id=0
      #accedo a la funcion visible_fields gracias a que la llame con el metodo super()
      for form in self.visible_fields():
        #estoy recorriendo todo los campos de cada valor del modelo
        #asi puedo agregar atributos a mis inputs y label si lo necesito, en este caso, clases de Bootstrap para los estilos, y su "id"
        form.field.widget.attrs.update({'class': 'form-control','id':f'{id}a'})
        form.label_attrs={'class': 'form-label','for':f'{id}'}
        id+=1
  class Meta:
    #en la clase Meta debo poner que modelo voy a trabajar
    model = Producto
    #con esto le digo que atributos de mi modelo crearle el input, en este caso le digo que todos
    fields = '__all__'
