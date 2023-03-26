from config.wsgi import *
from app.models import *

#funcion para agregar mis categorias
for i in range(5):
  cate=input('Ingresa una categoria: ')
  Categoria(nombre=cate).save()