from django.contrib import admin
from .models import *

#agrego los modelos al panel de administrador para verlos desde el admin de django
admin.site.register(Producto)
admin.site.register(Categoria)
