from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *

def principal(request):
  datos = {
    'titulo':'Principal',
    'usuario':User.objects.filter(pk=1),
  }
  return render(request,'home.html',datos)

def vistaInventario(request):
  datos = {
    'titulo':'Inventario',
    'inventario':Producto.objects.all()
  }
  return render(request,'inventario.html',datos)

def agregarProducto(request):
    if request.method=='GET':
      datos = {
            'titulo':'Agregar Producto',
            'form':FormInventario
          }
      return render(request,'agregar.html',datos)
    if request.method=='POST':
      form = FormInventario(request.POST)
      if form.is_valid():
        form.save()
        return redirect('inventario')

def borrar(request,id_produ):
  Producto.objects.filter(id=id_produ).delete()
  return redirect('inventario')