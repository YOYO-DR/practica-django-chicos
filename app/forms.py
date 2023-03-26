from django.forms import ModelForm
from .models import *
class FormInventario(ModelForm):
  def __init__(self,*args, **kwargs):
      super().__init__(*args, **kwargs)
      id=0
      for form in self.visible_fields():
        form.field.widget.attrs.update({'class': 'form-control','id':f'{id}a'})
        form.label_attrs={'class': 'form-label','for':f'{id}'}
        id+=1
  class Meta:
    model = Producto
    fields = '__all__'
