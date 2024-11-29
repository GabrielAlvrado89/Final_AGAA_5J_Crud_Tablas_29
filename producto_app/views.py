from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.
def inicio_Producto(request):
    producto=Productos.objects.all()
    return render(request,"gestionarproducto.html",{"misproductos": producto})

def registrarProducto(request):
    id_producto=request.POST["txtidproducto"]
    id_proveedores=request.POST["txtidproveedores"]
    id_sucursal=request.POST["txtidsucursal"]
    TipoProducto=request.POST["txtproducto"]
    Cantidad=request.POST["txtcantidad"]
    NombreProducto=request.POST["txtnombreproducto"]
    Sucursal=request.POST["txtsucursal"]
    Correo=request.POST["txtcorreo"]
    NumTelefono=request.POST["txtNumTelefono"]
    precio=request.POST["txtprecio"]

    guardarProducto=Productos.objects.create(
    id_producto=id_producto, Cantidad=Cantidad, NombreProducto=NombreProducto,
    id_proveedores=id_proveedores, id_sucursal = id_sucursal, TipoProducto = TipoProducto, Sucursal = Sucursal,
    Correo=Correo, NumTelefono=NumTelefono, precio = precio)
    return redirect("producto")

def seleccionarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    return render(request,'editarproducto.html', {'misproductos': producto})

def editarProducto(request):
    id_producto=request.POST["txtidproducto"]
    id_proveedores=request.POST["txtidproveedores"]
    id_sucursal=request.POST["txtidsucursal"]
    TipoProducto=request.POST["txtproducto"]
    Cantidad=request.POST["txtcantidad"]
    NombreProducto=request.POST["txtnombreproducto"]
    Sucursal=request.POST["txtsucursal"]
    Correo=request.POST["txtcorreo"]
    NumTelefono=request.POST["txtNumTelefono"]
    precio=request.POST["txtprecio"]
    producto = Productos.objects.get(id_producto=id_producto)
    producto.id_producto = id_producto
    producto.id_proveedores = id_proveedores
    producto.id_sucursal = id_sucursal
    producto.Cantidad = Cantidad
    producto.NombreProducto = NombreProducto
    producto.TipoProducto = TipoProducto
    producto.Sucursal = Sucursal
    producto.Correo = Correo
    producto.NumTelefono = NumTelefono
    producto.precio = precio
    producto.save() # guarda registro actualizado
    return redirect("producto")

def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete() # borra el registro
    return redirect("producto")
