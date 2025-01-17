from django.urls import path
from empleados_app import views 

urlpatterns = [
    path("empleado", views.inicio_empleados, name="empleado"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path('seleccionarEmpleados/<id_empleado>', views.seleccionarEmpleados, name='seleccionarEmpleados'),
    path('editarEmpleados/', views.editarEmpleados, name='editarEmpleados'),
    path('borrarEmpleados/<id_empleado>', views.borrarEmpleados, name='borrarEmpleados'),
]