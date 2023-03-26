from django.shortcuts import render
from .models import *

def principal(request):
  datos = {
    'titulo':'Principal'
  }
  return render(request,'principal.html',datos)

def inventario(request):
  datos ={
    'titulo':'Inventario',
    'productos': Producto.objects.all()
  }
  return render(request,'inventario.html',datos)