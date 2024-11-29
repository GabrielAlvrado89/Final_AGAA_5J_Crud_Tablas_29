from django.shortcuts import render,redirect
from .models import marcas
# Create your views here.
def inicio_Marcas(request):
    marca=marcas.objects.all()
    return render(request,"gestionarmarcas.html",{"mismarcas": marca})

def registrarMarcas(request):
    id_marcas=request.POST["txtidmarcas"]
    id_sucursal=request.POST["txtidsucursal"]
    id_producto=request.POST["txtidproducto"]
    Nombre_Marca=request.POST["txtnombremarca"]
    Numtelefono=request.POST["txtNumTelefono"]
    Correo=request.POST["txtcorreo"]

    guardarMarcas=marcas.objects.create(
    id_marcas=id_marcas, Nombre_Marca=Nombre_Marca, Correo=Correo,
    id_sucursal=id_sucursal, id_producto=id_producto, Numtelefono=Numtelefono)
    return redirect("marcas")

def seleccionarMarcas(request, id_marcas):
    marca = marcas.objects.get(id_marcas=id_marcas)
    return render(request,'editarmarcas.html', {'mismarcas': marca})

def editarMarcas(request):
    id_marcas=request.POST["txtidmarcas"]
    id_sucursal=request.POST["txtidsucursal"]
    id_producto=request.POST["txtidproducto"]
    Nombre_Marca=request.POST["txtnombremarca"]
    Numtelefono=request.POST["txtNumTelefono"]
    Correo=request.POST["txtcorreo"]
    marca = marcas.objects.get(id_marcas=id_marcas)
    marca.id_marcas = id_marcas
    marca.id_sucursal = id_sucursal
    marca.id_producto = id_producto
    marca.Nombre_Marca = Nombre_Marca
    marca.Numtelefono = Numtelefono
    marca.Correo = Correo
    marca.save() # guarda registro actualizado
    return redirect("marcas")


def borrarMarcas(request, id_marcas):
    marca = marcas.objects.get(id_marcas=id_marcas)
    marca.delete() # borra el registro
    return redirect("marcas")
