from distutils.log import info
from django.shortcuts import render
from itertools import product
from Application.models import *
from Application.forms import *

# Create your views here.

def inicio(request):
    return render(request, "Application/inicio.html")

def producto(request):

    if request.method == 'Post':

        formulario = ProductoForm(request.POST)

        print(formulario)

        if formulario.is_valid:

            data = formulario.cleaned_data

            print(data)

            producto = Producto(nombre = info['nombre'],serie = info['serie'],tipo = info['tipo'])
            producto.save()

            return render(request,"Application/inicio.html")
    
    else:
        
        formulario = ProductoForm()
    
    return render(request,"App/producto.html",{"formulario":formulario})

    
def vendedor(request):

    if request.method == 'Post':

        formulario = VendedorForm(request.POST)

        print(formulario)

        if formulario.is_valid:

            data = formulario.cleaned_data

            print(data)

            vendedor = Vendedor(nombre = info['nombre'],apellido = info['apellido'],cuil = info['cuil'],DNI = info ['DNI'])
            vendedor.save()

            return render(request,"Application/inicio.html")
    
    else:
        
        formulario = VendedorForm()
    
    return render(request,"App/vendedor.html",{"formulario":formulario})


def cliente(request):

    if request.method == 'Post':

        formulario = ClienteForm(request.POST)

        print(formulario)

        if formulario.is_valid:

            data = formulario.cleaned_data

            print(data)

            cliente = Cliente(nombre = info['nombre'],apellido = info['apellido'],telefono = info['telefono'])
            cliente.save()

            return render(request,"Application/inicio.html")
    
    else:
        
        formulario = ClienteForm()
    
    return render(request,"App/cliente.html",{"formulario":formulario})

def buscador(request):

    if request.GET['producto']:

        producto = request.GET['producto']
        print(producto)

        vendedor = vendedor.objects.filter(producto_icontains = producto)
        print(vendedor)

        return render(request,"Application/inicio.html",{"vendedor":vendedor.values,"prod":producto})

    else:
        
        response = "N/A"

    return render (request,"Application/inicio.html",{"prod":response})