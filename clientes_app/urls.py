from django.urls import path
from clientes_app import views 

urlpatterns = [
    path("cliente", views.inicio_clientes, name="cliente"),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path('seleccionarClientes/<id_cliente>', views.seleccionarClientes, name='seleccionarClientes'),
    path('editarClientes/', views.editarClientes, name='editarClientes'),
    path('borrarClientes/<id_cliente>', views.borrarClientes, name='borrarClientes'),
]