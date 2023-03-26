from django.shortcuts import render,redirect,get_object_or_404
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

def actualizar(request,id_produ):
  produ = get_object_or_404(Producto,pk=id_produ)
  if request.method=='GET':
    datos = {
            'titulo':'Actualizar Producto',
            'form':FormInventario(instance=produ)
          }
    return render(request,'actu.html',datos)
  if request.method=='POST':
    form = FormInventario(request.POST,instance=produ)
    form.save()
    return redirect('inventario')