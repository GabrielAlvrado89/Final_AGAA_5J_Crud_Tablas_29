from django.shortcuts import render,redirect
from .models import ventas
# Create your views here.
def inicio_ventas(request):
    venta=ventas.objects.all()
    return  render(request,"gestionarventas.html",{"misventas":venta})

def registrarVentas(request):
    id_venta=request.POST["txtidventa"]
    id_Productos=request.POST["txtidProductos"]
    id_Clientes=request.POST["txtidClientes"]
    Cantidad=request.POST["txtCantidad"]
    Hora_venta=request.POST["txtHoraVenta"]
    Sucursal=request.POST["txtSucursal"]
    Marcas=request.POST["txtMarcas"]
    FormaPago=request.POST["txtFormaPago"]

    guardarVentas=ventas.objects.create(
    id_venta=id_venta, Cantidad=Cantidad, Hora_venta=Hora_venta,
    id_Productos=id_Productos,id_Clientes=id_Clientes,Sucursal=Sucursal,
    Marcas=Marcas,FormaPago=FormaPago)
    return redirect("venta")

def seleccionarVentas(request, id_venta):
    venta = ventas.objects.get(id_venta=id_venta)
    return render(request,'editarventas.html', {'misventas': venta})


def editarVentas(request):
    id_venta=request.POST["txtidventa"]
    id_Productos=request.POST["txtidProductos"]
    id_Clientes=request.POST["txtidClientes"]
    Cantidad=request.POST["txtCantidad"]
    Hora_venta=request.POST["txtHoraVenta"]
    Sucursal=request.POST["txtSucursal"]
    Marcas=request.POST["txtMarcas"]
    FormaPago=request.POST["txtFormaPago"]
    venta = ventas.objects.get(id_venta=id_venta)
    venta.id_venta = id_venta
    venta.id_Productos = id_Productos
    venta.id_Clientes = id_Clientes
    venta.Cantidad = Cantidad
    venta.Hora_venta = Hora_venta
    venta.Sucursal = Sucursal
    venta.Marcas = Marcas
    venta.FormaPago = FormaPago
    venta.save() # guarda registro actualizado
    return redirect("venta")


def borrarVentas(request, id_venta):
    venta = ventas.objects.get(id_venta=id_venta)
    venta.delete() # borra el registro
    return redirect("venta")
