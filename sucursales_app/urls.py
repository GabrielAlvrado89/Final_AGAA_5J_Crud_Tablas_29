from django.urls import path
from sucursales_app import views 

urlpatterns = [
    path("sucursal", views.inicio_sucursal, name="sucursal"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path('seleccionarSucursal/<id_sucursal>', views.seleccionarSucursal, name='seleccionarSucursal'),
    path('editarSucursal/', views.editarSucursal, name='editarMateria'),
    path('borrarSucursal/<id_sucursal>', views.borrarSucursal, name='borrarSucursal' ),
]