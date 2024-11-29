from django.shortcuts import render,redirect
from .models import Proveedores
# Create your views here.
def inicio_Proveedor(request):
    proveedor=Proveedores.objects.all()
    return render(request,"gestionarproveedores.html",{"misproveedores": proveedor})

def registrarProveedor(request):
    id_proveedores=request.POST["txtidproveedor"]
    Producto=request.POST["txtproducto"]
    Cantidad=request.POST["txtcantidad"]
    Sucursal=request.POST["txtSucursal"]
    Telefono=request.POST["txtTelefono"]
    correo=request.POST["txtCorreo"]
    Hora=request.POST["txtHora"]
    FechaVenta=request.POST["txtFechaventa"]

    guardarProveedor=Proveedores.objects.create(
    id_proveedores=id_proveedores, Producto=Producto ,Cantidad=Cantidad, Sucursal=Sucursal,
    Telefono=Telefono, correo=correo, Hora=Hora, FechaVenta=FechaVenta)
    return redirect("proveedor")

def seleccionarProveedor(request, id_proveedores):
    proveedor = Proveedores.objects.get(id_proveedores=id_proveedores)
    return render(request,'editarproveedores.html', {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedores=request.POST["txtidproveedor"]
    Producto=request.POST["txtproducto"]
    Cantidad=request.POST["txtcantidad"]
    Sucursal=request.POST["txtSucursal"]
    Telefono=request.POST["txtTelefono"]
    correo=request.POST["txtCorreo"]
    Hora=request.POST["txtHora"]
    FechaVenta=request.POST["txtFechaventa"]
    proveedor = Proveedores.objects.get(id_proveedores=id_proveedores)
    proveedor.id_proveedores = id_proveedores
    proveedor.producto = Producto
    proveedor.Cantidad = Cantidad
    proveedor.Sucursal = Sucursal
    proveedor.Telefono = Telefono
    proveedor.correo = correo
    proveedor.Horar = Hora
    proveedor.FechaVenta = FechaVenta
    proveedor.save() # guarda registro actualizado
    return redirect("proveedor")


def borrarProveedor(request, id_proveedores):
    proveedor = Proveedores.objects.get(id_proveedores=id_proveedores)
    proveedor.delete() # borra el registro
    return redirect("proveedor")
