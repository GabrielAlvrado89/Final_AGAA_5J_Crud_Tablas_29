from django.shortcuts import render,redirect
from .models import clientes
# Create your views here.
def inicio_clientes(request):
    cliente=clientes.objects.all()
    return  render(request,"gestionarclientes.html",{"misclientes":cliente})

def registrarClientes(request):
    id_cliente=request.POST["txtidcliente"]
    NombreCompleto=request.POST["txtnombre"]
    Edad=request.POST["txtedad"]
    NumeroTelefono=request.POST["txtNumTel"]
    Correo=request.POST["txtCorreo"]
    Domicilio=request.POST["txtDomicilio"]
    FormaPago=request.POST["txtFormaPago"]

    guardarVentas=clientes.objects.create(
    id_cliente=id_cliente, Correo=Correo, Domicilio=Domicilio,
    NombreCompleto=NombreCompleto, Edad=Edad, NumeroTelefono=NumeroTelefono, FormaPago=FormaPago)
    return redirect("cliente")

def seleccionarClientes(request, id_cliente):
    cliente = clientes.objects.get(id_cliente=id_cliente)
    return render(request,'editarclientes.html', {'misclientes': cliente})

def editarClientes(request):
    id_cliente=request.POST["txtidcliente"]
    NombreCompleto=request.POST["txtnombre"]
    Edad=request.POST["txtedad"]
    NumeroTelefono=request.POST["txtNumTel"]
    Correo=request.POST["txtCorreo"]
    Domicilio=request.POST["txtDomicilio"]
    FormaPago=request.POST["txtFormaPago"]
    cliente = clientes.objects.get(id_cliente=id_cliente)
    cliente.id_cliente = id_cliente
    cliente.NombreCompleto = NombreCompleto
    cliente.Edad = Edad
    cliente.NumeroTelefono = NumeroTelefono
    cliente.Correo = Correo
    cliente.Domicilio = Domicilio
    cliente.FormaPago = FormaPago
    cliente.save() # guarda registro actualizado
    return redirect("cliente")

def borrarClientes(request, id_cliente):
    cliente = clientes.objects.get(id_cliente=id_cliente)
    cliente.delete() # borra el registro
    return redirect("cliente")