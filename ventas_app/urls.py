from django.urls import path
from ventas_app import views 

urlpatterns = [
    path("venta", views.inicio_ventas, name="venta"),
    path("registrarVentas/",views.registrarVentas,name="registrarVentas"),
    path('seleccionarVentas/<id_venta>', views.seleccionarVentas, name='seleccionarVentas'),
    path('editarVentas/', views.editarVentas, name='editarVentas'),
    path('borrarVentas/<id_venta>', views.borrarVentas, name='borrarVentas' ),
]