from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from .forms import *

#vista de la parte principal
def principal(request):
  datos = {
    'titulo':'Principal',
  }
  return render(request,'home.html',datos)

#vista para visualizar el inventario
def vistaInventario(request):
  datos = {
    'titulo':'Inventario',
    #en la clave 'inventario' le paso todos mis productos
    'inventario':Producto.objects.all()
  }
  return render(request,'inventario.html',datos)

#vista para agregar un producto
def agregarProducto(request):
    #si el metodo es GET le paso el formulario que cree para mi clase/modelo inventario
    if request.method=='GET':
      datos = {
            'titulo':'Agregar Producto',
            'form':FormInventario
          }
      return render(request,'agregar.html',datos)
    #si el metodo es POST voy a validar si el formulario fue valido
    if request.method=='POST':
      #creo una instacia del formulario con los datos que ingreso la persona la cual estan en request.POST
      form = FormInventario(request.POST)
      #verifico si es valido con ese metodo
      if form.is_valid():
        #si es valido, lo guardo
        form.save()
        #despues de guardar lo redirecciono a la vista inventario
        return redirect('inventario')

#vista/funcion para borrar un producto
def borrar(request,id_produ):
  #esta vista recibe un id para poder borrar un producto
  #los busco, y luego le aplico el metodo delete para borrarlo
  Producto.objects.filter(id=id_produ).delete()
  #lo redirecciono a la vista de inventario
  return redirect('inventario')

#vista para actualizar un producto
def actualizar(request,id_produ):
  #como voy a actualizar un producto, necesito saber que producto es, la cual lo traigo de la base de datos, el id lo pido por la url
  produ = Producto.objects.get(id=id_produ)
  #si es get, le paso el formulario con los datos del producto para que luego sea actualizado
  if request.method=='GET':
    datos = {
            'titulo':'Actualizar Producto',
            #en el formulario, le paso el registro el cual se va a actualizar, en el parametro de "instance"
            'form':FormInventario(instance=produ)
          }
    return render(request,'actu.html',datos)
  #si el metodo es post, osea, que ya mando el formulario, a la clase formulario le paso el request.POST y como vamos a actualizar, le pasamos en el parametro de "instance" el mismo registro/objeto traido de la base de datos, porque si no se lo pasamos, solo va a agregar otro producto
  if request.method=='POST':
    form = FormInventario(request.POST,instance=produ)
    #guardamos
    form.save()
    #lo redireccionamos a inventario
    return redirect('inventario')