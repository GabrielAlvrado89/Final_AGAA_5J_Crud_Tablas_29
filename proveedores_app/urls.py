from django.urls import path
from proveedores_app import views 

urlpatterns = [
    path("proveedor", views.inicio_Proveedor, name="proveedor"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path('seleccionarProveedor/<id_proveedores>', views.seleccionarProveedor, name='seleccionarProveedor'),
    path('editarProveedor/', views.editarProveedor, name='editarProveedor'),
    path('borrarProveedor/<id_proveedores>', views.borrarProveedor, name='borrarProveedor' ),
]