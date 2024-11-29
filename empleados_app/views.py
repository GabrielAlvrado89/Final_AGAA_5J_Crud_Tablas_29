from django.shortcuts import render,redirect
from .models import empleados
# Create your views here.
def inicio_empleados(request):
    empleado=empleados.objects.all()
    return render(request,"gestionarempleados.html",{"misempleados": empleado})

def registrarEmpleados(request):
    id_empleado=request.POST["txtidEmpleados"]
    Nombre_Completo=request.POST["txtnombre"]
    numtelefono=request.POST["txtnumtel"]
    CURP=request.POST["txtCURP"]
    RFC=request.POST["txtRFC"]
    Edad=request.POST["txtedad"]
    sexo=request.POST["txtsexo"]

    guardarEmpleados=empleados.objects.create(
    id_empleado=id_empleado, Nombre_Completo=Nombre_Completo, CURP=CURP,
    numtelefono=numtelefono, RFC=RFC, Edad=Edad, sexo=sexo)
    return redirect("empleado")

def seleccionarEmpleados(request, id_empleado):
    empleado = empleados.objects.get(id_empleado=id_empleado)
    return render(request,'editarempleados.html', {'misempleados': empleado})


def editarEmpleados(request):
    id_empleado=request.POST["txtidEmpleados"]
    Nombre_Completo=request.POST["txtnombre"]
    numtelefono=request.POST["txtnumtel"]
    CURP=request.POST["txtCURP"]
    RFC=request.POST["txtRFC"]
    Edad=request.POST["txtedad"]
    sexo=request.POST["txtsexo"]
    empleado = empleados.objects.get(id_empleado=id_empleado)
    empleado.id_empleado = id_empleado
    empleado.Nombre_Completo = Nombre_Completo
    empleado.numtelefono = numtelefono
    empleado.CURP = CURP
    empleado.RFC = RFC
    empleado.Edad = Edad
    empleado.sexo = sexo
    empleado.save() # guarda registro actualizado
    return redirect("empleado")


def borrarEmpleados(request, id_empleado):
    empleado = empleados.objects.get(id_empleado=id_empleado)
    empleado.delete() # borra el registro
    return redirect("empleado")
