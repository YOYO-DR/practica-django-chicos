from config.wsgi import *
from app.models import *

for i in range(5):
  cate=input('Ingresa una categoria: ')
  Categoria(nombre=cate).save()